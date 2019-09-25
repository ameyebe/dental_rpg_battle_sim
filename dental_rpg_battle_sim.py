# dental_rpg_battle_sim.py
# date: 1/07/2019
# Author: Benjamin Ameye

import random
import sys
import time
try: color = sys.stdout.shell
except AttributeError: raise RuntimeError("use IDLE")

victories = 0
grade = 'none'
# types of attacks
ATK = 'Attack that lands once'
M_ATK = 'Multi hitting Attack'
BUFF = 'Next attack will deal a extra 50% damage (except power attacks)'
HEAL = 'Heal 1 character by 75 HP'
ALL_HEAL = 'Heals all characters by 75HP'
REVIVAL = 'Revives 1 fallen character with 200HP'
ULTIMATE = 'The characters strongest attack'
M_ULTIMATE = 'The characters strongest attack (chance to land multible times)'


# item types
H = 'Heals 1 character by 75 HP' 
A_H = 'Heals all characters by 50 HP'
F_H =  'Fully heals 1 character' 
R = 'Restores all characters HP and MP' 
MP_R = 'Restores 1 characters MP by 25'
REV = 'Revives 1 character with 175 HP'
REV_F = 'Revives 1 character with max HP'
GAIN_STR = 'Gives a character 2 STR'

# Item information
single_item_letters = ['A', 'B', 'C', 'D', 'E']
single_items_carried = ['Tooth cleaner', 'Mint', 'power paste', 'Dentist spray', 'Tooth enhancer']
single_item_types = [H, F_H, MP_R, REV, GAIN_STR]
single_item_amounts = [4, 3, 5, 3, 3]
all_item_letters = ['A', 'B']
all_items_carried = ['Mouthwash', 'Gold toothpaste']
all_item_types = [A_H, R]
all_item_amounts = [3, 2]

#The characters max HP, MP, STR and list of special attacks
# Paste man attacks, HP, STR and MP
paste_man_HP = 475
paste_man_HP_max = 475
paste_man_MP = 120
paste_man_MP_max = 120
paste_man_STR = 3
paste_man_STR_max = 8
paste_man_letters = ['A', 'B', 'C']
paste_man_names = ['Toothpaste squirt', 'Tooth pick clean', 'clean breathe']
paste_man_types = [ATK, ATK, M_ATK]
paste_man_costs = [9, 16, 19]
paste_man_damage = {1: [50, 60], 2: [45, 65], 3: [55, 60]}
paste_man_STR_letters = ['A', 'B', 'C', 'D']
paste_man_STR_names = ['Brush bow', 'Paste rain', 'freshness spray', 'pure paste']
paste_man_STR_types = [ATK, M_ATK, M_ATK, ULTIMATE]
paste_man_STR_required = [2, 3, 5, 8]
paste_man_STR_damage = {1: [70, 75], 2: [30, 40], 3: [40, 55], 4: [105, 115]}
paste_man_normal_attack = [15, 25]
# Brusher attacks, HP, STR and MP
brusher_HP = 3
brusher_HP_max = 410
brusher_MP = 115
brusher_MP_max = 115
brusher_STR = 3
brusher_STR_max = 10
brusher_special_attacks = ['A', 'B', 'C', 'D']
brusher_special_attack_names = ['Brush smack', 'Clean rinse', 'Ultimate scrub', 'Add toothpaste']
brusher_types = [ATK, M_ATK, ATK, BUFF]
brusher_costs = [10, 11, 20, 22]
brusher_damage = {1: [40, 45], 2: [40, 50], 3: [55, 65]}
brusher_normal_attack = [30, 35]
brusher_STR_letters = ['A', 'B', 'C']
brusher_STR_names = ['Tooth brush rain', 'Cross brush', 'brush spear']
brusher_STR_types = [M_ATK, ATK, ULTIMATE]
brusher_STR_required = [5, 7, 10]
brusher_STR_damage = {1: [30, 40], 2: [65, 80], 3: [115, 130]}
# Mouth washer attacks, healing abilities, HP, STR and MP
mouth_washer_HP = 390
mouth_washer_HP_max = 390
mouth_washer_MP = 145
mouth_washer_MP_max = 145
mouth_washer_attacks = ['A', 'B']
mouth_washer_special_attacks_names = ['Dental floss whip', 'Mouthwash Blast']
mouth_washer_types = [M_ATK, ATK]
mouth_washer_damage = {1: [25, 35], 2: [50, 65]}
mouth_washer_costs = [8, 16, 21, 22]
mouth_washer_normal_attack = [15, 20]
mouth_washer_healing_abilities = ['A', 'B', 'C']
mouth_washer_healing_ability_names = ['Teeth cleaner', 'Full clean', 'Germ removal']
mouth_washer_healing_types = [HEAL, ALL_HEAL, REVIVAL]
mouth_washer_healing_costs = [16, 22, 30]
mouth_washer_STR = 3
mouth_washer_STR_max = 6
mouth_washer_STR_letters = ['A', 'B']
mouth_washer_STR_names = ['mouth wash whip', 'electric toothbrush rinces']
mouth_washer_STR_types = [M_ATK, M_ULTIMATE]
mouth_washer_STR_required = [4, 6]
mouth_washer_STR_damage = {1: [40, 45], 2: [50, 60]}


team = {'A': 'paste man', 'B': 'Brusher', 'C': 'mouth_washer'}
# Enemies HP, attacks and the damage they do
# Bacteria information
bacteria_HP = 350
bacteria_attacks = ['Normal attack','Rain of germs', 'infected strike', 'Bad breathe']
bacteria_damage = {1: [50, 65], 2:[30, 50], 3: [90, 110], 4: [50, 75]}
bacteria_types = [ATK, M_ATK, ATK, M_ATK]
# infected tooth information
infected_tooth_HP = 300
infected_tooth_attacks = ['Normal attack', 'decaying spit', 'infected bite', 'Potato chips']
infected_tooth_damage = {1: [40, 50], 2: [70, 90], 3: [90, 110], 4: [0]}
infected_tooth_types = [ATK, ATK, ATK, BUFF]
# Germ pile information
germ_pile_HP = 310
germ_pile_attacks = ['Normal attack', 'Actinomyces whip', 'Fusobacterium rain', 'Candida spray']
germ_pile_damage = {1: [20, 40], 2: [35, 50], 3: [40, 55], 4: [60, 80]}
germ_pile_types = [ATK, M_ATK, M_ATK, M_ATK]
# Candy teeth information
candy_teeth_HP = 315
candy_teeth_attacks = ['normal attack', 'chewing gum whip', 'Candy cane', 'lollipop disc', 'Bag of sugar']
candy_teeth_damage = {1: [70, 90], 2: [55, 70], 3: [80, 85], 4: [90, 100], 5: [0]}
candy_teeth_types = [ATK, M_ATK, M_ATK, ATK, BUFF]

# List of bosses and characters
bosses = ['Bacteria', 'Infected tooth', 'germ pile', 'candy teeth']
team = ['paste man', 'brusher', 'mouth washer']


actions = ('''Enter which of the following actions you want to performs
            A to use your normal attack
            
            P to use your power attacks
            
            S to use your special attacks
            
            B to block
            
            I to select a item
            
            enter H for help''')

actions_2 = ('''Enter which of the following actions you want to performs
            A to use your normal attack
            
            P to use your power attacks
            
            S to use your either use a special attack or a healing ability
            
            B to block
            
            I to select a item

            enter H for help''')
