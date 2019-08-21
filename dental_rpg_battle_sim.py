# dental_rpg_battle_sim.py
# date: 1/07/2019
# Author: Benjamin Ameye
import random

# types of special attacks
ATK = 'Attack that lands once'
M_ATK = 'Multi hitting Attack'
BUFF = 'Next attack will deal a extra 50% damage (except physical attacks)'
HEAL = 'Heal 1 character by 75 HP'
ALL_HEAL = 'Heals all characters by 75HP'
REVIVAL = 'Revives 1 fallen character with 200HP'
ULTIMATE = 'The characters strongest attack'
M_ULTIMATE = 'The characters strongest attack (chance to land multible times)'


# item types
H = 'Heals 1 character by 75 HP' 
A_H = 'Heals all characters by 50 HP'
F_H =  'Fully heals 1 character' 
R = 'Restores all characters HP and SP' 
MP_R = 'Restores 1 characters MP by 25'
REV = 'Revives 1 character with 175 HP'
REV_F = 'Revives 1 character with max HP'
GAIN_STR = 'Gives a character 1 STR'

#The characters max HP, MP, STR and list of special attacks
# Paste man attacks, HP, STR and MP
paste_man_HP = 475
paste_man_HP_max = 475
paste_man_MP = 120
paste_man_MP_max = 120
paste_man_STR = 3
paste_man_STR_max = 5
paste_man_letters = ['A', 'B', 'C']
paste_man_names = ['Toothpaste squirt', 'Tooth pick clean', 'clean breathe']
paste_man_types = [ATK, ATK, M_ATK]
paste_man_costs = [9, 16, 19]
paste_man_damage = {1: [15, 20], 2: [30, 45], 3: [40, 45]}
paste_man_STR_letters = ['A', 'B', 'C', 'D']
paste_man_STR_names = ['Brush bow', 'Paste rain', 'freshness spray', 'pure paste']
paste_man_STR_types = [ATK, M_ATK, M_ATK, ULTIMATE]
paste_man_STR_required = [2, 2, 3, 5]
paste_man_STR_damage = {1: [25, 35], 2: [15, 20], 3: [30, 35], 4: [40, 50]}
paste_man_normal_attack = [5, 10]
# Brusher attacks, HP, STR and MP
brusher_HP = 0
brusher_HP_max = 410
brusher_MP = 115
brusher_MP_max = 115
brusher_STR = 2
brusher_STR_max = 8
brusher_special_attacks = ['A', 'B', 'C', 'D']
brusher_special_attack_names = ['Brush smack', 'Clean rinse', 'Ultimate scrub', 'Add toothpaste']
brusher_types = [ATK, M_ATK, ATK, BUFF]
brusher_costs = [10, 11, 20, 22]
brusher_damage = {1: [20, 25], 2: [20, 30], 3: [50,55]}
brusher_normal_attack = [10, 15]
brusher_STR_letters = ['A', 'B', 'C']
brusher_STR_names = ['Tooth brush rain', 'Cross brush', 'brush spear']
brusher_STR_types = [M_ATK, ATK, ULTIMATE]
brusher_STR_required = [3, 5, 8]
brusher_STR_damage = {1: [20, 30], 2: [30, 35], 3: [50, 60]}
# Mouth washer attacks, healing abilities, HP, STR and MP
mouth_washer_HP = 390
mouth_washer_HP_max = 390
mouth_washer_MP = 145
mouth_washer_MP_max = 145
mouth_washer_attacks = ['A', 'B', 'C', 'D']
mouth_washer_special_attacks_names = ['Dental floss whip', 'Mouthwash Blast']
mouth_washer_types = [M_ATK, ATK]
mouth_washer_damage = {1: [10, 15], 2: [35, 45]}
mouth_washer_costs = [8, 16, 21, 22]
mouth_washer_normal_attack = [5, 10]
mouth_washer_healing_abilities = ['A', 'B', 'C']
mouth_washer_healing_ability_names = ['Teeth cleaner', 'Full clean', 'Germ removal']
mouth_washer_healing_types = [HEAL, ALL_HEAL, REVIVAL]
mouth_washer_healing_costs = [16, 22, 30]
mouth_washer_STR = 2
mouth_washer_STR_max = 6
mouth_washer_STR_letters = ['A', 'B']
mouth_washer_STR_names = ['mouth wash whip', 'electric toothbrush rinces']
mouth_washer_STR_types = [M_ATK, M_ULTIMATE]
mouth_washer_STR_required = [4, 6]
mouth_washer_STR_damage = {1: [30, 35], 2: [20, 35]}


team = {'A': 'paste man', 'B': 'Brusher', 'C': 'mouth_washer'}
# Enemies
Bacteria_HP = 800
Bacteria_attacks = ['Normal attack','Rain of germs', 'infected strike', 'Bad breathe']
Bacteria_damage = {1: [30, 45], 2:[20, 45], 3: [60, 75], 4: [30, 45]}
Bacteria_types = [ATK, M_ATK, ATK, M_ATK]
infected_tooth_HP = 1075
infected_tooth_attacks = {'Normal attack': [10, 20], 'decaying spit':[20, 25], 'Potato chips': 1.50, 'infected bite': [30, 40]}
germ_pile_HP = 1400
germ_pile_attacks = {'Normal attack':[5, 10], 'Actinomyces whip':[15, 20], 'Fusobacterium rain':[15, 20], 'Candida spray':[30, 40]}
bosses = ['Bacteria', 'Infected_tooth', 'germ_pile']
team = ['brusher']


actions = ('''Enter which of the following actions you want to performs
            A to use your normal attack
            
            P to use your physical attacks
            
            S to use your special attacks
            
            B to block
            
            I to select a item
            
            enter H for help''')

