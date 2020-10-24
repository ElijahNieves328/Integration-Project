# Elijah Nieves
# Text Adventure
# This project is a text based adventure where you are a knight travelling
# through a dangerous forest.
# You must fight your way through the forest, gaining strength and items
# throughout the process.

import random

import sys


###Creating all the simple, convenient functions

def prompt_to_proceed():
    input(">Press Enter to proceed<")
    # this is on a function because this will be used very often to introduce
    # smaller bits of information at a time. its annoying to retype.


def get_sword_damage():
    return random.randint(8, 12)


def get_flame_damage():
    return random.randint(5, 8)


####Found on https://thispointer.com/python-how-to-convert-a-list-to-string/
###we are using this function to print the valid_actions_string list
def convert_list_to_string(list_variable, separator):
    ###Convert list to string, by joining all items in list with given
    # separator. Returns the concatenated string
    return separator.join(list_variable)


def print_file_text(file, start_line, end_line):
    for line in range(start_line, end_line):
        print(file.readline().rstrip())


def seek_line(file, line_number):
    file.seek(0)
    for line in range(line_number):
        file.readline()


def print_combat_string(actor, action, target):
    combat_strings = open('resources/combat_text.txt', 'r')
    if actor == "player":
        if action == "attack" or action == "smite":
            if target == "Slime":
                combat_strings.readline()
                print(combat_strings.readline().rstrip())
            elif target == "Ent":
                for line in range(5):
                    combat_strings.readline()
                print(combat_strings.readline().rstrip())
            elif target == "Lich":
                for line in range(12):
                    combat_strings.readline()
                print(combat_strings.readline().rstrip())
            elif target == "Horde":
                for line in range(11):
                    combat_strings.readline()
                print(combat_strings.readline().rstrip())
            else:
                print("print_combat_string player attack ERROR")
        elif action == "flame":
            if target == "Slime":
                for line in range(2):
                    combat_strings.readline()
                print(combat_strings.readline().rstrip())
            elif target == "Ent":
                for line in range(6):
                    combat_strings.readline()
                print(combat_strings.readline().rstrip())
            elif target == "Lich":
                for line in range(14):
                    combat_strings.readline()
                print(combat_strings.readline().rstrip())
            elif target == "Horde":
                for line in range(13):
                    combat_strings.readline()
                print(combat_strings.readline().rstrip())
            else:
                print("print_combat_string player flame ERROR")
        elif action == "faerie fire":
            if target == "Ent":
                for line in range(7):
                    combat_strings.readline()
                print(combat_strings.readline().rstrip())
            elif target == "Lich":
                for line in range(16):
                    combat_strings.readline()
                print(combat_strings.readline().rstrip())
            elif target == "Horde":
                for line in range(15):
                    combat_strings.readline()
                print(combat_strings.readline().rstrip())
            else:
                print("print_combat_string player faerie fire ERROR")
        elif action == "heal":
            print("You channel your magic to mend your wounds.")
        elif action == "block":
            print("You raise your shield, preparing for an attack.")
        else:
            print("print_combat_string player INVALID ACTION ERROR")

    elif actor == "Slime":
        if action == "attack":
            for line in range(3):
                combat_strings.readline()
            print(combat_strings.readline().rstrip())
        else:
            print("print_combat_string slime action ERROR")
    elif actor == "Ent":
        if action == "wind up":
            for line in range(8):
                combat_strings.readline()
            print(combat_strings.readline().rstrip())
        elif action == "attack":
            for line in range(9):
                combat_strings.readline()
            print(combat_strings.readline().rstrip())
        else:
            print("print_combat_string ent action ERROR")
    elif actor == "Lich":
        if action == "summon":
            for line in range(17):
                combat_strings.readline()
            print(combat_strings.readline().rstrip())
        elif action == "attack":
            for line in range(18):
                combat_strings.readline()
            print(combat_strings.readline().rstrip())
        else:
            print("print_combat_string Lich action ERROR")
    elif actor == "Horde":
        for line in range(19):
            combat_strings.readline()
        print(combat_strings.readline().rstrip())
    elif actor == "fairies":
        if action == "attack":
            for line in range(20):
                combat_strings.readline()
            print(combat_strings.readline().rstrip())
        if action == "heal":
            for line in range(21):
                combat_strings.readline()
            print(combat_strings.readline().rstrip())
            print(combat_strings.readline().rstrip())
    combat_strings.seek(0)  # returns back to the top of the txt file