def single_select_item(HP, HP_max, MP, MP_max, STR, STR_max, end_turn, character, type_of_item):
    '''This function is called if the user wants to use an item that'll affect 1 character, it'll return a variable called
end turn as true if the item could be used (example: character doesn't have max HP and needs healing), and return it as\
false if the item couldn't be used (example: character has max HP and doesn't need healing)'''
    if type_of_item == H:   # I item that heals 1 character by 75HP
        if HP > 0:
            if HP < HP_max:
                HP += 75
                if HP > HP_max:
                    HP = HP_max
                    print("\n{} HP = {}/{}\n".format(character, HP, HP_max))
                    end_turn = True
                    print("\n==----Healed----==\n")
                    time.sleep(1.5)
                    
                else:
                    print("\n{} HP = {}/{}\n".format(character, HP, HP_max))
                    print("\n==----Healed----==\n")
                    time.sleep(1.5)
                    end_turn = True

        if HP == HP_max:
            print("\nAlready at max HP\n")
                
        elif HP == 0:
             print("\n{} is unconcious\n".format(character))
        
                    
    elif type_of_item == F_H: # A item that fully heals 1 character
        if HP > 0:
            if HP < HP_max:
                HP = HP_max
                end_turn = True
                print("HP fully restored")
                print("\n{} HP = {}/{}\n".format(character, HP, HP_max))
                print("\n==----Fully Healed----==\n")
                time.sleep(1.5)
            elif HP == HP_max:
                print("Already at max HP")
        elif HP == 0:
                print("\n{} is Unconcious\n".format(character))         

    elif type_of_item == MP_R:  # A item that restores 25MP to a character
        if HP > 0:
            if MP < MP_max:
                MP += 25
                if MP > MP_max:
                    MP = MP_max
                    print("\n{} MP = {}/{}\n".format(character, MP, MP_max))
                    print("\n==----MP restored----==\n")
                    time.sleep(1.5)
                    end_turn = True
                else:
                    print("\n{} MP = {}/{}\n".format(character, MP, MP_max))
                    print("\n==----MP restored----==\n")
                    time.sleep(1.5)
                    end_turn = True
            elif MP == MP_max:
                print("Already at max MP")
        elif HP == 0:
            print("\n{} is unconcious\n".format(character))      
                    
    elif type_of_item == REV: # A item that revives a fallen character
        if HP == 0:
            HP += 175
            print("{} revived".format(character))
            print("\n{} HP = {}/{}\n".format(character, HP, HP_max))
            print("\n==----Revived----==\n")
            time.sleep(1.5)
            end_turn = True
        elif HP > 0:
            print("\n{} is already concious".format(character))

    elif type_of_item == GAIN_STR:  # A item that gives 1 character 2 STR
        if HP > 0:
            if STR < STR_max:
                STR += 2
                if STR > STR_max:
                    STR = STR_max
                    print("\n==----Gained STR----==\n")
                    print("\n{} STR = {}/{}\n".format(character, STR, STR_max))
                    time.sleep(1.5)
                    end_turn = True
                elif STR < STR_max:
                    print("\n==----Gained 2 STR----==\n")
                    print("\n{} STR = {}/{}\n".format(character, STR, STR_max))
                    time.sleep(1.5)
                    end_turn = True
            elif STR == STR_max:
                print("\nAlready at max STR\n")
        elif HP == 0:
             print("\n{} is unconcious\n".format(character))

    return HP, MP, STR, end_turn

def all_item(paste_man_HP, paste_man_MP, brusher_HP, brusher_MP, mouth_washer_HP, mouth_washer_MP, type_of_item):
    '''This function is ued if the user wants to use a item that'll affact all characters (Provided that character is concious)'''
    if type_of_item == A_H: # Heal any concious characters by 50HP (provided that character is concious)
        heal_paste_man = True
        while heal_paste_man == True:
            if paste_man_HP > 0:
                paste_man_HP += 50
                heal_paste_man = False
            elif paste_man_HP == 0:
                print("Paste man is unconcious")
                heal_paste_man = False

        heal_brusher = True
        while heal_brusher == True:
            if brusher_HP > 0:
                brusher_HP += 50
                heal_brusher = False
            elif brusher_HP == 0:
                print("brusher is unconcious")
                heal_brusher = False

        heal_mouth_washer = True
        while heal_mouth_washer == True:
            if mouth_washer_HP > 0:
                mouth_washer_HP += 50
                heal_mouth_washer = False
            elif mouth_washer_HP == 0:
                print("Mouth washer is unconcious")
                heal_mouth_washer = False

        if paste_man_HP > 475:
            paste_man_HP = 475
            print("\nPaste man HP = {}/475\n".format(paste_man_HP))
        else:
            print("\nPaste man HP = {}/475\n".format(paste_man_HP))

                    
        if brusher_HP > 410:
            brusher_HP = 410
            print("\nbrusher HP = {}/410\n".format(brusher_HP))
        else:
             print("\nbrusher HP = {}/410\n".format(brusher_HP))

        if mouth_washer_HP > 390:
            mouth_washer_HP = 390
            print("\nMouth washer HP = {}/390\n".format(mouth_washer_HP))
        else:
            print("\nMouth washer HP = {}/390\n".format(mouth_washer_HP))

        print("==----All characters healed----==")
        time.sleep(1.5)


    elif type_of_item == R: # restore all characters HP and MP to max (provided that character is concious)
        restore_paste_man = True
        while restore_paste_man == True:
            if paste_man_HP > 0:
                paste_man_HP = 475
                paste_man_MP = 120
                print("\nPaste man HP = {}/475".format(paste_man_HP))
                print("Paste man MP = {}/120".format(paste_man_MP))
                restore_paste_man = False
            elif paste_man_HP == 0:
                print("\nPaste man is unconcious\n")
                restore_paste_man = False

        restore_brusher = True
        while restore_brusher == True:
            if brusher_HP > 0:
                brusher_HP = 410
                brusher_MP = 115
                print("\nBrusher HP = {}/410".format(brusher_HP))
                print("brusher MP = {}/115".format(brusher_MP))
                restore_brusher = False
            elif brusher_HP == 0:
                print("\nBrusher is unconcious\n")
                restore_brusher = False

        restore_mouth_washer = True
        while restore_mouth_washer == True:
            if mouth_washer_HP > 0:
                mouth_washer_HP = 390
                mouth_washer_MP = 145
                print("\nMouth washer HP = {}/390".format(mouth_washer_HP))
                print("Mouth washer MP = {}/145\n".format(mouth_washer_MP))
                restore_mouth_washer = False
            elif mouth_washer_HP == 0:
                print("\nBrusher is unconcious\n")
                restore_mouth_washer = False
                    
        print("=----HP and MP restored----=")
        time.sleep(1.5)
                
    return paste_man_HP, paste_man_MP, brusher_HP, brusher_MP, mouth_washer_HP, mouth_washer_MP


def normal_attack(B_HP, norm, buff, STR, STR_max):
    '''This code is called if the user chooses to use a normal attack, when this function is called the numbers for the
    normal attack damage for the current character is called so the code can select a random number between the 2 numbers'''
    connect = random.randint(1,5)
    if connect == 5:
        print('miss')
        buff = False
    else:
        print('Hit')
        damage_1 = norm[0]
        damage_2 = norm[1]
        damage_dealt = random.randint(damage_1, damage_2)
        if buff == True:
            boosted_damage = damage_dealt * 1.5
            print("Your attack was buffed")
            boosted_damage = int(boosted_damage)
            B_HP -= boosted_damage
            print("\nYou dealt {} damage\n".format(boosted_damage))
            buff = False

        elif buff == False:
            B_HP -= damage_dealt
            print("You dealt {} damage".format(damage_dealt))
        if STR < STR_max:
            STR += 1
            print("STR = {}/{}".format(STR, STR_max))
            
    return B_HP, buff, STR