actions_2 = ('''Enter which of the following actions you want to performs
            A to use your normal attack
            
            P to use your physical attacks
            
            S to use your either use a special attack or a healing ability
            
            B to block
            
            I to select a item

            enter H for help''')
def single_select_item(HP, HP_max, MP, MP_max, end_turn, character, type_of_item):
    if type_of_item == H:
        if HP > 0:
            if HP < HP_max:
                HP += 75
                if HP > HP_max:
                    HP = HP_max
                    print("\nHP = {}/{}\n".format(HP, HP_max))
                    end_turn = True
                else:
                    print("\nHP = {}/{}\n".format(HP, HP_max))
                    end_turn = True

        elif HP == HP_max:
                print("Already at max HP")
                
        elif HP == 0:
             print("\n{} is unconcious\n".format(character))
        
                    
    elif type_of_item == F_H:
        if HP > 0:
            if HP < HP_max:
                HP = HP_max
                end_turn = True
                print("HP fully restored")
                print("\nHP = {}/{}\n".format(HP, HP_max))
            elif HP == HP_max:
                print("Already at max HP")
        elif HP == 0:
                print("\n{} is Unconcious\n".format(character))         

    elif type_of_item == MP_R:
        if HP > 0:
            if MP < MP_max:
                MP += 25
                if MP > MP_max:
                    MP = MP_max
                    print("\nMP = {}/{}\n".format(MP, MP_max))
                    end_turn = True
                else:
                    print("\nMP = {}/{}\n".format(MP, MP_max))
                    end_turn = True
            elif MP == MP_max:
                print("Already at max MP")
        elif HP == 0:
            print("\n{} is unconcious\n")      
                    
    elif type_of_item == REV:
        if HP == 0:
            HP += 175
            print("{} revived".format(character))
            end_turn = True
        elif HP > 0:
            print("{} is already concious".format(character))

    return HP, MP, end_turn

def all_item(paste_man_HP, paste_man_MP, brusher_HP, brusher_MP, mouth_washer_HP, mouth_washer_MP, type_of_item):
    '''This function is ued if the user wants to use a item that'll affact all characters (Provided that character is concious)'''
    if type_of_item == A_H: # Heal any concious characters by 50HP
        heal_paste_man = True
        while heal_paste_man == True:
            if paste_man_HP > 0:
                paste_man_HP += 50
                heal_paste_man = False
            elif paste_man_HP == 0:
                print("Paste man I unconcious")
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


    elif type_of_item == R: # restore all characters HP and MP (provided that character is concious)
        restore_paste_man = True
        while restore_paste_man == True:
            if paste_man_HP > 0:
                paste_man_HP = 475
                paste_man_MP = 120
                restore_paste_man = False
            elif paste_man_HP == 0:
                print("\nPaste man is unconcious\n")
                restore_paste_man = False

        restore_brusher = True
        while restore_brusher == True:
            if brusher_HP > 0:
                brusher_HP = 410
                brusher_MP = 115
                restore_brusher = False
            elif brusher_HP == 0:
                print("\nBrusher is unconcious\n")
                restore_brusher = False

        restore_mouth_washer = True
        while restore_mouth_washer == True:
            if mouth_washer_HP > 0:
                mouth_washer_HP = 390
                mouth_washer_MP = 145
                restore_mouth_washer = False
            elif mouth_washer_HP == 0:
                print("\nBrusher is unconcious\n")
                restore_mouth_washer = False
                    
        print("HP and MP restored")       
                
    return paste_man_HP, paste_man_MP, brusher_HP, brusher_MP, mouth_washer_HP, mouth_washer_MP

    
def rules():
    print("""Welcome to my Dental RPG battle sim, you'll fight bacteria and infected teeth with a team of characters and attack in turns. You can either
          use all 3 characters by yourself or have some friends play with you, with each of them using a different character.""")

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
            round(boosted_damage)
            B_HP -= boosted_damage
            print("\nYou dealt {} damage\n".format(boosted_damage))

        elif buff == False:
            B_HP -= damage_dealt
            print("You dealt {} damage".format(damage_dealt))
        if STR < STR_max:
            STR += 1
            print("STR = {}/{}".format(STR, STR_max))
            
    return B_HP, buff, STR

def enemy_attack(name_of_ATK, attack_type, dam, HP, char, block, enemy_turn):
    '''The enemy will randomly choose a attack from their particular list of attacks and will try to use it on 1 of the characters, which will be selected before
    this function is called'''
    select = True
    while select == True:
        attack_used = random.choice(name_of_ATK)
        pick = name_of_ATK.index(attack_used)
        type_of_attack = attack_type[pick]
        print(attack_used)
        if type_of_attack == ATK:
            connect = random.randint(1, 4)
            if connect == 1 or connect == 2 or connect == 3:
                damage_1 = dam[pick + 1][0]
                damage_2 = dam[pick + 1][1]
                damage_dealt = random.randint(damage_1, damage_2)
                print('Hit')
                if block == True:
                    print('{} was blocking'.format(char))
                    decreased_damage = damage_dealt / 2
                    round(decreased_damage, 0)
                    HP -= decreased_damage
                    print("{} took {} damage".format(char, decreased_damage))
                    if HP < 0:
                        HP = 0
                        print("{} has fallen".format(char))
                        enemy_turn = False
                        select = False
                    else:
                        print("{} HP = {}".format(char, HP))
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
                        enemy_turn = False
                        select = False
            else:
                print('Miss')
                select = False
                enemy_turn = False
                
        elif type_of_attack == M_ATK:
            connect = random.randint(1,4)
            if connect == 1 or connect == 2 or connect == 3:
                damage_1 = dam[pick + 1][0]
                damage_2 = dam[pick + 1][1]
                hits = random.randint(1, 5)
                damage_dealt = random.randint(damage_1, damage_2) * hits
                print('Hit')
                print("The attack landed {} times".format(hits))
                if block == True:
                    print('{} was blocking'.format(char))
                    decreased_damage = damage_dealt / 2
                    round(decreased_damage, 0)
                    HP -= decreased_damage
                    print("{} took {} damage".format(char, damage_dealt))
                    if HP < 0:
                        HP = 0
                        print("{} has fallen".format(char))
                        enemy_turn = False
                        select = False
                    else:
                        print("{} HP = {}".format(char, HP))
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
                        print("{} HP = {}".format(char, HP))
                        enemy_turn = False
                        select = False
            else:
                print('Miss')
                enemy_turn = False
                select = False

    return HP, enemy_turn
    