### Also initializing functions and variables player does not have yet.
###This is so we can use one singular combat results function while redefining
### the combat options list as the player gets more options.

def get_ffire_damage():
    return random.randint(10, 14)


def get_heal_amount():
    return random.randint(10, 12)


def get_block(enemy_damage_value, enemy, armor_value):
    damage_value = enemy_damage_value % armor_value
    if damage_value < 1:
        damage_value = 1
        ####it will always do some damage. no "enemy takes 0 damage"
    #####else: proceed as normal
    print("You block the attack, taking minimal damage!")
    print("Energy is reflected back towards the {}!".format(enemy))
    print("The {} takes {} damage!".format(enemy, damage_value))
    return damage_value


###### Now creating base combat functions needed throughout the program
def check_valid_actions(action, actions_string, valid_actions, mp):
    # makes sure a valid action is sent to the combat results function.
    # valid_actions is being used as a parameter because it will be updated
    # and changed multiple times throughout the main() function
    # actions_string is a parameter here so we can pass that variable to
    # ask_combat_actions() if needed
    if action not in valid_actions:
        print("Please select a valid action.")
        return ask_combat_actions(actions_string, valid_actions, mp)
    if mp < get_spell_cost(action):
        print("Insufficient mana!")
        return ask_combat_actions(actions_string, valid_actions, mp)
    else:
        return action


def ask_combat_actions(actions_string, valid_actions, mp):
    # actions_string is being used as a parameter because it will be updated
    # and changed multiple times throughout the main() function
    # valid actions is a parameter here so we can pass that variable to
    # check_valid_actions()
    print("What do you do?\n" + convert_list_to_string(actions_string, "\t"))
    action = input().lower()
    # learned that .lower makes things easier to read from w3schools
    action = check_valid_actions(action, actions_string, valid_actions, mp)
    return action


def choose_target(action):
    if action == "block" or action == "heal":
        return "Lich"
        #######it doesnt matter what we return if it is non-damaging
    else:
        enemy = input("Who would you like to attack? ").lower()
        if enemy != "lich" and enemy != "horde":
            if enemy == "fairies":
                print("Fairies are too small to attack.")
            print("Please choose a valid target.")
            choose_target(action)
        else:
            enemy = enemy.capitalize()
            ##learned from w3schools
            return enemy


def print_damage_dealt(damage_value):
    print("You do {} damage!".format(damage_value))


def print_damage_taken(damage_value):
    print("You take {} damage!".format(damage_value))


def do_player_turn(action, enemy):
    print_combat_string("player", action, enemy)
    if enemy == "Slime":
        if action == "attack":
            damage_value = round(get_sword_damage() / 2)
            print_damage_dealt(damage_value)
            return damage_value
        elif action == "flame":
            damage_value = get_flame_damage() * 2
            print_damage_dealt(damage_value)
            return damage_value
        else:
            print("Player turn action ERROR. Invalid action")
    else:
        if action == "attack":
            damage_value = get_sword_damage()
            print_damage_dealt(damage_value)
            return damage_value
        elif action == "flame":
            damage_value = get_flame_damage()
            print_damage_dealt(damage_value)
            return damage_value
        elif action == "faerie fire":
            damage_value = get_ffire_damage()
            print_damage_dealt(damage_value)
            return damage_value
        elif action == "block":
            return 0
        elif action == "heal":
            return "heal"
        elif action == "smite":
            damage_value = get_sword_damage() ** 2
            print_damage_dealt(damage_value)
            return damage_value
        else:
            print("Player turn action ERROR. Invalid action")