def enemy_attack(name_of_ATK, attack_type, dam, HP, HP_max, char, block, enemy_turn, buff):
    '''The enemy will randomly choose a attack from their particular list of attacks and will try to use it on 1 of the characters, which will be selected before
    this function is called. if the attack hits it'll deal damage equal to a random number between 2 different numbers'''
    select = True
    while select == True:
        attack_used = random.choice(name_of_ATK)
        pick = name_of_ATK.index(attack_used)
        type_of_attack = attack_type[pick]
        color.write("\n{}\n".format(attack_used), "COMMENT")
        if type_of_attack == ATK:   # a attack that lands once if it connects
            connect = random.randint(1, 4)
            if connect == 1 or connect == 2 or connect == 3:
                damage_1 = dam[pick + 1][0]
                damage_2 = dam[pick + 1][1]
                damage_dealt = random.randint(damage_1, damage_2)
                color.write('\nHit\n', "COMMENT")
                if buff == True:
                    boosted_damage = damage_dealt * 1.5
                    boosted_damage = int(boosted_damage)
                    color.write("\nThe attack was buffed\n", "COMMENT")
                    if block == True:
                        color.write('{} was blocking\n'.format(char), "COMMENT")
                        decreased_damage = boosted_damage / 2
                        decreased_damage = int(decreased_damage)
                        HP -= decreased_damage
                        buff = False
                        color.write("\n{} took {} damage\n".format(char, decreased_damage), "COMMENT")
                        if HP < 0:
                            HP = 0
                            print("{} has fallen".format(char))
                            enemy_turn = False
                            select = False
                        else:
                            print("{} HP = {}".format(char, HP))
                            enemy_turn = False
                            select = False
                            buff = False
                    elif block == False:
                        HP -= boosted_damage
                        buff = False
                        print("{} took {} damage".format(char, boosted_damage))
                        if HP < 0:
                            HP = 0
                            print("{} has fallen".format(char))
                            enemy_turn = False
                            select = False
                        else:
                            print("\n==----{} HP = {}/{}----==\n".format(char, HP, HP_max))
                            time.sleep(1.5)
                            enemy_turn = False
                            select = False

                    

                elif buff == False:
                    if block == True:
                        print('{} was blocking'.format(char))
                        decreased_damage = damage_dealt / 2
                        decreased_damage = int(decreased_damage)
                        HP -= decreased_damage
                        print("{} took {} damage".format(char, decreased_damage))
                        if HP < 0:
                            HP = 0
                            print("{} has fallen".format(char))
                            enemy_turn = False
                            select = False
                        else:
                            print("\n==----{} HP = {}/{}----==\n".format(char, HP, HP_max))
                            time.sleep(1.5)
                            enemy_turn = False
                            select = False
                    else:
                        HP -= damage_dealt
                        print("{} took {} damage".format(char, damage_dealt))
                        if HP < 0:
                            HP = 0
                            print("{} has fallen".format(char))
                            enemy_turn = False
                            select = False
                        else:
                            print("\n==----{} HP = {}/{}----==\n".format(char, HP, HP_max))
                            time.sleep(1.5)
                            enemy_turn = False
                            select = False
            else:
                print('Miss')
                select = False
                enemy_turn = False
                buff = False
                
        elif type_of_attack == M_ATK:   # a attack that'll hit the target multible times if it hits
            connect = random.randint(1,4)
            if connect == 1 or connect == 2 or connect == 3:
                damage_1 = dam[pick + 1][0]
                damage_2 = dam[pick + 1][1]
                hits = random.randint(1, 5)
                damage_dealt = random.randint(damage_1, damage_2) * hits
                color.write('\nHit\n', "COMMENT")
                if buff == True:
                    color.write("The attack was buffed\n", "COMMENT")
                    boosted_damage = damage_dealt * 1.5
                    boosted_damage = int(boosted_damage)
                    color.write("The attack landed {} times".format(hits), "COMMENT")
                    if block == True:
                        print('{} was blocking'.format(char))
                        decreased_damage = boosted_damage / 2
                        decreased_damage = int(decreased_damage)
                        HP -= decreased_damage
                        buff = False
                        print("{} took {} damage".format(char, decreased_damage))
                    
                        if HP < 0:
                            HP = 0
                            print("{} has fallen".format(char))
                            enemy_turn = False
                            select = False
                        else:
                            print("\n==----{} HP = {}/{}----==\n".format(char, HP, HP_max))
                            time.sleep(1.5)
                            enemy_turn = False
                            select = False
                    
                    else:
                        HP -= boosted_damage
                        print("{} took {} damage".format(char, boosted_damage))
                        buff = False
                        if HP < 0:
                            HP = 0
                            print("{} has fallen".format(char))
                            enemy_turn = False
                            select = False
                        else:
                            print("\n==----{} HP = {}/{}----==\n".format(char, HP, HP_max))
                            time.sleep(1.5)
                            enemy_turn = False
                            select = False
                elif buff == False:
                    color.write("The attack landed {} times\n".format(hits), "COMMENT")
                    if block == True:
                        print('{} was blocking'.format(char))
                        decreased_damage = damage_dealt / 2
                        decreased_damage = int(decreased_damage)
                        HP -= decreased_damage
                        print("{} took {} damage".format(char, damage_dealt))
                    
                        if HP < 0:
                            HP = 0
                            print("{} has fallen".format(char))
                            enemy_turn = False
                            select = False
                        else:
                            print("\n==----{} HP = {}/{}----==\n".format(char, HP, HP_max))
                            time.sleep(1.5)
                            enemy_turn = False
                            select = False
                    
                    elif block == False:
                        HP -= damage_dealt
                        print("{} took {} damage".format(char, damage_dealt))
                        if HP < 0:
                            HP = 0
                            print("{} has fallen".format(char))
                            enemy_turn = False
                            select = False
                        else:
                            print("\n==----{} HP = {}/{}----==\n".format(char, HP, HP_max))
                            time.sleep(1.5)
                            enemy_turn = False
                            select = False
            else:
                print('Miss')
                enemy_turn = False
                select = False
                buff = False

        elif type_of_attack == BUFF:    # The next damage of the attack the boss uses next will be multiplied by 1.5
            if buff == False:
                buff = True
                color.write("Buffed and ready\n", "COMMENT")
                enemy_turn = False
                select = False
            elif buff == True:
                color.write("Selecting attack", "COMMENT")
            
    return HP, enemy_turn, buff
    


def special_attack(letter_of_ATK, name_of_ATK, type_of_ATK, cost_of_ATK, MP, MP_max, dam, B_HP, buff, turn, select_ability):
    '''This function will be called if the user wants to use a special attack. They enter the letter for what attack they
want to use and if they have the right amount of MP, that characters current MP will decrease by that amount, and if they
don't have anough then they won't be able to perform that special attack'''
    choice = True
    while choice == True:
        print("MP = {}/{}".format(MP, MP_max))
        for letter, name, type, cost in zip(letter_of_ATK, name_of_ATK, type_of_ATK, cost_of_ATK):
            print("\n{}, {}, {}, {}\n".format(letter, name, type, cost))
        attack = input('''Please enter the letter for what attack you want to use or press enter
without typing anything to return to the previous screen ''').upper()
        if attack == '':
            choice = False
        elif attack in letter_of_ATK:
            pick = letter_of_ATK.index(attack)
            name = name_of_ATK[pick]
            result = type_of_ATK[pick]
            required_cost = cost_of_ATK[pick]
            if MP >= required_cost:
                if result == ATK:   # a attack that lands once if it connects
                    print("Used {}".format(name))
                    MP -= required_cost
                    connect = random.randint(1,3)
                    if connect == 1 or connect == 2:
                        damage_1 = dam[pick + 1][0]
                        damage_2 = dam[pick + 1][1]
                        damage_dealt = random.randint(damage_1, damage_2)
                        print("Hit")
                        if buff == True:
                            boosted_damage = damage_dealt * 1.50
                            boosted_damage = int(boosted_damage)
                            B_HP -= boosted_damage
                            print("You attack was buffed")
                            print("\nYou dealt {} damage\n".format(boosted_damage))
                            print("MP = {}/{}".format(MP, MP_max))
                            choice = False
                            turn = False
                            buff = False
                            select_ability = False
                        elif buff == False:
                            B_HP -= damage_dealt
                            print("\nyou dealt {} damage\n".format(damage_dealt))
                            print("MP = {}/{}".format(MP, MP_max))
                            choice = False
                            turn = False
                            select_ability = False
                            
                    else:
                        print('miss')
                        print("MP = {}/{}".format(MP, MP_max))
                        choice = False
                        turn = False
                        buff = False
                        select_ability = False
                        
                elif result == M_ATK:   # Attack that has a chance to land multible times
                    print("Used {}".format(name))
                    MP -= required_cost
                    connect = random.randint(1,3)
                    if connect == 1 or connect == 2:
                        damage_1 = dam[pick + 1][0]
                        damage_2 = dam[pick + 1][1]
                        hits = random.randint(1,5)
                        damage_dealt = random.randint(damage_1, damage_2) * hits
                        if buff == True:
                            boosted_damage = damage_dealt * 1.50
                            boosted_damage = int(boosted_damage)
                            print('Hit')
                            print("You attack was buffed")
                            print('\nYou attack landed {} times\n'.format(hits))
                            B_HP -= boosted_damage
                            print("You dealt {} damage".format(boosted_damage))
                            print("MP = {}/{}".format(MP, MP_max))
                            choice = False
                            turn = False
                            buff = False
                            select_ability = False
                        elif buff == False:
                            print('Hit')
                            print('\nYou attack landed {} times\n'.format(hits))
                            B_HP -= damage_dealt
                            print("You dealt {} damage".format(damage_dealt))
                            print("MP = {}/{}".format(MP, MP_max))
                            choice = False
                            turn = False
                            select_ability = False
                        
                    else:
                        print('miss')
                        print("MP = {}/{}".format(MP, MP_max))
                        choice = False
                        turn = False
                        buff = False
                        select_ability = False
                        
                elif result == BUFF:
                    if buff == False:
                        print("Used {}".format(name))
                        buff = True
                        choice = False
                        turn = False
                        print("Buffed and ready")
                        MP -= required_cost
                        print("MP = {}/{}".format(MP, MP_max))
                    elif buff == True:
                        print("Already buffed")
                elif MP < required_cost:
                    print("Not enough MP")

            elif MP < required_cost:
                print("\nnot enough MP\n")
                time.sleep(1.5)
        else:
            print("\nThat wasn't a option\n")
                
                                    
    return B_HP, MP, turn, buff, select_ability

