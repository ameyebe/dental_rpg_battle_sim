# dental_rpg_battle_sim.py
# date: 1/07/2019
# Author: Benjamin Ameye
import random

# types of special attacks
ATK = 'Attack'
M_ATK = 'Multi Attack'
BUFF = 'Next attack will deal a extra 50% damage'
HEAL = 'Heal 1 character by 75 HP'


# item types
H = 'Heals 1 character by 75 HP' 
A_H = 'Heals all characters by 50 HP'
F_H =  'Fully heals 1 character' 
R = 'Restores all characters HP and SP' 
MP_R = 'Restores 1 characters MP by 25' 


#The characters max HP, MP and list of special attacks
# Paste man
paste_man_HP = 475
paste_man_MP = 120
paste_man_letters = ['A', 'B', 'C']
paste_man_names = ['Toothpaste squirt', 'tooth pick jab', 'clean breathe']
paste_man_types = [ATK, ATK, M_ATK]
paste_man_costs = [9, 16, 19]
paste_man_damage = {1: [15, 20], 2: [30, 45], 3: [40, 45]}
paste_man_normal_attack = [5, 10]
# Brusher
brusher_HP = 410
brusher_MP = 115
brusher_special_attacks = ['A', 'B', 'C', 'D']
brusher_special_attack_names = ['Brush smack', 'Clean rinse', 'Ultimate scrub', 'Add toothpaste']
brusher_types = [ATK, M_ATK, ATK, BUFF]
brusher_costs = [10, 11, 20, 22]
brusher_damage = {1: [20, 25], 2: [20, 30], 3: [50,55]}
brusher_normal_attack = [10, 15]
# Mouth washer
mouth_washer_HP = 360
mouth_washer_MP = 145
mouth_washer_special_attacks = {'A': 'Dental floss whip', 'B': 'Teeth cleaner', 'C': 'Mouthwash Blast', 'D': 'Full clean'}
mouth_washer_results = {8: [10, 15], 16: '75HP', 21: [35, 45], 22: '75HP'}
mouth_washer_costs = ['8 MP', '16 MP', '21 MP', '22 MP']
#mouth_washer_results = [{10, 15}, '75 HP', {35, 45}, '75 HP']

team = {'A': 'paste man', 'B': 'Brusher', 'C': 'mouth_washer'}
# Enemies
Bacteria_HP = 1200
Bacteria_attacks = ['Normal attack','Rain of germs', 'infected strike', 'Bad breathe']
Bacteria_damage = {1: [10, 15], 2:[30, 50], 3: [25, 35], 4: [10, 15]}
Bacteria_types = [ATK, M_ATK, ATK, ATK]
infected_tooth_HP = 1075
infected_tooth_attacks = {'Normal attack': [10, 20], 'decaying spit':[20, 25], 'Potato chips': 1.50, 'infected bite': [30, 40]}
germ_pile_HP = 1400
germ_pile_attacks = {'Normal attack':[5, 10], 'Actinomyces whip':[15, 20], 'Fusobacterium rain':[15, 20], 'Candida spray':[30, 40]}
bosses = ['Bacteria', 'Infected_tooth', 'germ_pile']
team = ['paste man']


actions = ('''Enter which of the following actions you want to performs
            A to use your normal attack
            S to use your special attacks
            B to block
            I to select a item''')