def special_attack(letter_of_ATK, name_of_ATK, type_of_ATK, cost_of_ATK, MP, dam, B_HP, buff, turn, select_ability):
    choice = True
    while choice == True:
        for letter, name, type, cost in zip(letter_of_ATK, name_of_ATK, type_of_ATK, cost_of_ATK):
            print("{}, {}, {}, {}".format(letter, name, type, cost))
        print("MP = {}".format(MP))
        attack = input("Please enter the letter for what attack you want to use or enter 'R' to return to the previous screen").upper()
        if attack == 'R':
            choice = False
        elif attack in letter_of_ATK:
            pick = letter_of_ATK.index(attack)
            result = type_of_ATK[pick]
            required_cost = cost_of_ATK[pick]
            if MP >= required_cost:
                if result == ATK:
                    MP -= required_cost
                    connect = random.randint(1,2)
                    if connect == 1:
                        damage_1 = dam[pick + 1][0]
                        damage_2 = dam[pick + 1][1]
                        damage_dealt = random.randint(damage_1, damage_2)
                        print("Hit")
                        if buff == True:
                            boosted_damage = damage_dealt * 1.50
                            round(boosted_damage, 0)
                            B_HP -= boosted_damage
                            print("You attack was buffed")
                            print("\nYou dealt {} damage\n".format(boosted_damage))
                            choice = False
                            turn = False
                            buff = False
                            select_ability = False
                        elif buff == False:
                            B_HP -= damage_dealt
                            print("\n you dealt {} damage\n".format(damage_dealt))
                            choice = False
                            turn = False
                            select_ability = False
                            
                    else:
                        print('miss')
                        choice = False
                        turn = False
                        buff = False
                        select_ability = False
                        
                elif result == M_ATK:
                    MP -= required_cost
                    connect = random.randint(1,2)
                    if connect == 1:
                        damage_1 = dam[pick + 1][0]
                        damage_2 = dam[pick + 1][1]
                        hits = random.randint(1,5)
                        damage_dealt = random.randint(damage_1, damage_2) * hits
                        if buff == True:
                            boosted_damage = damage_dealt * 1.50
                            round(boosted_damage, 0)
                            print('Hit')
                            print("You attack was buffed")
                            print('\nYou attack landed {} times\n'.format(hits))
                            B_HP -= boosted_damage
                            print("You dealt {} damage".format(boosted_damage))
                            choice = False
                            turn = False
                            buff = False
                            select_ability = False
                        elif buff == False:
                            print('Hit')
                            print('\nYou attack landed {} times\n'.format(hits))
                            B_HP -= damage_dealt
                            print("You dealt {} damage".format(damage_dealt))
                            choice = False
                            turn = False
                            select_ability = False
                        
                    else:
                        print('miss')
                        choice = False
                        turn = False
                        buff = False
                        select_ability = False
                        
                elif result == BUFF:
                    if buff == False:
                        buff = True
                        choice = False
                        turn = False
                        print("Buffed and ready")
                        MP -= required_cost
                    elif buff == True:
                        print("Already buffed")
                elif MP < required_cost:
                    print("Not enough MP")

            elif MP < required_cost:
                print("\n not enough MP\n")
        else:
            print("That wasn't a option")
                
                    
                
                    
        
                
        return B_HP, MP, turn, buff, select_ability