def get_spell_cost(action):
    flame_cost = 3
    ffire_cost = 6
    heal_cost = 6
    if action == "flame":
        return flame_cost
    elif action == "faerie fire":
        return ffire_cost
    elif action == "heal":
        return heal_cost
    else:  # if action is not a spell, no mp is drained
        return 0


def get_enemy_damage(num1, num2):
    return random.randint(num1, num2)


def do_enemy_turn(action, enemy, armor_value, cycle):
    if enemy == "Slime":
        print_combat_string("Slime", "attack", "player")
        damage_value = (get_enemy_damage(5, 8) - armor_value)
        # reduced the damage by the armor value
        print_damage_taken(damage_value)
        return damage_value
    elif enemy == "Ent":
        if cycle == 0:
            print_combat_string(enemy, "wind up", "player")
            return 0
        else:
            print_combat_string(enemy, "attack", "player")
            if action == "block":
                enemy_damage_value = get_enemy_damage(10, 14)
                damage_value = enemy_damage_value // armor_value
                return damage_value
            else:
                damage_value = get_enemy_damage(10, 14)
                return damage_value
    elif enemy == "Lich":
        if cycle == 0:
            print_combat_string(enemy, "summon", "player")
            return 0
        else:
            print_combat_string(enemy, "attack", "player")
            if action == "block":
                if armor_value > 3:
                    enemy_damage_value = get_enemy_damage(8, 14)
                    damage_value = enemy_damage_value // (armor_value ** 2)
                    return damage_value
                else:
                    enemy_damage_value = get_enemy_damage(8, 14)
                    damage_value = enemy_damage_value // armor_value
                    return damage_value
            else:
                damage_value = get_enemy_damage(8, 14)
                return damage_value
    elif enemy == "Horde":
        print_combat_string(enemy, "attack", "player")
        if action == "block":
            if armor_value > 3:
                enemy_damage_value = get_enemy_damage(1, 3)
                damage_value = enemy_damage_value // (armor_value ** 2)
                return damage_value
            else:
                enemy_damage_value = get_enemy_damage(1, 3)
                damage_value = enemy_damage_value // armor_value
                return damage_value
        else:
            damage_value = get_enemy_damage(1, 3)
            return damage_value
    elif enemy == "fairies":
        if action == "attack":
            print_combat_string(enemy, "attack", "player")
            print("The fairies are too small to block!")
            print("You take 1 damage!\n" * 5)
            damage_value = 5
            return damage_value
        elif action == "heal":
            print_combat_string(enemy, "heal", "player")
        else:
            print("no valid fairy action")

    else:
        print("INVALID ENEMY")


def damage_over_time(dot_fire, dot_ffire, enemy):
    damage_value = 0
    if dot_fire == 1:
        damage_value = 3
        print("The {} burns! They take {} damage!".format(enemy, damage_value))
    elif dot_ffire > 0:
        damage_value += (dot_ffire * 3)
        print("The {} burns! They take {} damage from Faerie Fire!".format(
            enemy, damage_value))
    ###else: damage value remains 0.
    return damage_value


######## Game over sequence ##########
def game_over(enemy):
    game_over_strings = open('resources/game_overs.txt', 'r')
    if enemy == "Slime":
        seek_line(game_over_strings, 1)
        print_file_text(game_over_strings, 2, 5)
    elif enemy == "Ent":
        seek_line(game_over_strings, 5)
        print_file_text(game_over_strings, 6, 9)
    elif enemy == "lich":
        seek_line(game_over_strings, 9)
        print_file_text(game_over_strings, 10, 18)
    else:
        print("Game over error. No existing game over message.")
    sys.exit("GAME OVER")