def select_item(paste_man_HP, brusher_HP, paste_man_MP, turn, item_letter, items_carried, item_types, item_amounts):
    for letter, items, types, amounts in zip(item_letter, items_carried, item_types, item_amounts):
        print("{}, {}, {}, {}".format(letter, items, types, amounts))
    select = True
    while select == True:
        item = input("Please enter the letter for what item you want to use for enter R to return to the action select screen").upper()
        if item == 'R':
            select = False
        elif item in item_letter:
            pick = item_letter.index(item)
            item_name = items_carried[pick]
            type_of_item = item_types[pick]
            amount = item_amounts[pick]
            if amount > 0:
                if type_of_item == H:
                    choice = True
                    while choice == True:
                        print("'A': paste man HP = {}/475".format(paste_man_HP))
                        print("'B': brusher HP = {}/410".format(brusher_HP))
                        character = input('Enter the letter for what character you want to heal, or enter 'R' to return to the previous screen').upper()
                        if character == 'R':
                            choice = False
                        elif character == 'A':
                            if paste_man_HP > 0:
                                if paste_man_HP < 475:
                                    paste_man_HP += 75
                                    amount -= 1
                                    item_amounts[pick] = amount
                                    if paste_man_HP > 475:
                                        paste_man_HP = 475
                                        print("you healed paste man")
                                        print(paste_man_HP)
                                        choice =  False
                                        select = False
                                        turn = False
                                    else:
                                        print("you healed paste_man")
                                        print(paste_man_HP)
                                        choice = False
                                        select = False
                                        turn = False
                                elif paste_man_HP == 475:
                                    print('Paste man is already has fully health')
                            else:
                                print("paste man is unconcious")
                        elif character == 'B':
                            if brusher_HP > 0:
                                if brusher < 410:
                                    brusher_HP += 75
                                    amount -= 1
                                    item_amounts[pick] = amount
                                    if brusher_HP > 410:
                                        brusher_HP = 410
                                        print("you healed brusher")
                                        print(brusher_HP)
                                        choice =  False
                                        select = False
                                        turn = False
                                    else:
                                        print("you healed brusher")
                                        print(brusher_HP)
                                        choice = False
                                        select = False
                                        turn = False
                                elif brusher_HP == 410:
                                    print('brusher is already has fully health')
                            else:
                                print("brusher is unconcious")
            
                        else:
                            print("That wasn't a option")
                        
                elif type_of_item == F_H:
                    choice = True
                    while choice == True:
                        print("'A': paste man HP = {}/ 475".format(paste_man_HP))
                        print("'B': brusher HP = {}/410".format(brusher_HP))
                        character = input('Enter the letter for what character you want to heal, or enter 'R' to return to the previous screen').upper()
                        if character == 'R':
                            choice = False
                        elif character == 'A':
                            if paste_man_HP > 0:
                                if paste_man_HP < 475:
                                    amount -= 1
                                    item_amounts[pick] = amount
                                    print("Fully healed paste man")
                                    paste_man_HP = 475
                                    print(paste_man_HP)
                                    choice = False
                                    select = False
                                    turn = False
                                elif paste_man_HP == 475:
                                    print('Paste man is already at full health')
                            else:
                                print('Paste man is unconcious')

                elif type_of_item == MP_R:
                    choice = True
                    while choice == True:
                        print("'A': paste man MP = {}/ 120".format(paste_man_MP))
                        character = input("Enter the letter for which character's MP you want to restore, or enter 'R' to return to the previous screen").upper()
                        if character == 'R':
                            choice = False
                        elif character == 'A':
                            if paste_man_HP > 0:
                                if paste_man_MP < 120:
                                    amount -= 1
                                    item_amounts[pick] = amount
                                    paste_man_MP += 25
                                    if paste_man_MP > 120:
                                        paste_man_MP = 120
                                        print(paste_man_MP)
                                        choice = False
                                        select = False
                                        turn = False
                                    else:
                                        print(paste_man_MP)
                                        choice = False
                                        select = False
                                        turn = False
                                else:
                                    print("paste man already has max MP")
                            else:
                                print("paste man is unconcious")
                        else:
                            print("That wasn't an option")
                elif type_of_item == R:
                    amount -= 1
                    item_amounts[pick] = amount
                    paste_man_HP = 475
                    paste_man_MP = 120
                    choice = False
                    select = False
                    turn = False
                    
                elif type_of_item == A_H:
                    paste_man_HP += 50
                    if paste_man_HP > 475:
                        paste_man_HP = 475
                        print(paste_man_HP)
                    else:
                        print(paste_man_HP)
                    choice = False
                    select = False
                    turn = False
            else:
                print("Not enough of that item")
        else:
            print("That wasn't an option")
    return paste_man_HP, item_amounts, turn, paste_man_MP

    