def heal_ability(paste_man_HP, brusher_HP, mouth_washer_HP, MP, MP_max, turn, heal_abilities, healing_names, healing_types, healing_costs, select_ability):
    '''This function is if the dcharacter wants to use a special that heals 1 or all characters.'''
    heal_char = True
    while heal_char == True:
        print("MP = {}/{}".format(MP,MP_max))
        for letter, name, type_of_healing, cost in zip(heal_abilities, healing_names, healing_types, healing_costs):
            print("\n{}, {}, {}, {}\n".format(letter, name, type_of_healing, cost))
        heal = input('''Enter the letter for what healing ability you want to use or press enter
without typing anything to return to before ''').upper()
        if heal == '':
            heal_char = False
        elif heal in heal_abilities:
            pick = heal_abilities.index(heal)
            result = healing_types[pick]
            name = healing_names[pick]
            required_cost = healing_costs[pick]
            if MP >= required_cost:
                if result == HEAL:  # A ability that heals 1 character by 75HP
                    select = True
                    while select == True:
                        print("'A', paste man HP = {}/475".format(paste_man_HP))
                        print("'B', brusher HP = {}/410".format(brusher_HP))
                        print("'C', mouth washer HP = {}/390".format(mouth_washer_HP))
                        select_char = input("Please select what character you want to heal or press enter without typing anything to return to before ").upper()
                        if select_char == '':
                            select = False
                        elif select_char == 'A':
                            if paste_man_HP > 0 and paste_man_HP < 475:
                                print("Used {}".format(name))
                                paste_man_HP += 75
                                if paste_man_HP > 475:
                                    paste_man_HP = 475
                                    print("\npaste man HP = {}/475\n".format(paste_man_HP))
                                    turn = False
                                    select = False
                                    heal_char = False
                                    select_ability = False
                                    MP -= required_cost
                                    print("\n==----Healed----==\n")
                                    print("MP = {}/{}".format(MP, MP_max))
                                    time.sleep(1.5)
                                else:
                                    print("\npaste man HP = {}/475\n".format(paste_man_HP))
                                    turn = False
                                    select = False
                                    heal_char = False
                                    select_ability = False
                                    MP -= required_cost
                                    print("\n==----Healed----==\n")
                                    print("MP = {}/{}".format(MP, MP_max))
                                    time.sleep(1.5)
                            elif paste_man_HP == 475:
                                print("\nAlready at max HP\n")
                                
                            elif paste_man_HP == 0:
                                print("\nPaste man is unconcious\n")
                        elif select_char == 'B':
                            if brusher_HP > 0 and brusher_HP < 410:
                                print("Used {}".format(name))
                                brusher_HP += 75
                                if brusher_HP > 410:
                                    brusher_HP = 410
                                    print("\nbrusher HP = {}/410\n".format(brusher_HP))
                                    turn = False
                                    select = False
                                    heal_char = False
                                    select_ability = False
                                    MP -= required_cost
                                    print("\n==----Healed----==\n")
                                    print("MP = {}/{}".format(MP, MP_max))
                                    time.sleep(1.5)
                                else:
                                    print("\nbrusher HP = {}/410\n".format(brusher_HP))
                                    turn = False
                                    select = False
                                    heal_char = False
                                    select_ability = False
                                    MP -= required_cost
                                    print("\n==----Healed----==\n")
                                    print("MP = {}/{}".format(MP, MP_max))
                                    time.sleep(1.5)
                            elif brusher_HP == 410:
                                print("\nAlready at max HP\n")     
                            elif brusher_HP == 0:
                                print("\nbrusher is unconcious\n")
                                
                        elif select_char == 'C':
                            if mouth_washer_HP > 0 and mouth_washer_HP < 390:
                                print("Used {}".format(name))
                                mouth_washer_HP += 75
                                if mouth_washer_HP > 390:
                                    mouth_washer_HP = 390
                                    print("\nmouth washer HP = {}/390\n".format(mouth_washer_HP))
                                    turn = False
                                    select = False
                                    heal_char = False
                                    select_ability = False
                                    MP -= required_cost
                                    print("\n==----Healed----==\n")
                                    print("MP = {}/{}".format(MP, MP_max))
                                    time.sleep(1.5)
                                else:
                                    print("\nmouth washer HP = {}/410\n".format(mouth_washer_HP))
                                    turn = False
                                    select = False
                                    heal_char = False
                                    select_ability = False
                                    MP -= required_cost
                                    print("\n==----Healed----==\n")
                                    print("MP = {}/{}".format(MP, MP_max))
                                    time.sleep(1.5)
                            elif mouth_washer_HP == 390:
                                print("\nAlready at max HP\n")
                            elif mouth_washer_HP == 0:
                                print("\nMouth washer is unconcious\n")
                        else:
                            print("That wasn't a option")

                elif result == ALL_HEAL:  # A ability that heals all character by 75HP (provided that character is consious)
                    heal_paste_man = True
                    while heal_paste_man == True:
                        if paste_man_HP > 0:
                            paste_man_HP += 75
                            heal_paste_man = False
                            
                        elif paste_man_HP == 0:
                            print("Paste man is unconcious")
                            heal_paste_man = False

                    heal_brusher = True
                    while heal_brusher == True:
                        if brusher_HP > 0:
                            brusher_HP += 75
                            heal_brusher = False
                             
                        elif brusher_HP == 0:
                            print("Brusher is unconcious")
                            heal_brusher = False
                        
                    heal_mouth_washer = True
                    while heal_mouth_washer == True:
                        if mouth_washer_HP > 0:
                            mouth_washer_HP += 75
                            heal_mouth_washer = False

                        elif mouth_washer_HP == 0:
                            print("mouth washer is unconcious")
                            heal_mouth_washer = False


                    if paste_man_HP > 475:
                        paste_man_HP = 475
                        print("\nPaste man HP = {}/475\n".format(paste_man_HP))
                    else:
                        print("\nPaste man HP = {}/475\n".format(paste_man_HP))

                    
                    if brusher_HP > 410:
                        brusher_HP = 410
                        print("\nbrusher HP = {}/410\n".format(brusher_HP))
                    else:
                         print("\nbrusher HP = {}/410\n".format(brusher_HP))

                    if mouth_washer_HP > 390:
                        mouth_washer_HP = 390
                        print("\nMouth washer HP = {}/390\n".format(mouth_washer_HP))
                    else:
                        print("\nMouth washer HP = {}/390\n".format(mouth_washer_HP))
                        
                    print("\n==----All characters healed----==\n")   
                    MP -= required_cost
                    print("MP = {}/{}".format(MP, MP_max))
                    turn = False
                    heal_char = False
                    select_ability = False


                elif result == REVIVAL: # A ability that revives a fallen character with 200HP
                    select_char = True
                    while select_char == True:
                        print("'A', paste man HP = {}/475".format(paste_man_HP))
                        print("'B', brusher HP = {}/410".format(brusher_HP))
                        character = input('''Enter the letter for what character you want to revive, or press enter
without typing anything to return to the previous screen (note: a character has to have 0 HP to be revived) ''').upper()
                        if character == '':
                            select_char = False
                        elif character == 'A':
                            if paste_man_HP == 0:
                                paste_man_HP += 200
                                print("Paste man revived")
                                print("Paste man HP = {}/475".format(paste_man_HP))
                                MP -= required_cost
                                print("\n==----Revived----==\n")
                                print("MP = {}/{}".format(MP, MP_max))
                                time.sleep(1.5)
                                select_char = False
                                turn = False
                                select_ability = False
                                heal_char = False
                            elif paste_man_HP > 0:
                                print("Paste man is already concious")
                        elif character == 'B':
                            if brusher_HP == 0:
                                brusher_HP += 200
                                print("Brusher revived")
                                print("Brusher HP = {}/410".format(brusher_HP))
                                MP -= required_cost
                                print("\n==----Revived----==\n")
                                print("MP = {}/{}".format(MP, MP_max))
                                time.sleep(1.5)
                                select_char = False
                                turn = False
                                select_ability = False
                                heal_char = False
                            elif brusher_HP > 0:
                                print("Brusher is already concious")
                        else:
                            print("That wasn't an option")
                
            elif MP < required_cost:
                print("Not enough MP")
                time.sleep(1.5)
        else:
            print("That wasn't an option")

    return paste_man_HP, brusher_HP, mouth_washer_HP, MP, turn, select_ability

