from RPG_inventory_demoV2 import inventory
import random

a = "Rusty Shield"
b = "Not Rusty Sword"
c = "Mana Potion"
d = "Rusty Sword"
for i in range(2):
    print(" ")
print("You left the chest behind and continued down the path. But all of a sudden an enemy jumps in front of you.")
player_stat_attack = random.randint(1, 10)
player_stat_defence = random.randint(1, 10)
enemy_stat_attack = random.randint(1, 13)
enemy_stat_defence = random.randint(1, 15)
floor = 1
weapons_stats = {"Rusty sword": 1, "Not Rusty Sword": 3, "Rusty Shield": 5}
point = 0
final_player_stat_attack = player_stat_attack


def final_stat_attack(x):
    global final_player_stat_attack
    if x in inventory:
        final_player_stat_attack = player_stat_attack + weapons_stats[x]
    return final_player_stat_attack


def final_stat_defence(x):
    global final_player_stat_defence
    if x in inventory:
        final_player_stat_defence = player_stat_defence + weapons_stats[x]
        return final_player_stat_defence
    else:
        final_player_stat_defence = player_stat_defence
        return final_player_stat_defence


if a in inventory:
    final_player_stat_defence = final_stat_defence(a)
if b in inventory:
    final_player_stat_attack = final_stat_attack(b)
if d in inventory:
    final_player_stat_attack = final_stat_attack(d)
final_player_stat_defence = player_stat_defence
enemy_health = 50 + enemy_stat_defence
player_health = 50 + final_player_stat_defence
player_actions = {1: 3, 2: 8, 3: 3}
enemy_actions = {1: 3, 2: 8, 3: 3}
enemy_acts = [1, 2, 3]


def enemy_action_output(x):
    global player_selected_move
    global player_health
    if x == 1:
        p = random.randint(1, 100)
        if p <= 75:
            if player_selected_move == 3:
                player_health = player_health + 3
            player_health = player_health - (enemy_stat_attack + 3)
            print("successful hit from the enemy")
            return player_health
        else:
            print("The enemy has missed")
    elif x == 2:
        p = random.randint(1, 100)
        if p <= 45:
            if player_selected_move == 3:
                player_health = player_health + 3
            player_health = player_health - (enemy_stat_attack + 8)
            print("successful hit from the enemy")
            return player_health
        else:
            print("The enemy has missed")
    else:
        print("The enemy has changed their stance to a more defensive one")


def player_action_output(x):
    global enemy_selected_move
    global enemy_health
    if x == 1:
        p = random.randint(1, 100)
        if p <= 90:
            if enemy_selected_move == 3:
                enemy_health = enemy_health + 3
                print("The enemy's defence has risen for 1 turn")
            enemy_health = enemy_health - (final_player_stat_attack + 3)
            print("A successful hit")
            return enemy_health
        else:
            print("the enemy has dodged the attack")
    elif x == 2:
        p = random.randint(1, 100)
        if p <= 45:
            if enemy_selected_move == 3:
                enemy_health = enemy_health + 3
                print("The enemy's defence has risen for 1 turn")
            enemy_health = enemy_health - (final_player_stat_attack + 8)
            print("A successful hit")
            return enemy_health
        else:
            print("The enemy has dodged your attack")
    else:
        print("You got ready to react to the enemy's attack")


while player_health > 0:
    while enemy_health > 0 or player_health > 0:
        enemy_selected_move = random.randint(1, 100)
        player_selected_move = int(input(
            "Select your move (stronger moves miss more frequently) \n weak attack (1), strong attack (2), "
            "weak defence (3): "))
        player_action_output(player_selected_move)
        if enemy_selected_move <= 60:
            enemy_action_output(1)
        elif 60 < enemy_selected_move <= 80:
            enemy_action_output(2)
        elif 80 < enemy_selected_move <= 100:
            enemy_action_output(3)
        print("enemy health: " + str(enemy_health))
        print("player health: " + str(player_health))
        if enemy_health <= 0 < player_health:
            print("You have won")
            point = int(point) + 1
            break
        elif player_health <= 0:
            print("You have lost")
            break
        else:
            continue
    if player_health <= 0:
        if "Mana Potion" in inventory:
            del (inventory["Mana Potion"])
        else:
            break
    floor = int(floor) + 1
    enemy_health = (50 + enemy_stat_defence) * (floor * 0.5)
    enemy_stat_attack = enemy_stat_attack * (floor * 0.5)
    enemy_stat_defence = enemy_stat_defence * (floor * 0.5)
    upgrade = input(
        "You have won and the gods grants you a wish. You may upgrade one of your stats. \n Health (a) Attack (b) "
        "Defence (c):")
    if upgrade == "b":
        upgrade_b = random.randint(1, 100)
        if upgrade_b <= 20:
            final_player_stat_attack = final_player_stat_attack + 1
        elif 70 > upgrade_b > 20:
            final_player_stat_attack = final_player_stat_attack + 3
        elif 70 < upgrade_b <= 100:
            final_player_stat_attack = final_player_stat_attack + 5
    elif upgrade == "c":
        upgrade_c = random.randint(1, 100)
        if upgrade_c <= 20:
            final_player_stat_defence = final_player_stat_defence + 1
        elif 70 > upgrade_c > 20:
            final_player_stat_defence = final_player_stat_defence + 3
        elif 70 < upgrade_c <= 100:
            final_player_stat_defence = final_player_stat_defence + 5
    else:
        player_health = 50 + final_player_stat_defence + 10
    print("Current score: " + str(point))
    print("current floor: " + str(floor))