def rules():
    print("""Welcome to my Dental RPG battle sim, you'll fight bacteria and infected teeth with a team of characters and attack in turns. You can either
          use all 3 characters by yourself or have some friends play with you, with each of them using a different character.""")

def normal_attack(B_HP, norm):
    '''This code is called if the user chooses to use a normal attack, when this function is called the numbers for the
    normal attack damage for the current character is called so the code can select a random number between the 2 numbers'''
    connect = random.randint(1,5)
    if connect == 5:
        print('miss')
    else:
        print('Hit')
        damage_1 = norm[0]
        damage_2 = norm[1]
        damage_dealt = random.randint(damage_1, damage_2)
        B_HP -= damage_dealt
        print("You dealt {} damage".format(damage_dealt))
    return B_HP

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
                    round(decreased_damage)
                    print(decreased_damage)
                    HP -= decreased_damage
                    print("{} took {} damage".format(char, decreased_damage))
                    enemy_turn = False
                    select = False
                else:
                    HP -= damage_dealt
                    print("{} took {} damage".format(char, damage_dealt))
                    enemy_turn = False
                    select = False
            else:
                print('Miss')
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
                    round(decreased_damage)
                    print(decreased_damage)
                    HP -= decreased_damage
                    print("{} took {} damage".format(char, damage_dealt))
                    enemy_turn = False
                    select = False
                else:
                    HP -= damage_dealt
                    print("{} took {} damage".format(char, damage_dealt))
                    enemy_turn = False
                    select = False
            else:
                print('Miss')
                enemy_turn = False
                select = False

    return HP, enemy_turn
    


def special_attack(letter_of_ATK, name_of_ATK, type_of_ATK, cost_of_ATK, MP, dam, B_HP, buff, turn, next_turn):
    choice = True
    while choice == True:
        for letter, name, type, cost in zip(letter_of_ATK, name_of_ATK, type_of_ATK, cost_of_ATK):
            print("{}, {}, {}, {}".format(letter, name, type, cost))
        print(MP)
        attack = input("Please enter the letter for what attack you want to use or enter 'R' to return to the previous screen").upper()
        if attack == 'R':
            choice = False
        elif attack in letter_of_ATK:
            pick = letter_of_ATK.index(attack)
            result = type_of_ATK[pick]
            if result == ATK:
                required_cost = cost_of_ATK[pick]
                if MP >= required_cost:
                    MP -= required_cost
                    connect = random.randint(1,4)
                    if connect == 1 or connect == 2 or connect == 3:
                        damage_1 = dam[pick + 1][0]
                        damage_2 = dam[pick + 1][1]
                        damage_dealt = random.randint(damage_1, damage_2)
                        print("Hit")
                        B_HP -= damage_dealt
                        print("You dealt {} damage".format(damage_dealt))
                        choice = False
                        turn = False
                        next_turn = True
                            
                    else:
                        print('miss')
                        choice = False
                        turn = False
                        next_turn = True
                        
                elif MP < cost_required:
                    print("Not enough MP")
            elif result == M_ATK:
                required_cost = cost_of_ATK[pick]
                if MP >= required_cost:
                    MP -= required_cost
                    connect = random.randint(1,4)
                    if connect == 1 or connect == 2 or connect == 3:
                        damage_1 = dam[pick + 1][0]
                        damage_2 = dam[pick + 1][1]
                        hits = random.randint(1,5)
                        damage_dealt = random.randint(damage_1, damage_2) * hits
                        print('Hit')
                        print('You attack landed {} times'.format(hits))
                        B_HP -= damage_dealt
                        print("You dealt {} damage".format(damage_dealt))
                        choice = False
                        turn = False
                        next_turn = True
                        
                    else:
                        print('miss')
                        choice = False
                        turn = False
                        next_turn = True
            elif result == BUFF:
                if buff == False:
                    buff = True
                    choice = False
                    turn = False
                    next_turn = True
                elif buff == True:
                    print("Already buffed")
        else:
            print("That wasn't a option")
                
                    
                
                    
        
                
        return B_HP, MP, turn, next_turn, buff
        