def power_attacks(boss_HP, STR, STR_max, turn, letter_of_ATK, name_of_ATK, type_of_ATK, STR_required, dam):
    choice = True
    while choice == True:
        print("STR = {}/{}".format(STR, STR_max))
        for letter, name, ATK_type, STR_cost in zip(letter_of_ATK, name_of_ATK, type_of_ATK, STR_required):
            print("\n{}, {}, {}, {}\n".format(letter, name, ATK_type, STR_cost))
        attack = input('''Please enter the letter for what attack you want to use or press enter
without typing anything to return to the previous screen ''').upper()
        if attack == '':
            choice = False
        elif attack in letter_of_ATK:
            pick = letter_of_ATK.index(attack)
            name = name_of_ATK[pick]
            result = type_of_ATK[pick]
            STR_cost = STR_required[pick]
            if STR >= STR_cost:
                print("used {}".format(name))
                if result == ATK:   # a attack that lands once if it connects
                    STR -= STR_cost
                    connect = random.randint(1,4)
                    if connect == 1 or connect == 2 or connect == 3:
                        damage_1 = dam[pick + 1][0]
                        damage_2 = dam[pick + 1][1]
                        damage_dealt = random.randint(damage_1, damage_2)
                        print("Hit")
                        boss_HP -= damage_dealt
                        print("\nYou dealt {} damage".format(damage_dealt))
                        print("STR = {}/{}\n".format(STR, STR_max))
                        choice = False
                        turn = False
                            
                    else:
                        print('miss')
                        print("STR = {}/{}".format(STR, STR_max))
                        choice = False
                        turn = False
                        
                elif result == ULTIMATE:    # A characters ultimate attack that deals alot of damage and always lands
                    STR -= STR_cost
                    damage_1 = dam[pick + 1][0]
                    damage_2 = dam[pick + 1][1]
                    damage_dealt = random.randint(damage_1, damage_2)
                    print("Hit")
                    boss_HP -= damage_dealt
                    print("\nYou used your strongest attack and dealt {} damage".format(damage_dealt))
                    print("STR = {}/{}\n".format(STR, STR_max))
                    choice = False
                    turn = False

                elif result == M_ATK:   # A attack that has a chance to land multible times
                    STR -= STR_cost
                    connect = random.randint(1,4)
                    if connect == 1 or connect == 2 or connect == 3:
                        damage_1 = dam[pick + 1][0]
                        damage_2 = dam[pick + 1][1]
                        hits = random.randint(1,3)
                        damage_dealt = random.randint(damage_1, damage_2) * hits
                        print("Hit")
                        print("\nYour attack landed {} times\n".format(hits))
                        boss_HP -= damage_dealt
                        print("\nYou dealt {} damage\n".format(damage_dealt))
                        print("STR = {}/{}".format(STR, STR_max))
                        choice = False
                        turn = False
                            
                    else:
                        print('miss')
                        print("STR = {}/{}".format(STR, STR_max))
                        choice = False
                        turn = False

                elif result == M_ULTIMATE:  # A characters Ultimate attack that can land multible times and always hits
                    STR -= STR_cost
                    damage_1 = dam[pick + 1][0]
                    damage_2 = dam[pick + 1][1]
                    hits = random.randint(1,3)
                    damage_dealt = random.randint(damage_1, damage_2) * hits
                    print("Hit")
                    print("Your attack landed {} times".format(hits))
                    boss_HP -= damage_dealt
                    print("\nYou used your strongest attack and dealt {} damage\n".format(damage_dealt))
                    print("STR = {}/{}".format(STR, STR_max))
                    choice = False
                    turn = False

            elif STR < STR_cost:
                print("Not enough STR")
                time.sleep(1.5)
            
        else:
            print("\nThat wasn't an option\n")
    return boss_HP, STR, turn

def tutorial():
    '''This function is called if the user needs help with understanding how certain actions work'''
    print('''
    'H'  for HP
    'N'  normal attack
    'S'  for STR
    'P'  for physical attack
    'M'  for MP
    'SP'  for special ability
    'B'  for block
    'I'  to use a item
    'T'  for turn order
    'G'  for what the goal is''')
    help_me = True
    while help_me == True:
        information = input('''Enter a letter too see a tutorial for how that action works incase you don't understand,
or press enter without typing anything when you're done ''').upper()
        if information == '':
            help_me = False
        elif information == 'H':
            print('''\nEach character has a set amount of HP, which is that characters health. If the enemies
attack lands the character will lose HP. If a character runs out of HP that character will be unconcious and
won't be able to do anything unless they are revived\n''')
        elif information == 'N':
            print('''\nEnter 'A' on the previous screen to have your character use a normal attack. Normal
attacks do very small damage but have a high chance of landing a hit on the enemy and if it lands the
character will gain 1 STR\n''')
        elif information == 'S':
            print('''\nSTR is a special type of point each character has. They have a limit to how much
they can have and start with 3 and gain 1 at the start of their turn (with the exception of their starting
turn) if that character is concious.\n''')
        elif information == 'P':
            print('''\nEntering 'P' on the previous screen will have a character use their power attacks.
power attacks do the most damage out of all attacks and require STR to use. When you enter P a list of
that characters power attacks will appear. The letter at the start of each line is what you enter to
use it, the text is the name and what it'll do, and the number at the end is how much STR you need too use
it. If you don't have the right amount of STR you can't use it. Using a power attack will use that amount
of STR. Each character also has a ultimate attack listed in there power attacks. These require the character
to have the most STR they can have but deals alot of damage and will hit always hit no matter what.\n''')
        elif information == 'M':
            print('''\nMP is used for using special abilities, which are attacks that don't deal as much damage
as physical attacks, but you have alot more MP so they can be used much more. Though make sure your careful since
unlike HP or STR the only way to recover MP is by using A couple items, so make sure your conservative with it\n''')
        elif information == 'SP':
            print('''\nEntering 'S' on the previous screen will let you use a special attack. These cost a set
number of MP to use and will deplete that amount of MP upon use. The letter at the start is what to enter, the
text is the name and what it does, and the number at the end is how much it costs. If you don't have the right
amount of MP the attack won't work. Also just real quick, the third character Mouth washer has 2 options for
special abilities. Attack and healing. After entering S on mouth washers turn you can either enter A to use a
attacking special, or H to use a healing special which can heal or revive all fallen character.\n''')
        elif information == 'B':
            print('''\nEntering 'B' on the previous screen will have your character block, if a character blocks
they won't be able to attacks, or use an item, but if a character is blocking it'll last until their next turn,
and if they get attacked they take half the damage. Blocking is very useful if your character is running low
on HP\n''')
        elif information == 'I':
            print('''\nEntering 'I' on the previous screen will give you the option to use a item on one or all
characters. Enter the letter next to each characters current HP, MP and STR to use an item on that character,
or F to use an item that'll affect all characters. Items can do things like heal characters, revive characters
and restore MP. Enter the letter next to each item to use that item. The text between shows the name and what that
item does and the number at the end is how much of that item you have. If you use an item that amount will decrease
by 1 and if you don't have the required amount then you can't use that item. Theres no way to get an item back after
using it so make sure you use it when your sure you want to\n''')
        elif information == 'T':
            print('''\nEach character will go in turns. First it's paste man, then brusher, then Mouth washer and
finally the enemy. After that it starts over. You can select what the 3 characters do, but the enemy chooses a attack
automaticly. You can either use all 3 characters by yourself or have friends play with you, each choosing what to do\n''')
        elif information == 'G':
            print('''\nThe main goal of the game is too try and defeat a randomly selected enemy. Do this by attacking
it until it's HP reaches 0. If you do that then you win. But if all 3 characters HP reaches 0 then it's game over and
you lose. If you win you can choose to fight another randomly selected enemy, or just end the game there. Try to win
as many battles as you can\n''')
        else:
            print("\nThat wasn't an option\n")

def  select_enemy(boss, boss_HP, boss_attacks, boss_damage, boss_types):
    boss = random.choice(bosses)
    if boss == 'Bacteria':
        boss_HP = bacteria_HP
        boss_attacks = bacteria_attacks
        boss_damage = bacteria_damage
        boss_types = bacteria_types
    elif boss == 'Infected tooth':
        boss_HP = infected_tooth_HP
        boss_attacks = infected_tooth_attacks
        boss_damage = infected_tooth_damage
        boss_types = infected_tooth_types
    elif boss == 'germ pile':
        boss_HP = germ_pile_HP
        boss_attacks = germ_pile_attacks
        boss_damage = germ_pile_damage
        boss_types = germ_pile_types
    elif boss == 'candy teeth':
        boss_HP = candy_teeth_HP
        boss_attacks = candy_teeth_attacks
        boss_damage = candy_teeth_damage
        boss_types = candy_teeth_types

    return  boss, boss_HP, boss_attacks, boss_damage, boss_types
        