def heal_ability(paste_man_HP, brusher_HP, mouth_washer_HP, MP, turn, heal_abilities, healing_names, healing_types, healing_costs, select_ability):
    '''This function is if the dcharacter wants to use a special that heals 1 or all characters'''
    for letter, name, type_of_healing, cost in zip(heal_abilities, healing_names, healing_types, healing_costs):
        print("{}, {}, {}, {}".format(letter, name, type_of_healing, cost))
    heal_char = True
    while heal_char == True:
        print(MP)
        heal = input("Enter the letter for what healing ability you want to use or enter 'R' to return to before").upper()
        if heal == 'R':
            heal_char = False
        elif heal in heal_abilities:
            pick = heal_abilities.index(heal)
            result = healing_types[pick]
            required_cost = healing_costs[pick]
            if MP >= required_cost:
                if result == HEAL:  # The user wants to heal one character
                    select = True
                    while select == True:
                        print("'A', paste man HP = {}/475".format(paste_man_HP))
                        print("'B', brusher HP = {}/410".format(brusher_HP))
                        print("'C', mouth washer HP = {}/390".format(mouth_washer_HP))
                        select_char = input("Please select what character you want to heal or enter R top return to before").upper()
                        if select_char == 'R':
                            select = False
                        elif select_char == 'A':
                            if paste_man_HP > 0:
                                paste_man_HP += 75
                                if paste_man_HP > 475:
                                    paste_man_HP = 475
                                    print("\npaste man HP = {}/475\n".format(paste_man_HP))
                                    turn = False
                                    select = False
                                    heal_char = False
                                    select_ability = False
                                    MP -= required_cost
                                else:
                                    print("\npaste man HP = {}/475\n".format(paste_man_HP))
                                    turn = False
                                    select = False
                                    heal_char = False
                                    select_ability = False
                                    MP -= required_cost
                            elif paste_man_HP == 475:
                                print("Already at max HP")
                                
                            elif paste_man_HP == 0:
                                print("Paste man is unconcious")
                        elif select_char == 'B':
                            if brusher_HP > 0:
                                brusher_HP += 75
                                if brusher_HP > 410:
                                    brusher_HP = 410
                                    print("\nbrusher HP = {}/410\n".format(brusher_HP))
                                    turn = False
                                    select = False
                                    heal_char = False
                                    select_ability = False
                                    MP -= required_cost
                                else:
                                    print("\nbrusher HP = {}/410\n".format(brusher_HP))
                                    turn = False
                                    select = False
                                    heal_char = False
                                    select_ability = False
                                    MP -= required_cost
                            elif brusher_HP == 410:
                                print("Already at max HP")     
                            elif brusher_HP == 0:
                                print("brusher is unconcious")
                                
                        elif select_char == 'C':
                            if mouth_washer_HP > 0:
                                mouth_washer_HP += 75
                                if mouth_washer_HP > 390:
                                    mouth_washer_HP = 390
                                    print("\nmouth washer HP = {}/390\n".format(mouth_washer_HP))
                                    turn = False
                                    select = False
                                    heal_char = False
                                    select_ability = False
                                    MP -= required_cost
                                else:
                                    print("\nmouth washer HP = {}/410\n".format(mouth_washer_HP))
                                    turn = False
                                    select = False
                                    heal_char = False
                                    select_ability = False
                                    MP -= required_cost
                            elif mouth_washer_HP == 390:
                                print("Already at max HP")
                            elif mouth_washer_HP == 0:
                                print("Mouth washer is unconcious")
                        else:
                            print("That wasn't a option")

                elif result == ALL_HEAL:  # The user wants to heal all charcters
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
                        
                    print("All characters healed")   
                    MP -= required_cost
                    turn = False
                    heal_char = False
                    select_ability = False


                elif result == REVIVAL: # the user wants to revive a fallen character
                    print("'A', paste man HP = {}/475".format(paste_man_HP))
                    print("'B', brusher HP = {}/410".format(brusher_HP))
                    print("'C', mouth washer HP = {}/390".format(mouth_washer_HP))
                    select_char = True
                    while select_char == True:
                        character = input("Enter the letter for what character you want to revive, or enter R to return to the previous screen (note: a character has to have 0 HP to be revived").upper()
                        if character == 'R':
                            select_char = False
                        elif character == 'A':
                            if paste_man_HP == 0:
                                paste_man_HP += 200
                                print("Paste man revived")
                                MP -= required_cost
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
                                MP -= required_cost
                                select_char = False
                                turn = False
                                select_ability = False
                                heal_char = False
                            elif brusher_HP > 0:
                                print("Brusher is already concious")
                        elif character == 'C':
                            if mouth_washer_HP == 0:
                                mouth_washer_HP += 200
                                print("Mouth washer revived")
                                MP -= required_cost
                                select_char = False
                                turn = False
                                select_ability = False
                                heal_char = False
                            elif mouth_washer_HP > 0:
                                print("Mouth washer is already concious")
                        else:
                            print("That wasn't an option")
                
            elif MP < required_cost:
                print("Not enough MP")
        else:
            print("That wasn't an option")

    return paste_man_HP, brusher_HP, mouth_washer_HP, MP, turn, select_ability

def physical(boss_HP, STR, turn, letter_of_ATK, name_of_ATK, type_of_ATK, STR_required, dam):
    for letter, name, ATK_type, STR_cost in zip(letter_of_ATK, name_of_ATK, type_of_ATK, STR_required):
        print("{}, {}, {}, {}".format(letter, name, ATK_type, STR_cost))
    choice = True
    while choice == True:
        attack = input("Please enter the letter for what attack you want to use or enter R to return to the previous screen").upper()
        if attack == 'R':
            choice = False
        elif attack in letter_of_ATK:
            pick = letter_of_ATK.index(attack)
            result = type_of_ATK[pick]
            STR_cost = STR_required[pick]
            if STR >= STR_cost:
                if result == ATK:
                    STR -= STR_cost
                    connect = random.randint(1,4)
                    if connect == 1 or connect == 2 or connect == 3:
                        damage_1 = dam[pick + 1][0]
                        damage_2 = dam[pick + 1][1]
                        damage_dealt = random.randint(damage_1, damage_2)
                        print("Hit")
                        boss_HP -= damage_dealt
                        print("\nYou dealt {} damage\n".format(damage_dealt))
                        choice = False
                        turn = False
                            
                    else:
                        print('miss')
                        choice = False
                        turn = False
                        
                elif result == ULTIMATE:
                    STR -= STR_cost
                    damage_1 = dam[pick + 1][0]
                    damage_2 = dam[pick + 1][1]
                    damage_dealt = random.randint(damage_1, damage_2)
                    print("Hit")
                    boss_HP -= damage_dealt
                    print("\nYou used your strongest attack and dealt {} damage\n".format(damage_dealt))
                    choice = False
                    turn = False

                elif result == M_ATK:
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
                        choice = False
                        turn = False
                            
                    else:
                        print('miss')
                        choice = False
                        turn = False

                elif result == M_ULTIMATE:
                    STR -= STR_cost
                    damage_1 = dam[pick + 1][0]
                    damage_2 = dam[pick + 1][1]
                    hits = random.randint(1,3)
                    damage_dealt = random.randint(damage_1, damage_2) * hits
                    print("Hit")
                    print("Your attack landed {} times".format(hits))
                    boss_HP -= damage_dealt
                    print("\nYou used your strongest attack and dealt {} damage\n".format(damage_dealt))
                    choice = False
                    turn = False

            elif STR < STR_cost:
                print("Not enough STR")
            
        else:
            print("That wasn't an option")
    return boss_HP, STR, turn