def turn_order(paste_man_MP, paste_man_HP, brusher_HP, brusher_MP):
    item_letter = ['A', 'B', 'C', 'D', 'E']
    items_carried = ['Tooth cleaner', 'Mouthwash', 'Mint', 'Gold toothpaste', 'power paste']
    item_types = [H, A_H, F_H, R, MP_R]
    item_amounts = [4, 4, 5, 2, 2]
    paste_man_turn = True
    none = False
    brusher_turn = False
    brusher_buff = False
    enemy_turn = False
    boss = 'Bacteria'
    boss_HP = Bacteria_HP
    boss_max = Bacteria_HP
    boss_attacks = Bacteria_attacks
    boss_damage = Bacteria_damage
    boss_types = Bacteria_types
    while paste_man_HP > 0 or boss_HP > 0:
        while paste_man_turn == True:
            print("HP = {}/475".format(paste_man_HP))
            print("MP = {}/120".format(paste_man_MP))
            print(actions)
            paste_man_block = False
            action = input("Select what action above you want to perform").upper()
            if action == 'A':   # the user wants to use a normal attack
                print('You used a normal attack')
                (boss_HP) = normal_attack(boss_HP, paste_man_normal_attack)
                paste_man_turn = False
                brusher_turn = True
            elif action == 'S': # the user wants to use a special attack
                (boss_HP, paste_man_MP, paste_man_turn, brusher_turn, none) = special_attack(paste_man_letters, paste_man_names, paste_man_types, paste_man_costs, paste_man_MP, paste_man_damage, boss_HP, none, paste_man_turn, brusher_turn)                

            elif action == 'B': # the user wants to block
                print('You chose to block')
                paste_man_block = True
                paste_man_turn = False
                brusher_turn = True

            elif action == 'I': # the user wants to use a item
                (paste_man_HP, brusher_HP, item_amounts, paste_man_turn, brusher_turn, paste_man_MP) = select_item(paste_man_HP, paste_man_MP, paste_man_turn, item_letter, items_carried, item_types, none, item_amounts)
            else:
                print("That wasn't a option")

        if brusher_HP == 0:
            brusher_turn = False
            enemy_turn = True
            print('Brusher is unconcious')
        elif brusher_HP > 0:
            print(brusher_turn)
        while brusher_turn == True: # brusher turn
            brusher_block = False
            print("HP = {}/410".format(brusher_HP))
            print("MP = {}/115".format(brusher_MP))
            print(actions)
            brusher_block = False
            action = input("Select what action above you want to perform").upper()
            if action == 'A':
                print('You used a normal attack')
                (boss_HP) = normal_attack(boss_HP, brusher_normal_attack)
                brusher_turn = False
                enemy_turn = True
            elif action == 'S':
                (boss_HP, brusher_MP, brusher_turn, enemy_turn, brusher_buff) = special_attack(brusher_special_attacks, brusher_special_attack_names, brusher_types, brusher_costs, brusher_MP, brusher_damage, boss_HP, brusher_buff, brusher_turn, enemy_turn)
            elif action == 'B':
                brusher_block = True
                brusher_turn = False
                enemy_turn = True
            elif action == 'I':
                print('Item')
                
        
        # Now it's the enemies turn
        while enemy_turn == True:
            print("{} turn".format(boss))
            print("HP = {}/{}".format(boss_HP, boss_max))
            target = random.choice(team)
            if target == 'paste man':
                (paste_man_HP, enemy_turn) = enemy_attack(boss_attacks, boss_types, boss_damage, paste_man_HP, target, paste_man_block, enemy_turn)
                paste_man_turn = True
                
            
                
                
        
rules()
turn_order(paste_man_MP, paste_man_HP, brusher_HP, brusher_MP)