###############################MAIN CODE######################################
def main():
    #####initializing variables########
    maxhp = 24
    hp = 24  # health. if it reaches 0, game over

    maxmp = 12
    mp = 12  # magic points. used to cast magic

    armor_value = 3  # armor reduces incoming damage by said amount

    sword_string = "(8-12 slashing damage)"
    flame_string = "(5-8 fire damage, 3 MP)"
    ffire_string = "(10-14 fire damage, 6 MP)"
    heal_string = "(10-12 HP, 6 MP)"

    ######the lists below will be updated when the player learns new actions

    actions_string = ["Attack" + sword_string, "Flame" + flame_string]
    # the concatenated strings tell the player what the actions does
    valid_actions = ["attack", "flame"]

    main_text = open('resources/noncombat_text.txt', 'r')
    ############INTRO#############
    main_text.readline()
    for line in range(4):
        print(main_text.readline().rstrip())
    prompt_to_proceed()
    answer = input(
        "Would you like an explanation of the stats and mechanics? ").lower()
    if answer == "yes":
        main_text.readline()
        print_file_text(main_text, 7, 9)
        print(main_text.readline().rstrip().format(maxhp))
        # to format the variables in, I have to break out of the print file
        # function
        print_file_text(main_text, 10, 11)
        prompt_to_proceed()
        print_file_text(main_text, 11, 12)
        print(main_text.readline().rstrip().format(maxmp))
        print_file_text(main_text, 13, 14)
        print(main_text.readline().rstrip().format(flame_string))
        print_file_text(main_text, 15, 16)
        prompt_to_proceed()
        print_file_text(main_text, 16, 18)
        print(main_text.readline().rstrip().format(armor_value))
        print(main_text.readline().rstrip().format(sword_string))
    else:
        print("HP: {} \nMP: {} \nArmor: {}".format(hp, mp, armor_value))
    prompt_to_proceed()

    ########################COMBAT 1##################################
    seek_line(main_text, 20)
    print_file_text(main_text, 21, 24)
    prompt_to_proceed()
    print_file_text(main_text, 24, 27)

    slime_hp = 34
    enemy = "Slime"
    while slime_hp > 0:
        print("You have {} HP and {} MP.".format(hp, mp))
        action = ask_combat_actions(actions_string, valid_actions, mp)
        damage_value = do_player_turn(action, enemy)
        mp -= get_spell_cost(action)
        slime_hp -= damage_value
        print("The Slime now has {} HP".format(slime_hp))
        prompt_to_proceed()
        if slime_hp > 0:  # slime can't act after it is dead
            hp -= do_enemy_turn(action, enemy, armor_value, 0)
            prompt_to_proceed()
        ###else, proceed to top of while loop to end combat
        if hp <= 0:
            game_over(enemy)
        ###else, proceed to top of while loop to continue combat
    mp = maxmp
    seek_line(main_text, 26)
    print_file_text(main_text, 27, 31)
    prompt_to_proceed()
    print_file_text(main_text, 31, 34)
    actions_string.append("Block")
    valid_actions.append("block")
    prompt_to_proceed()

    #####################FAIRY FOUNTAIN##################################
    seek_line(main_text, 34)
    print_file_text(main_text, 35, 41)
    fairy_event = 0
    ####variable that dictates end of the event
    fairy_hate = 0
    fairy_help = 0
    ####these two variables will affect the story later on if their value is 1.
    action = 0
    while fairy_event != 1:
        action = input().lower()
        if action == "drink":
            hp = maxhp
            print_file_text(main_text, 41, 42)
            print(main_text.readline().rstrip().format(hp))
            print_file_text(main_text, 43, 46)
            actions_string.append("Heal" + heal_string)
            valid_actions.append("heal")
            fairy_event = 1
        elif action == "bathe":
            fairy_hate = 1
            maxhp *= 3
            hp = maxhp
            seek_line(main_text, 45)
            print_file_text(main_text, 46, 49)
            print(main_text.readline().rstrip().format(maxhp))
            fairy_event = 1
        elif action == "leave":
            fairy_help = 1
            maxmp *= 2
            mp = maxmp
            hp = maxhp
            seek_line(main_text, 49)
            print_file_text(main_text, 50, 51)
            print(main_text.readline().rstrip().format(maxmp))
            print_file_text(main_text, 52, 54)
            actions_string[1] = "Faerie Fire" + ffire_string
            valid_actions[1] = "faerie fire"
            fairy_event = 1
        else:
            print("Invalid action. Please select a valid action")
    print("You leave the fountain behind", end="")
    if action == "bathe":
        print(", but the fairies seem to despise you now.")
    elif action == "drink":
        print(" feeling replenished.")
    elif action == "leave":
        print(", having made new tiny allies")
    else:
        print(", with and error message")
    prompt_to_proceed()

    ###########################ENT FIGHT#################################
    seek_line(main_text, 54)
    print_file_text(main_text, 55, 57)
    prompt_to_proceed()
    print_file_text(main_text, 57, 59)

    ent_hp = 54
    enemy = "Ent"
    dot_fire = 0
    dot_ffire = 0
    cycle = 0
    while ent_hp > 0:
        print("You have {} HP and {} MP.".format(hp, mp))
        action = ask_combat_actions(actions_string, valid_actions, mp)
        damage_value = do_player_turn(action, enemy)
        mp -= get_spell_cost(action)
        if damage_value == "heal":
            health_gained = get_heal_amount()
            if (health_gained + hp) > maxhp:
                health_gained = (maxhp - hp)
                print("You heal to maximum HP.")
                hp += health_gained
            else:
                print("You regain {} HP.".format(health_gained))
                hp += health_gained
            damage_value = 0
        # else continue as normal
        if action == "flame" or action == "faerie fire":
            if dot_fire == 0 and dot_ffire == 0:
                print("The Ent bursts into flames!")
            # else do not print statement
        # else continue as normal
        if action == "flame" and dot_fire == 0:
            dot_fire = 1
        elif action == "faerie fire":
            dot_ffire += 1
        # else no damage over time accumulates
        damage_value += damage_over_time(dot_fire, dot_ffire, enemy)
        ent_hp -= damage_value
        print("The Ent now has {} HP".format(ent_hp))
        prompt_to_proceed()
        if ent_hp > 0:
            if cycle == 0:
                cycle = 1
                enemy_damage_value = do_enemy_turn(action, enemy,
                                                   armor_value, cycle)
                if action == "block":
                    ent_hp -= get_block(enemy_damage_value, enemy, armor_value)
                print("You take {} damage.".format(enemy_damage_value))
                hp -= enemy_damage_value
            else:
                cycle = 0
                do_enemy_turn(action, enemy, armor_value, cycle)
            prompt_to_proceed()
        ###else, proceed to top of while loop to end combat
        if hp <= 0:
            game_over(enemy)
        ###else, proceed to top of while loop to continue combat
    ######print victory and proceed to next event
    if dot_fire > 0:
        seek_line(main_text, 58)
        print_file_text(main_text, 59, 60)
    elif dot_ffire > 0:
        seek_line(main_text, 59)
        print_file_text(main_text, 60, 61)
    else:
        seek_line(main_text, 60)
        print_file_text(main_text, 61, 63)
    mp = maxmp
    seek_line(main_text, 62)
    print_file_text(main_text, 63, 64)
    prompt_to_proceed()

    #########################SWORD OR HELM###############################
    sword_event = 0
    seek_line(main_text, 64)
    print_file_text(main_text, 65, 68)
    prompt_to_proceed()
    print_file_text(main_text, 68, 71)
    while sword_event != 1:
        answer = input().lower()
        if answer == "helm":
            seek_line(main_text, 70)
            print_file_text(main_text, 71, 74)
            prompt_to_proceed()
            armor_value = 6
            ####the additional effect of the helm is already handled in
            # the enemy turn function
            print(main_text.readline().rstrip().format(armor_value))
            print_file_text(main_text, 75, 77)
            sword_event = 1
            prompt_to_proceed()
        elif answer == "sword":
            seek_line(main_text, 76)
            print_file_text(main_text, 77, 83)
            answer = input().lower()
            if answer == "yes":
                maxmp = 0
                mp = maxmp
                actions_string[0] = "Smite"
                valid_actions[0] = "smite"
                print_file_text(main_text, 83, 87)
                sword_event = 1
                prompt_to_proceed()
            else:
                print("Which item do you want to take with you?")
        else:
            print("Please select an item")

    ###############################LICH FIGHT################################
    seek_line(main_text, 87)
    print_file_text(main_text, 88, 91)
    prompt_to_proceed()
    print_file_text(main_text, 91, 94)
    prompt_to_proceed()
    print_file_text(main_text, 94, 98)
    dot_fire = 0
    #####these are non flammable enemies
    enemy = "Lich"
    lich_hp = 150
    horde_hp = 75  # i am calculating the whole horde's hp as one, but...
    zombies = horde_hp // 15
    # depending on how much hp the horde has, it will have a certain  amount
    # of zombies.
    # this determines how many attacks the horde can make.
    # each zombie has 15 health
    lich_ffire = 0
    # only have the faerie fire counter here because normal fire will not
    # do any damage over time
    horde_ffire = 0  
    cycle = 0  # lich will cycle between summoning zombies (0) and
    # casting spells (1)
    while lich_hp > 0:
        print("You have {} HP and {} MP.".format(hp, mp))
        action = ask_combat_actions(actions_string, valid_actions, mp)
        enemy = choose_target(action)
        damage_value = do_player_turn(action, enemy)
        mp -= get_spell_cost(action)
        if damage_value == "heal":
            health_gained = get_heal_amount()
            if (health_gained + hp) > maxhp:
                health_gained = (maxhp - hp)
                hp += health_gained
                print("You heal to maximum HP.")
            else:
                print("You regain {} HP.".format(health_gained))
                hp += health_gained
            damage_value = 0
        if enemy == "Lich":
            if action == "faerie fire":
                lich_ffire += 1
            lich_hp -= damage_value
        elif enemy == "Horde":
            if action == "faerie fire":
                horde_ffire += 1
            horde_hp -= damage_value
        lich_hp -= damage_over_time(0, lich_ffire, "Lich")
        horde_hp -= damage_over_time(0, horde_ffire, "Horde")
        zombies = horde_hp // 15
        print("There are {} undead left.".format(zombies))
        print("The Lich now has {} HP".format(lich_hp))
        prompt_to_proceed()
        if fairy_hate == 1:
            enemy_damage_value = do_enemy_turn("attack", "fairies", 0, 0)
            print("You take {} damage.".format(enemy_damage_value))
            hp -= enemy_damage_value
            prompt_to_proceed()
        if lich_hp > 0:
            enemy_damage_value = do_enemy_turn(action, "Horde", armor_value,
                                               cycle) * zombies
            if action == "block":
                horde_hp -= get_block(enemy_damage_value, "Horde", armor_value)
            print("You take {} damage.".format(enemy_damage_value))
            hp -= enemy_damage_value
            if cycle == 1:
                enemy_damage_value = do_enemy_turn(action, "Lich",
                                                   armor_value, cycle)
                cycle = 0
                if action == "block":
                    lich_hp -= get_block(enemy_damage_value, "Lich",
                                         armor_value)
                print("You take {} damage.".format(enemy_damage_value))
                hp -= enemy_damage_value
            else:
                do_enemy_turn(action, enemy, armor_value, cycle)
                horde_hp += (15 * 5)
                zombies += 5
                cycle = 1
            prompt_to_proceed()
        if hp <= 10 and fairy_help == 1:
            do_enemy_turn("heal", "fairies", 0, 0)
            maxhp += 50
            hp = maxhp
            fairy_help = 0
        if hp <= 0:
            game_over(enemy)

    #############################VICTORY######################################
    seek_line(main_text, 97)
    print_file_text(main_text, 98, 100)
    prompt_to_proceed()
    print_file_text(main_text, 100, 104)
    prompt_to_proceed()
    print_file_text(main_text, 104, 106)
    print("G A M E  O V E R")
    sys.exit()


main()