def tutorial():
    '''This function is called if the user needs help with understanding how certain actions work'''
    print('''
    'A'  for HP
    'B'  normal attack
    'C'  for STR
    'D'  for physical attack
    'E'  for MP
    'F'  for special ability
    'G'  for block
    'H'  to use a item
    'I'  for turn order
    'J'  for what the goal is''')
    help_me = True
    while help_me == True:
        information = input("Enter a letter too see a tutorial for how that action works incase you don't understand, or enter R to return to battle when you're done").upper()
        if information == 'R':
            help_me = False
        elif information == 'A':
            print("\nEach character has a set amount of HP, which is that characters health. If the enemies attack lands the character will lose HP. If a character runs out of HP that character will be unconcious and won't be able to do anything unless they are revived\n")
        elif information == 'B':
            print("\nEnter 'A' on the previous screen to have your character use a normal attack. Normal attacks do very small damage but have a high chance of landing a hit on the enemy and if it lands the character will gain 1 STR\n")
        elif information == 'C':
            print("\nSTR is a special type of point each character has. They have a limit to how much they can have and start with 3 and gain 1 at the start of their turn (with the exception of their starting turn) if that character is concious.\n")
        elif information == 'D':
            print("\nEntering 'P' on the previous screen will have a character use their physical attack. Physical attacks do the most damage out of all attacks and require STR to use. When you enter P a list of that characters physical attacks will appear. The letter at the start of each line is what you enter to use it, the text is the name and what it'll do, and the number at the end is how much STR you need too use it. If you don't have the right amount of STR you can't use it. Using a physical attack will use that amount of STR. Each character also has a ultimate physical attack, which requires the most STR they can have but deals alot of damage and will hit no matter what.\n")
        elif information == 'E':
            print("\nMP is used for using special abilities, which are attacks that don't deal as much damage as physical attacks, but you have alot more MP so they can be used much more. Though make sure your careful since unlike HP or STR the only way to recover MP is by using A couple items, so make sure your conservative with it\n")
        elif information == 'F':
            print("\nEntering 'S' on the previous screen will let you use a special attack. These cost a set number of MP to use and will deplete that amount of MP upon use. The letter at the start is what to enter, the text is the name and what it does, and the number at the end is how much it costs. If you don't have the right amount of MP the attack won't work. Also just real quick, the third character Mouth washer has 2 options for special abilities. Attack and healing. After entering S on mouth washers turn you can either enter A to use a attacking special, or H to use a healing special which can heal or revive all fallen character.\n")
        elif information == 'G':
            print("\nEntering 'B' on the previous screen will have your character block, if a character blocks they won't be able to attacks, or use an item, but if a character is blocking it'll last until their next turn, and if they get attacked they take half the damage. Blocking is very useful if your character is running lock on attacks\n")
        elif information == 'H':
            print("\nEntering 'I' on the previous screen will give you the option to use a item on one or all characters. Enter the letter next to each characters current HP, MP and STR to use an item on that character, or F to use an item that'll affect all characters. Items can do things like heal characters, revive characters and restore MP. Enter the letter next to each item to use that item. The text between shows the name and what that item does and the number at the end is how much of that item you have. If you use an item that amount will decrease by 1 and if you don't have the required amount then you can't use that item. Theres no way to get a item back after using it so make sure you use it when your sure you want to\n")
        elif information == 'I':
            print("\nEach character will go in turns. First it's paste man, then brusher, then Mouth washer and finally the enemy. After that it starts over. You can select what the 3 characters do, but the enemy chooses something automaticly. You can either use all 3 characters by yourself or have friends play with you, each choosing what to do\n")
        elif information == 'J':
            print("\nThe main goal of the game is too try and defeat a randomly selected enemy. DO this by attacking it until it's HP reaches 0. If you do that then you win. But if all 3 characters HP reaches 0 then it's game over and you lose\n")
        else:
            print("\nThat wasn't an option\n")
        