def turn_order(paste_man_MP, paste_man_HP, paste_man_STR, brusher_HP, brusher_MP, brusher_STR, mouth_washer_HP, mouth_washer_MP, mouth_washer_STR, single_item_letters, single_items_carried, single_item_types, single_item_amounts, all_item_letters, all_items_carried, all_item_types, all_item_amounts, victories):
    gain = False
    boss = ''
    boss_HP = 0
    boss_attacks = []
    boss_damage = {}
    boss_types = []
    (boss, boss_HP, boss_attacks, boss_damage, boss_types) = select_enemy(boss, boss_HP, boss_attacks, boss_damage, boss_types)
    color.write("\nYour fighting {}\n".format(boss), "COMMENT")
    boss_max = boss_HP
    color.write("==----{} HP = {}/{}----==\n".format(boss, boss_HP, boss_max), "COMMENT")
    print("Be ready to do some cleaning\n")
    # Varialbe used to end a turn when a item is used
    end_turn = False
    # paste man variables used
    paste_man_turn = False
    paste_man = 'Paste man'
    none = False
    none_2 = False
    paste_man_block = False
    # Brusher variables to use
    brusher_turn = False
    brusher_buff = False
    brusher = 'Brusher'
    brusher_block = False
    # Mouth washer variables used
    mouth_washer_turn = False
    mouth_washer_block = False
    mouth_washer = 'Mouth washer'
    mouth_washer_block = False
    # enemy variables
    enemy_turn = False
    boss_buff = False
    play = True
    while play == True:
        if paste_man_HP > 0:
            if paste_man_STR < 8:
                if gain == True:
                    paste_man_STR += 1
                print("\nIt's paste man's turn\n")
                paste_man_turn = True
            elif paste_man_STR == 8:
                print("\nIt's paste man's turn\n")
                paste_man_turn = True
        elif paste_man_HP == 0:
            print("\nPaste man is unconsious\n")
        while paste_man_turn == True:
            print("HP = {}/475".format(paste_man_HP))
            print("MP = {}/120".format(paste_man_MP))
            print("STR = {}/8".format(paste_man_STR))
            print(actions)
            paste_man_block = False
            action = input("Select what action above you want to perform ").upper()
            if action == 'A':   # the user wants to use a normal attack
                print('You used a normal attack')
                (boss_HP, none, paste_man_STR) = normal_attack(boss_HP, paste_man_normal_attack, none, paste_man_STR, paste_man_STR_max)
                paste_man_turn = False

            elif action == 'P': # The user wants to use a physical attack
                (boss_HP, paste_man_STR, paste_man_turn) = power_attacks(boss_HP, paste_man_STR, paste_man_STR_max, paste_man_turn, paste_man_STR_letters, paste_man_STR_names, paste_man_STR_types, paste_man_STR_required, paste_man_STR_damage)
                
            elif action == 'S': # the user wants to use a special attack
                (boss_HP, paste_man_MP, paste_man_turn, none, none_2) = special_attack(paste_man_letters, paste_man_names, paste_man_types, paste_man_costs, paste_man_MP, paste_man_MP_max, paste_man_damage, boss_HP, none, paste_man_turn, none_2)                

            elif action == 'B': # the user wants to block
                print('You chose to block')
                paste_man_block = True
                paste_man_turn = False

            elif action == 'I': # the user wants to use a item
                select_char = True
                while select_char == True:
                    print("\n'A', paste man HP = {}/475, MP = {}/120, STR = {}/8".format(paste_man_HP, paste_man_MP, paste_man_STR))
                    print("'B', brusher HP = {}/410, MP = {}/115, STR = {}/10".format(brusher_HP, brusher_MP, brusher_STR))
                    print("'C', mouth washer HP = {}/390, MP = {}/145, STR = {}/6".format(mouth_washer_HP, mouth_washer_MP, mouth_washer_STR))
                    print("'F', Use a item that effects all characters")
                    use_on = input('''Enter the letter for who you want to use a item on, enter F to use
a item that effects all, or press enter without typing anything
to return to the previous screen ''').upper()
                    if use_on == '':
                        select_char = False
                    elif use_on == 'A' or use_on == 'B' or use_on == 'C':   # Thue user wants to use an item on 1 of the 3 characters
                        for letter, name_of_item, type_of_item, amount in zip(single_item_letters, single_items_carried, single_item_types, single_item_amounts):
                            print("\n{}, {}, {}, {}\n".format(letter, name_of_item, type_of_item, amount))
                        item = input('''Please enter the letter for what item you want to use or press enter
without typing anything to return to the action select screen ''').upper()
                        if item == '':
                            select_char = False
                        elif item in single_item_letters:
                            pick = single_item_letters.index(item)
                            item_name = single_items_carried[pick]
                            type_of_item = single_item_types[pick]
                            if single_item_amounts[pick] > 0:
                                if use_on == 'A':
                                    (paste_man_HP, paste_man_MP, paste_man_STR, end_turn) = single_select_item(paste_man_HP, paste_man_HP_max, paste_man_MP, paste_man_MP_max, paste_man_STR, paste_man_STR_max, end_turn, paste_man, type_of_item)
                                elif use_on == 'B':
                                    (brusher_HP, brusher_MP, brusher_STR, end_turn) = single_select_item(brusher_HP, brusher_HP_max, brusher_MP, brusher_MP_max, brusher_STR, brusher_STR_max, end_turn, brusher, type_of_item)
                                elif use_on == 'C':
                                     (mouth_washer_HP, mouth_washer_MP, mouth_washer_STR, end_turn) = single_select_item(mouth_washer_HP, mouth_washer_HP_max, mouth_washer_MP, mouth_washer_MP_max, mouth_washer_STR, mouth_washer_STR_max, end_turn, mouth_washer, type_of_item)

                            elif single_item_amounts[pick] == 0:
                                print("\nDon't have any of this item")

                        else:
                            print("That's not an item")

                        if end_turn == True:
                            single_item_amounts[pick] -= 1
                            end_turn = False
                            paste_man_turn = False
                            select_char = False
                        elif end_turn == False:
                            print("Please select anothger item")
                    
                    elif use_on == 'F': #The user wants to use a item that affects all character
                        for letter, name_of_item, type_of_item, amount in zip(all_item_letters, all_items_carried, all_item_types, all_item_amounts):
                            print("\n{}, {}, {}, {}\n".format(letter, name_of_item, type_of_item, amount))
                        item = input('''Please enter the letter for what item you want to use,
or press enter without typing anything to return to the action select screen ''').upper()
                        if item == '':
                            select_char = False
                        elif item in all_item_letters:
                            pick = all_item_letters.index(item)
                            item_name = all_items_carried[pick]
                            type_of_item = all_item_types[pick]
                            if all_item_amounts[pick] > 0:
                                (paste_man_HP, paste_man_MP, brusher_HP, brusher_MP, mouth_washer_HP, mouth_washer_MP) = all_item(paste_man_HP, paste_man_MP, brusher_HP, brusher_MP, mouth_washer_HP, mouth_washer_MP, type_of_item)
                                all_item_amounts[pick] -= 1
                                select_char = False
                                paste_man_turn = False
                            elif all_item_amounts[pick] == 0:
                                print("\nNot enough of this item, please select somthing else")
                        else:
                            print("That wasn't an option")

                    else:
                        print("That wasn't a option")

            elif action == 'H': # The user wants help
                tutorial()
                
            else:
                print("That wasn't a option")

        if boss_HP > 0:
            color.write("\n==----{} HP = {}/{}----==\n".format(boss, boss_HP, boss_max), "COMMENT")
            time.sleep(1.5)
            if brusher_HP == 0:
                print("\nBrusher is unconcious\n")
            elif brusher_HP > 0:
                brusher_turn = True
                if brusher_STR < 10:
                    if gain == True:
                        brusher_STR += 1
                    print("\nIt's brusher's turn\n")
                elif brusher_STR == 10:
                    print("\nIt's brusher's turn\n")
        elif boss_HP <= 0:
            print("You won")
            print("\nRemember to always use enough toothpaste to keep those teeth clean\n")
            time.sleep(2)
            victories += 1
            play = False
            play_again(paste_man_MP, paste_man_HP, paste_man_STR, brusher_HP, brusher_MP, brusher_STR, mouth_washer_HP, mouth_washer_MP, mouth_washer_STR, single_item_letters, single_items_carried, single_item_types, single_item_amounts, all_item_letters, all_items_carried, all_item_types, all_item_amounts, victories, grade)
            sys.exit()

            
        while brusher_turn == True: # brusher turn
            brusher_block = False
            print("HP = {}/410".format(brusher_HP))
            print("MP = {}/115".format(brusher_MP))
            print("STR = {}/10".format(brusher_STR))
            print(actions)
            action = input("Select what action above you want to perform ").upper()
            if action == 'A':   # The user wants to use a normal attack
                print('You used a normal attack')
                (boss_HP, brusher_buff, brusher_STR) = normal_attack(boss_HP, brusher_normal_attack, brusher_buff, brusher_STR, brusher_STR_max)
                brusher_turn = False

            elif action == 'P':
                (boss_HP, brusher_STR, brusher_turn) = power_attacks(boss_HP, brusher_STR, brusher_STR_max, brusher_turn, brusher_STR_letters, brusher_STR_names, brusher_STR_types, brusher_STR_required, brusher_STR_damage)

            elif action == 'S': # The user wants to use a special attack
                (boss_HP, brusher_MP, brusher_turn, brusher_buff, none_2) = special_attack(brusher_special_attacks, brusher_special_attack_names, brusher_types, brusher_costs, brusher_MP, brusher_MP_max, brusher_damage, boss_HP, brusher_buff, brusher_turn, none_2)

            elif action == 'B': #The user wants to block
                print("you chose to block")
                brusher_block = True
                brusher_turn = False
                
            elif action == 'I': # The user wants to use a item
                select_char = True
                while select_char == True:
                    print("\n'A', paste man HP = {}/475, MP = {}/120, STR = {}/8".format(paste_man_HP, paste_man_MP, paste_man_STR))
                    print("'B', brusher HP = {}/410, MP = {}/115, STR = {}/10".format(brusher_HP, brusher_MP, brusher_STR))
                    print("'C', mouth washer HP = {}/390, MP = {}/145, STR = {}/6".format(mouth_washer_HP, mouth_washer_MP, mouth_washer_STR))
                    print("'F', Use a item that effects all characters")
                    use_on = input('''Enter the letter for who you want to use a item on, enter F to use
a item that effects all, or press enter without typing anything
to return to the previous screen ''').upper()
                    if use_on == '':
                        select_char = False
                    elif use_on == 'A' or use_on == 'B' or use_on == 'C':
                        for letter, name_of_item, type_of_item, amount in zip(single_item_letters, single_items_carried, single_item_types, single_item_amounts):
                            print("\n{}, {}, {}, {}\n".format(letter, name_of_item, type_of_item, amount))
                        item = input('''Please enter the letter for what item you want to use,
or press enter without typing anything to return to the action select screen ''').upper()
                        if item == '':
                            select_char = False
                        elif item in single_item_letters:
                            pick = single_item_letters.index(item)
                            item_name = single_items_carried[pick]
                            type_of_item = single_item_types[pick]
                            if single_item_amounts[pick] > 0:
                                if use_on == 'A':
                                    (paste_man_HP, paste_man_MP, paste_man_STR, end_turn) = single_select_item(paste_man_HP, paste_man_HP_max, paste_man_MP, paste_man_MP_max, paste_man_STR, paste_man_STR_max, end_turn, paste_man, type_of_item)
                                elif use_on == 'B':
                                    (brusher_HP, brusher_MP, brusher_STR, end_turn) = single_select_item(brusher_HP, brusher_HP_max, brusher_MP, brusher_MP_max, brusher_STR, brusher_STR_max, end_turn, brusher, type_of_item)
                                elif use_on == 'C':
                                     (mouth_washer_HP, mouth_washer_MP, mouth_washer_STR, end_turn) = single_select_item(mouth_washer_HP, mouth_washer_HP_max, mouth_washer_MP, mouth_washer_MP_max, mouth_washer_STR, mouth_washer_STR_max, end_turn, mouth_washer, type_of_item)

                            elif single_item_amounts[pick] == 0:
                                print("\nDon't have any of this item")
                            else:
                                print("TRY")

                        if end_turn == True:
                            single_item_amounts[pick] -= 1
                            end_turn = False
                            brusher_turn = False
                            select_char = False
                        elif end_turn == False:
                            print("Please select anothger item")
                    elif use_on == 'F': #The user wants to use a item that effects all character
                        for letter, name_of_item, type_of_item, amount in zip(all_item_letters, all_items_carried, all_item_types, all_item_amounts):
                            print("\n{}, {}, {}, {}\n".format(letter, name_of_item, type_of_item, amount))
                        item = input('''Please enter the letter for what item you want to use,
or press enter without typing anything to return to the action select screen ''').upper()
                        if item == '':
                            select_char = False
                        elif item in all_item_letters:
                            pick = all_item_letters.index(item)
                            item_name = all_items_carried[pick]
                            type_of_item = all_item_types[pick]
                            if all_item_amounts[pick] > 0:
                                (paste_man_HP, paste_man_MP, brusher_HP, brusher_MP, mouth_washer_HP, mouth_washer_MP) = all_item(paste_man_HP, paste_man_MP, brusher_HP, brusher_MP, mouth_washer_HP, mouth_washer_MP, type_of_item)
                                all_item_amounts[pick] -= 1
                                select_char = False
                                brusher_turn = False
                            elif all_item_amounts[pick] == 0:
                                print("\nNot enough of this item, please select somthing else")

                    else:
                        print("That wasn't a option")  

            else:
                print("That wasn't a option")

        if boss_HP > 0:
            color.write("\n==----{} HP = {}/{}----==\n".format(boss, boss_HP, boss_max), "COMMENT")
            time.sleep(1.5)
            if mouth_washer_HP == 0:
                print("\nmouth washer is unconcious\n")
                enemy_turn = True
            else:
                if mouth_washer_STR < 6:
                    if gain == True:
                        mouth_washer_STR += 1
                    print("\nIt's Mouth washer's turn\n")
                elif mouth_washer_STR == 6:
                    print("\nIt's Mouth washer's turn\n")
                mouth_washer_turn = True
        elif boss_HP <= 0:
            print("You won")
            print("\nAlways brush your teeth atleast twice a day kids\n")
            time.sleep(2)
            victories += 1
            play = False
            play_again(paste_man_MP, paste_man_HP, paste_man_STR, brusher_HP, brusher_MP, brusher_STR, mouth_washer_HP, mouth_washer_MP, mouth_washer_STR, single_item_letters, single_items_carried, single_item_types, single_item_amounts, all_item_letters, all_items_carried, all_item_types, all_item_amounts, victories, grade)
            sys.exit()

        while mouth_washer_turn == True:    # Mouth washer's turn
            mouth_washer_block = False
            print("HP = {}/390".format(mouth_washer_HP))
            print("MP = {}/145".format(mouth_washer_MP))
            print("STR = {}/6".format(mouth_washer_STR))
            print(actions_2)
            action = input("Please enter the letter for what action you want to perform ").upper()
            if action == 'A':   # The user wants to use a normal attack
                print('You used a normal attack')
                (boss_HP, none, mouth_washer_STR) = normal_attack(boss_HP, mouth_washer_normal_attack, none, mouth_washer_STR, mouth_washer_STR_max)
                mouth_washer_turn = False

            elif action == 'P':
                (boss_HP, mouth_washer_STR, mouth_washer_turn) = power_attacks(boss_HP, mouth_washer_STR, mouth_washer_STR_max, mouth_washer_turn, mouth_washer_STR_letters, mouth_washer_STR_names, mouth_washer_STR_types, mouth_washer_STR_required, mouth_washer_STR_damage)

            elif action == 'S': # The user wants to use a special attack
                select_ability = True
                while select_ability == True:
                    type_of_special = input('''\nEnter A to use a special ability that'll attack the enemy or H to use
a special that'll heal a character, or press enter without typing anything to return to before ''').upper()
                    if type_of_special == '':
                        select_ability = False
                    elif type_of_special == 'A':                        
                        (boss_HP, mouth_washer_MP, mouth_washer_turn, none, select_ability) = special_attack(mouth_washer_attacks, mouth_washer_special_attacks_names, mouth_washer_types, mouth_washer_costs, mouth_washer_MP, mouth_washer_MP_max, mouth_washer_damage, boss_HP, none, mouth_washer_turn, select_ability)
                    elif type_of_special == 'H':
                        (paste_man_HP, brusher_HP, mouth_washer_HP, mouth_washer_MP, mouth_washer_turn, select_ability) = heal_ability(paste_man_HP, brusher_HP, mouth_washer_HP, mouth_washer_MP, mouth_washer_MP_max, mouth_washer_turn, mouth_washer_healing_abilities, mouth_washer_healing_ability_names, mouth_washer_healing_types, mouth_washer_healing_costs, select_ability)

                    else:
                        print("That wasn't an option")

            elif action == 'B': #The user wants to block
                print("You chose to block")
                mouth_washer_block = True
                mouth_washer_turn = False
                
            elif action == 'I': # The user wants to use a item
                select_char = True
                while select_char == True:
                    print("\n'A', paste man HP = {}/475, MP = {}/120, STR = {}/8".format(paste_man_HP, paste_man_MP, paste_man_STR))
                    print("'B', brusher HP = {}/410, MP = {}/115, STR = {}/10".format(brusher_HP, brusher_MP, brusher_STR))
                    print("'C', mouth washer HP = {}/390, MP = {}/145, STR = {}/6".format(mouth_washer_HP, mouth_washer_MP, mouth_washer_STR))
                    print("'F', Use a item that effects all characters")
                    use_on = input('''Enter the letter for who you want to use a item on, enter F to use
a item that effects all, or press enter without typing anything
to return to the previous screen ''').upper()
                    if use_on == '':
                        select_char = False
                    elif use_on == 'A' or use_on == 'B' or use_on == 'C':
                        for letter, name_of_item, type_of_item, amount in zip(single_item_letters, single_items_carried, single_item_types, single_item_amounts):
                            print("\n{}, {}, {}, {}\n".format(letter, name_of_item, type_of_item, amount))
                        item = input('''Please enter the letter for what item you want to use,
or press enter without typing anything to return to the action select screen ''').upper()
                        if item == '':
                            select_char = False
                        elif item in single_item_letters:
                            pick = single_item_letters.index(item)
                            item_name = single_items_carried[pick]
                            type_of_item = single_item_types[pick]
                            if single_item_amounts[pick] > 0:
                                if use_on == 'A':
                                    (paste_man_HP, paste_man_MP, paste_man_STR, end_turn) = single_select_item(paste_man_HP, paste_man_HP_max, paste_man_MP, paste_man_MP_max, paste_man_STR, paste_man_STR_max, end_turn, paste_man, type_of_item)
                                elif use_on == 'B':
                                    (brusher_HP, brusher_MP, brusher_STR, end_turn) = single_select_item(brusher_HP, brusher_HP_max, brusher_MP, brusher_MP_max, brusher_STR, brusher_STR_max, end_turn, brusher, type_of_item)
                                elif use_on == 'C':
                                     (mouth_washer_HP, mouth_washer_MP, mouth_washer_STR, end_turn) = single_select_item(mouth_washer_HP, mouth_washer_HP_max, mouth_washer_MP, mouth_washer_MP_max, mouth_washer_STR, mouth_washer_STR_max, end_turn, mouth_washer, type_of_item)

                            elif single_item_amounts[pick] == 0:
                                print("\nDon't have any of this item")
                            else:
                                print("TRY")

                        if end_turn == True:
                            single_item_amounts[pick] -= 1
                            end_turn = False
                            mouth_washer_turn = False
                            select_char = False
                        elif end_turn == False:
                            print("Please select anothger item")
                                
                    elif use_on == 'F': #The user wants to use a item that effects all character
                        for letter, name_of_item, type_of_item, amount in zip(all_item_letters, all_items_carried, all_item_types, all_item_amounts):
                            print("\n{}, {}, {}, {}\n".format(letter, name_of_item, type_of_item, amount))
                        item = input('''Please enter the letter for what item you want to use,
or press enter without typing anything to return to the action select screen ''').upper()
                        if item == '':
                            select_char = False
                        elif item in all_item_letters:
                            pick = all_item_letters.index(item)
                            item_name = all_items_carried[pick]
                            type_of_item = all_item_types[pick]
                            if all_item_amounts[pick] > 0:
                                (paste_man_HP, paste_man_MP, brusher_HP, brusher_MP, mouth_washer_HP, mouth_washer_MP) = all_item(paste_man_HP, paste_man_MP, brusher_HP, brusher_MP, mouth_washer_HP, mouth_washer_MP, type_of_item)
                                all_item_amounts[pick] -= 1
                                select_char = False
                                mouth_washer_turn = False
                            elif all_item_amounts[pick] == 0:
                                print("\nNot enough of this item, please select somthing else")

                    else:
                        print("That wasn't a option")  

            else:
                print("That wasn't a option")
            

        if boss_HP > 0:
            color.write("\n==----{} HP = {}/{}----==\n".format(boss, boss_HP, boss_max), "COMMENT")
            time.sleep(1.5)
            color.write("\nIt's {}'s turn\n".format(boss), "COMMENT")
            enemy_turn = True
        elif boss_HP <= 0:
            print("You won")
            print("\nremember to use mouthwash to keep your mouth clean\n")
            time.sleep(2)
            victories += 1
            play = False
            play_again(paste_man_MP, paste_man_HP, paste_man_STR, brusher_HP, brusher_MP, brusher_STR, mouth_washer_HP, mouth_washer_MP, mouth_washer_STR, single_item_letters, single_items_carried, single_item_types, single_item_amounts, all_item_letters, all_items_carried, all_item_types, all_item_amounts, victories, grade)
            sys.exit()
                
        
        # Now it's the enemies turn
        while enemy_turn == True:
            target = random.choice(team)
            if target == 'paste man':
                if paste_man_HP > 0:
                    (paste_man_HP, enemy_turn, boss_buff) = enemy_attack(boss_attacks, boss_types, boss_damage, paste_man_HP, paste_man_HP_max, target, paste_man_block, enemy_turn, boss_buff)
                    choose_target = False
                else:
                    color.write("selecting attack\n", "COMMENT")
            elif target == 'brusher':
                if brusher_HP > 0:
                    (brusher_HP, enemy_turn, boss_buff) = enemy_attack(boss_attacks, boss_types, boss_damage, brusher_HP, brusher_HP_max, target, brusher_block, enemy_turn, boss_buff)
                    choose_target = False
                else:
                    color.write("selecting attack\n", "COMMENT")
            elif target == 'mouth washer':
                if mouth_washer_HP > 0:
                    (mouth_washer_HP, enemy_turn, boss_buff) = enemy_attack(boss_attacks, boss_types, boss_damage, mouth_washer_HP, mouth_washer_HP_max, target, mouth_washer_block, enemy_turn, boss_buff)
                else:
                    color.write("selecting attack\n", "COMMENT")
            if paste_man_HP == 0 and brusher_HP == 0 and mouth_washer_HP == 0:
                color.write("Game over you lost\n", "COMMENT")
                play = False
        gain = True