def turn_order(paste_man_MP, paste_man_HP, paste_man_STR, brusher_HP, brusher_MP, brusher_STR, mouth_washer_HP, mouth_washer_MP, mouth_washer_STR):
    single_item_letter = ['A', 'B', 'C', 'D']
    single_items_carried = ['Tooth cleaner', 'Mint', 'power paste', 'Dentist spray']
    single_item_types = [H, F_H, MP_R, REV]
    single_item_amounts = [4, 3, 2, 3]
    all_item_letters = ['A', 'B']
    all_items_carried = ['Mouthwash', 'Gold toothpaste']
    all_item_types = [A_H, R]
    all_item_amounts = [3, 2]
    end_turn = False
    # paste man variables used
    paste_man_turn = True
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
    boss = 'Bacteria'
    boss_HP = Bacteria_HP
    boss_max = Bacteria_HP
    boss_attacks = Bacteria_attacks
    boss_damage = Bacteria_damage
    boss_types = Bacteria_types
    play = True
    print("\nIt's paste man's turn\n")
    while play == True:
        while paste_man_turn == True:
            print("HP = {}/475".format(paste_man_HP))
            print("MP = {}/120".format(paste_man_MP))
            print("STR = {}/5".format(paste_man_STR))
            print(actions)
            paste_man_block = False
            action = input("Select what action above you want to perform").upper()
            if action == 'A':   # the user wants to use a normal attack
                print('You used a normal attack')
                (boss_HP, none, paste_man_STR) = normal_attack(boss_HP, paste_man_normal_attack, none, paste_man_STR, paste_man_STR_max)
                paste_man_turn = False

            elif action == 'P': # The user wants to use a physical attack
                (boss_HP, paste_man_STR, paste_man_turn) = physical(boss_HP, paste_man_STR, paste_man_turn, paste_man_STR_letters, paste_man_STR_names, paste_man_STR_types, paste_man_STR_required, paste_man_STR_damage)
                
            elif action == 'S': # the user wants to use a special attack
                (boss_HP, paste_man_MP, paste_man_turn, none, none_2) = special_attack(paste_man_letters, paste_man_names, paste_man_types, paste_man_costs, paste_man_MP, paste_man_damage, boss_HP, none, paste_man_turn, none_2)                

            elif action == 'B': # the user wants to block
                print('You chose to block')
                paste_man_block = True
                paste_man_turn = False

            elif action == 'I': # the user wants to use a item
                select_char = True
                while select_char == True:
                    print("'A', paste man HP = {}/475, paste man MP = {}/120".format(paste_man_HP, paste_man_MP))
                    print("'B', brusher HP = {}/410, brusher MP = {}/115".format(brusher_HP, brusher_MP))
                    print("'C', mouth washer HP = {}/390, mouth washer MP = {}/145".format(mouth_washer_HP, mouth_washer_MP))
                    print("'F', Use a item that effects all characters")
                    use_on = input("Enter the letter for who you want to use a item on, enter F to use a item that effects all, or enter R to return to the previous screen").upper()
                    if use_on == 'R':
                        select_char = False
                    elif use_on == 'A' or use_on == 'B' or use_on == 'C':
                        for letter, name_of_item, type_of_item, amount in zip(single_item_letter, single_items_carried, single_item_types, single_item_amounts):
                            print("{}, {}, {}, {}".format(letter, name_of_item, type_of_item, amount))
                        item = input("Please enter the letter for what item you want to use for enter R to return to the action select screen").upper()
                        if item == R:
                            select_char = False
                        elif item in single_item_letter:
                            pick = single_item_letter.index(item)
                            item_name = single_items_carried[pick]
                            type_of_item = single_item_types[pick]
                            if single_item_amounts[pick] > 0:
                                if use_on == 'A':
                                    (paste_man_HP, paste_man_MP, end_turn) = single_select_item(paste_man_HP, paste_man_HP_max, paste_man_MP, paste_man_MP_max, end_turn, paste_man, type_of_item)
                                elif use_on == 'B':
                                    (brusher_HP, brusher_MP, end_turn) = single_select_item(brusher_HP, brusher_HP_max, brusher_MP, brusher_MP_max, end_turn, brusher, type_of_item)
                                elif use_on == 'C':
                                     (mouth_washer_HP, mouth_washer_MP, end_turn) = single_select_item(mouth_washer_HP, mouth_washer_HP_max, mouth_washer_MP, mouth_washer_MP_max, end_turn, mouth_washer, type_of_item)

                            elif single_item_amounts[pick] == 0:
                                print("Don't have any of this item")

                        else:
                            print("That's not an item")

                            if end_turn == True:
                                single_item_amounts[pick] -= 1
                                end_turn = False
                                paste_man_turn = False
                                select_char = False
                            elif end_turn == False:
                                print("Please select anothger item")
                    
                    elif use_on == 'F': #The user wants to use a item that effects all character
                        for letter, name_of_item, type_of_item, amount in zip(all_item_letters, all_items_carried, all_item_types, all_item_amounts):
                            print("{}, {}, {}, {}".format(letter, name_of_item, type_of_item, amount))
                        item = input("Please enter the letter for what item you want to use for enter R to return to the action select screen").upper()
                        if item == R:
                            select_char = False
                        elif item in all_item_letters:
                            pick = all_item_letters.index(item)
                            item_name = all_items_carried[pick]
                            type_of_item = all_item_types[pick]
                            if single_item_amounts[pick] > 0:
                                (paste_man_HP, paste_man_MP, brusher_HP, brusher_MP, mouth_washer_HP, mouth_washer_MP) = all_item(paste_man_HP, paste_man_MP, brusher_HP, brusher_MP, mouth_washer_HP, mouth_washer_MP, type_of_item)
                                single_item_amounts[pick] -= 1
                                select_char = False
                                paste_man_turn = False
                            elif single_item_amounts[pick] == 0:
                                print("Not enough of this item, please select somthing else")
                        else:
                            print("That wasn't an option")

                    else:
                        print("That wasn't a option")
            elif action == 'H': # The user wants help
                tutorial()
                
            else:
                print("That wasn't a option")

        if boss_HP > 0:
            print("Boss HP = {}/{}".format(boss_HP, boss_max))
            if brusher_HP == 0:
                print("\nBrusher is unconcious\n")
            else:
                brusher_turn = True
                if brusher_STR < 8:
                    brusher_STR += 1
                    print("\n It's brusher's turn\n")
                elif brusher_STR == 8:
                    print("\n It's brusher's turn\n")
        elif boss_HP <= 0:
            print("You won")
            play = False

            
        while brusher_turn == True: # brusher turn
            brusher_block = False
            print("HP = {}/410".format(brusher_HP))
            print("MP = {}/115".format(brusher_MP))
            print("STR = {}/8".format(brusher_STR))
            print(actions)
            action = input("Select what action above you want to perform").upper()
            if action == 'A':   # The user wants to use a normal attack
                print('You used a normal attack')
                (boss_HP, brusher_buff, brusher_STR) = normal_attack(boss_HP, brusher_normal_attack, brusher_buff, brusher_STR, brusher_STR_max)
                brusher_turn = False

            elif action == 'P':
                (boss_HP, brusher_STR, brusher_turn) = physical(boss_HP, brusher_STR, brusher_turn, brusher_STR_letters, brusher_STR_names, brusher_STR_types, brusher_STR_required, brusher_STR_damage)

            elif action == 'S': # The user wants to use a special attack
                (boss_HP, brusher_MP, brusher_turn, brusher_buff, none_2) = special_attack(brusher_special_attacks, brusher_special_attack_names, brusher_types, brusher_costs, brusher_MP, brusher_damage, boss_HP, brusher_buff, brusher_turn, none_2)

            elif action == 'B': #The user wants to block
                brusher_block = True
                brusher_turn = False
                
            elif action == 'I': # The user wants to use a item
                select_char = True
                while select_char == True:
                    print("'A', paste man HP = {}/475, paste man MP = {}/120".format(paste_man_HP, paste_man_MP))
                    print("'B', brusher HP = {}/410, brusher MP = {}/115".format(brusher_HP, brusher_MP))
                    print("'C', mouth washer HP = {}/390, mouth washer MP = {}/145".format(mouth_washer_HP, mouth_washer_MP))
                    print("'F', Use a item that effects all characters")
                    use_on = input("\nEnter the letter for who you want to use a item on, enter F to use a item that effects all, or enter R to return to the previous screen\n").upper()
                    if use_on == 'R':
                        select_char = False
                    elif use_on == 'A' or use_on == 'B' or use_on == 'C':
                        for letter, name_of_item, type_of_item, amount in zip(single_item_letter, single_items_carried, single_item_types, single_item_amounts):
                            print("{}, {}, {}, {}".format(letter, name_of_item, type_of_item, amount))
                        item = input("Please enter the letter for what item you want to use for enter R to return to the action select screen").upper()
                        if item == R:
                            select_char = False
                        elif item in single_item_letter:
                            pick = single_item_letter.index(item)
                            item_name = single_items_carried[pick]
                            type_of_item = single_item_types[pick]
                            if single_item_amounts[pick] > 0:
                                if use_on == 'A':
                                    (paste_man_HP, paste_man_MP, end_turn) = single_select_item(paste_man_HP, paste_man_HP_max, paste_man_MP, paste_man_MP_max, end_turn, paste_man, type_of_item)
                                elif use_on == 'B':
                                    (brusher_HP, brusher_MP, end_turn) = single_select_item(brusher_HP, brusher_HP_max, brusher_MP, brusher_MP_max, end_turn, brusher, type_of_item)
                                elif use_on == 'C':
                                     (mouth_washer_HP, mouth_washer_MP, end_turn) = single_select_item(mouth_washer_HP, mouth_washer_HP_max, mouth_washer_MP, mouth_washer_MP_max, end_turn, mouth_washer, type_of_item)

                            elif single_item_amounts[pick] == 0:
                                print("Don't have any of this item")
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
                            print("{}, {}, {}, {}".format(letter, name_of_item, type_of_item, amount))
                        item = input("Please enter the letter for what item you want to use for enter R to return to the action select screen").upper()
                        if item == R:
                            select_char = False
                        elif item in all_item_letters:
                            pick = all_item_letters.index(item)
                            item_name = all_items_carried[pick]
                            type_of_item = all_item_types[pick]
                            if single_item_amounts[pick] > 0:
                                (paste_man_HP, paste_man_MP, brusher_HP, brusher_MP, mouth_washer_HP, mouth_washer_MP) = all_item(paste_man_HP, paste_man_MP, brusher_HP, brusher_MP, mouth_washer_HP, mouth_washer_MP, type_of_item)
                                single_item_amounts[pick] -= 1
                                select_char = False
                                brusher_turn = False
                            elif single_item_amounts[pick] == 0:
                                print("Not enough of this item, please select somthing else")

                    else:
                        print("That wasn't a option")  

            else:
                print("That wasn't a option")

        if boss_HP > 0:
            print("Boss HP = {}/{}".format(boss_HP, boss_max))
            if mouth_washer_HP == 0:
                print("\n mouth washer is unconcious\n")
                enemy_turn = True
            else:
                if mouth_washer_STR < 6:
                    mouth_washer_STR += 1
                    print("\nIt's Mouth washer's turn\n")
                elif mouth_washer_STR == 6:
                    print("\nIt's Mouth washer's turn\n")
                mouth_washer_turn = True
        elif boss_HP <= 0:
            print("You won")
            play = False

        while mouth_washer_turn == True:    # Mouth washer's turn
            mouth_washer_block = False
            print("HP = {}/390".format(mouth_washer_HP))
            print("MP = {}/145".format(mouth_washer_MP))
            print("STR = {}/6".format(mouth_washer_STR))
            print(actions_2)
            action = input("Please enter the letter for what action you want to perform").upper()
            if action == 'A':   # The user wants to use a normal attack
                print('You used a normal attack')
                (boss_HP, none, mouth_washer_STR) = normal_attack(boss_HP, mouth_washer_normal_attack, none, mouth_washer_STR, mouth_washer_STR_max)
                mouth_washer_turn = False

            elif action == 'P':
                (boss_HP, mouth_washer_STR, mouth_washer_turn) = physical(boss_HP, mouth_washer_STR, mouth_washer_turn, mouth_washer_STR_letters, mouth_washer_STR_names, mouth_washer_STR_types, mouth_washer_STR_required, mouth_washer_STR_damage)

            elif action == 'S': # The user wants to use a special attack
                select_ability = True
                while select_ability == True:
                    type_of_special = input("Enter A to use a special ability that'll attack the enemy or H to use a special that'll heal a character, or R to return to before").upper()
                    if type_of_special == 'R':
                        select_ability = False
                    elif type_of_special == 'A':                        
                        (boss_HP, mouth_washer_MP, mouth_washer_turn, none, select_ability) = special_attack(mouth_washer_attacks, mouth_washer_special_attacks_names, mouth_washer_types, mouth_washer_costs, mouth_washer_MP, mouth_washer_damage, boss_HP, none, mouth_washer_turn, select_ability)
                    elif type_of_special == 'H':
                        (paste_man_HP, brusher_HP, mouth_washer_HP, mouth_washer_MP, mouth_washer_turn, select_ability) = heal_ability(paste_man_HP, brusher_HP, mouth_washer_HP, mouth_washer_MP, mouth_washer_turn, mouth_washer_healing_abilities, mouth_washer_healing_ability_names, mouth_washer_healing_types, mouth_washer_healing_costs, select_ability)

                    else:
                        print("That wasn't an option")

            elif action == 'B': #The user wants to block
                mouth_washer_block = True
                mouth_washer_turn = False
                
            elif action == 'I': # The user wants to use a item
                select_char = True
                while select_char == True:
                    print("'A', paste man HP = {}/475, paste man MP = {}/120".format(paste_man_HP, paste_man_MP))
                    print("'B', brusher HP = {}/410, brusher MP = {}/115".format(brusher_HP, brusher_MP))
                    print("'C', mouth washer HP = {}/390, mouth washer MP = {}/145".format(mouth_washer_HP, mouth_washer_MP))
                    print("'F', Use a item that effects all characters")
                    use_on = input("Enter the letter for who you want to use a item on, enter F to use a item that effects all, or enter R to return to the previous screen").upper()
                    if use_on == 'R':
                        select_char = False
                    elif use_on == 'A' or use_on == 'B' or use_on == 'C':
                        for letter, name_of_item, type_of_item, amount in zip(single_item_letter, single_items_carried, single_item_types, single_item_amounts):
                            print("{}, {}, {}, {}".format(letter, name_of_item, type_of_item, amount))
                        item = input("Please enter the letter for what item you want to use for enter R to return to the action select screen").upper()
                        if item == R:
                            select_char = False
                        elif item in single_item_letter:
                            pick = single_item_letter.index(item)
                            item_name = single_items_carried[pick]
                            type_of_item = single_item_types[pick]
                            if single_item_amounts[pick] > 0:
                                if use_on == 'A':
                                    (paste_man_HP, paste_man_MP, end_turn) = single_select_item(paste_man_HP, paste_man_HP_max, paste_man_MP, paste_man_MP_max, end_turn, paste_man, type_of_item)
                                elif use_on == 'B':
                                    (brusher_HP, brusher_MP, end_turn) = single_select_item(brusher_HP, brusher_HP_max, brusher_MP, brusher_MP_max, end_turn, brusher, type_of_item)
                                elif use_on == 'C':
                                     (mouth_washer_HP, mouth_washer_MP, end_turn) = single_select_item(mouth_washer_HP, mouth_washer_HP_max, mouth_washer_MP, mouth_washer_MP_max, end_turn, mouth_washer, type_of_item)

                            elif single_item_amounts[pick] == 0:
                                print("Don't have any of this item")
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
                            print("{}, {}, {}, {}".format(letter, name_of_item, type_of_item, amount))
                        item = input("Please enter the letter for what item you want to use for enter R to return to the action select screen").upper()
                        if item == R:
                            select_char = False
                        elif item in all_item_letters:
                            pick = all_item_letters.index(item)
                            item_name = all_items_carried[pick]
                            type_of_item = all_item_types[pick]
                            if single_item_amounts[pick] > 0:
                                (paste_man_HP, paste_man_MP, brusher_HP, brusher_MP, mouth_washer_HP, mouth_washer_MP) = all_item(paste_man_HP, paste_man_MP, brusher_HP, brusher_MP, mouth_washer_HP, mouth_washer_MP, type_of_item)
                                single_item_amounts[pick] -= 1
                                select_char = False
                                mouth_washer_turn = False
                            elif single_item_amounts[pick] == 0:
                                print("Not enough of this item, please select somthing else")

                    else:
                        print("That wasn't a option")  

            else:
                print("That wasn't a option")
            

        if boss_HP > 0:
            print("\nIt's {}'s turn\n".format(boss))
            enemy_turn = True
        elif boss_HP <= 0:
            print("You won")
            play = False
                
        
        # Now it's the enemies turn
        while enemy_turn == True:
            print("HP = {}/{}".format(boss_HP, boss_max))
            target = random.choice(team)
            if target == 'paste man':
                if paste_man_HP > 0:
                    (paste_man_HP, enemy_turn) = enemy_attack(boss_attacks, boss_types, boss_damage, paste_man_HP, target, paste_man_block, enemy_turn)
                    choose_target = False
                else:
                    print("picking attack")
            elif target == 'brusher':
                if brusher_HP > 0:
                    (brusher_HP, enemy_turn) = enemy_attack(boss_attacks, boss_types, boss_damage, brusher_HP, target, brusher_block, enemy_turn)
                    choose_target = False
                else:
                    print("picking attack")
            elif target == 'mouth washer':
                if mouth_washer_HP > 0:
                    (mouth_washer_HP, enemy_turn) = enemy_attack(boss_attacks, boss_types, boss_damage, mouth_washer_HP, target, mouth_washer_block, enemy_turn)
                else:
                    print("Picking attack")
            if paste_man_HP == 0 and brusher_HP == 0 and mouth_washer_HP == 0:
                print("Game over you lost")
                play = False
            elif paste_man_HP > 0:
                paste_man_turn = True
                if paste_man_STR < 5:
                    paste_man_STR += 1
                    print("\nPaste man's turn\n")
                else:
                    print("\nPaste man's turn\n")
            elif paste_man_HP == 0:
                print('Paste man is unconcious')

                
            
turn_order(paste_man_MP, paste_man_HP, paste_man_STR, brusher_HP, brusher_MP, brusher_STR, mouth_washer_HP, mouth_washer_MP, mouth_washer_STR)