def grading(grade, victories):
    '''This function will be called after a game ends to give the user their grade based on how many fights they won before losing
or ending the game'''
    if victories < 5:
        grade = ("F  horrible dentist")
    elif victories >= 5 and victories <= 10:
        grade = ("E  bad dentist")
    elif victories >= 10 and victories <= 13:
        grade = ("D  starter dentist")
    elif victories >= 13 and victories <= 15:
        grade = ("C  Cadet dentist")
    elif victories >= 15 and victories <= 20:
        grade = ("B  good dentist")
    elif victories >= 20 and victories <= 25:
        grade = ("A  great dentist")
    elif victories >= 25:
        grade = ("S  master dentist")

    return grade

def play_again(paste_man_MP, paste_man_HP, paste_man_STR, brusher_HP, brusher_MP, brusher_STR, mouth_washer_HP, mouth_washer_MP, mouth_washer_STR, single_item_letters, single_items_carried, single_item_types, single_item_amounts, all_item_letters, all_items_carried, all_item_types, all_item_amounts, victories, grade):
    '''This function is called if the user wins. They can choose to fight again with there current HP, MP, STR and items carried over or end here. They will also be told how many fights they won, and will be given a grade
based on how many fights they won if they choose not to play again.'''
    choose = True
    colour = 'none'
    while choose == True:
        play_again = input('''\nCongradulations you won. Would you like to keep playing and fight another enemy, with
your current amount of items, HP, MP and STR. Or end here. Enter Y to fight again or
N to end here ''').upper()
        if play_again == 'Y':
            print("Ok then let's do it")
            choose = False
            turn_order(paste_man_MP, paste_man_HP, paste_man_STR, brusher_HP, brusher_MP, brusher_STR, mouth_washer_HP, mouth_washer_MP, mouth_washer_STR, single_item_letters, single_items_carried, single_item_types, single_item_amounts, all_item_letters, all_items_carried, all_item_types, all_item_amounts, victories)
        elif play_again == 'N':
            print("\nWell overall")
            print("You won {} fights".format(victories))    # Telling the user how many fights they won
            print("As for your grade (Please don't be offended if it's bad)")
            grade = grading(grade, victories)
            print("\n=---{}---=\n".format(grade))
            print("Well then thank you for playing and keep those teeth clean")
            choose = False

        else:
            print("That wasn't an option")


print("Note, any information relating to the enemy, such as it's current health, attacks is used and damage it dealt is printed in red\n")            
turn_order(paste_man_MP, paste_man_HP, paste_man_STR, brusher_HP, brusher_MP, brusher_STR, mouth_washer_HP, mouth_washer_MP, mouth_washer_STR, single_item_letters, single_items_carried, single_item_types, single_item_amounts, all_item_letters, all_items_carried, all_item_types, all_item_amounts, victories)

# This is used to print how many fights the user won, and give them a grade if they lose and get a game over.
print("\nOverall")
print("You won {} fights".format(victories))    # Telling the user how many fights they won
print("As for your grade (Please don't be offended if it's bad)")
grade = grading(grade, victories)
print("\n=---{}---=\n".format(grade))
print("Well then thank you for playing and remember to keep those teeth clean, no matter what")
