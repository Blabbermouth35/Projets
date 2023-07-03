import pygame
import os
import json
import random
import time
import keyboard


def show_popup(message, text_color=(255, 255, 255), border_color=(0, 0, 0), duration=1):
    popup_font = pygame.font.SysFont("Arial", 36)
    popup_text = popup_font.render(message, True, text_color)
    popup_rect = popup_text.get_rect(center=(screen_width // 2, screen_height // 2))
    pygame.draw.rect(screen, border_color, (popup_rect.x - 10, popup_rect.y - 10, popup_rect.width + 20, popup_rect.height + 20))
    screen.blit(popup_text, popup_rect)
    pygame.display.update()
    time.sleep(duration)


def load_existing_save(savefile):
    with open(os.path.join(savefile), 'r+') as file:
        save = json.load(file)
    return save


def write_save(data):
    with open(os.path.join(os.getcwd(), 'save.json'), 'w') as file:
        json.dump(data, file)


def load_save():
    try:
        save = load_existing_save('save.json')
    except:
        save = create_save()
        write_save(save)
    return save


def create_save():
    Player_Attack = random.randint(1, 10)
    Player_Defence = random.randint(1, 10)
    Player_Health = random.randint(50, 70)
    spa = Player_Attack
    spd = Player_Defence
    sph = Player_Health
    save = {'point': 0, 'floor': 0, 'Player_Attack': Player_Attack, 'Player_Defence': Player_Defence, 'Player_Health': Player_Health, 'Lost': 0, 'spd': spd, 'spa': spa, 'sph': sph}
    return save


def Enemy_Stats_Fonc():
    global Enemy_Health
    global Enemy_Attack
    global Enemy_Defence
    Enemy_Attack = random.randint(1, 13) * (save['floor'] * 0.5)
    Enemy_Defence = random.randint(1, 15) * (save['floor'] * 0.5)
    Enemy_Health = random.randint(1, 15) * (save['floor'] * 0.5)
    return Enemy_Attack, Enemy_Health, Enemy_Defence

def reset(save):
    Player_Attack = random.randint(1, 10)
    Player_Defence = random.randint(1, 10)
    Player_Health = random.randint(50, 70)
    spa = Player_Attack
    spd = Player_Defence
    sph = Player_Health
    save = {'point': save['point'], 'floor': 0, 'Player_Attack': Player_Attack, 'Player_Defence': Player_Defence,
            'Player_Health': Player_Health, 'Lost': save['Lost'], 'spd': spd, 'spa': spa, 'sph': sph}
    return save


def enemy_selected_move():
    global Enemy_Health
    if Enemy_Health != 0:
        enemy_percentage = random.randint(1, 100)
        if Enemy_Health <= Enemy_Health / 100 * 20 and enemy_percentage >= 10:
            if random.randint(1, 100) <= 80:
                Enemy_Health += Enemy_Defence
                time.sleep(1)
                show_popup('Enemy Healed')
            else:
                time.sleep(1)
                show_popup('Enemy Tried to Heal')
        else:
            if save['Player_Health'] <= save['Player_Health'] / 100 * 20:
                if enemy_percentage <= 10 and random.randint(1, 100) <= 80:
                    save['Player_Health'] -= Enemy_Attack * 2
                    time.sleep(1)
                    show_popup('Enemy Hit You Hard!')
                elif enemy_percentage >= 10 and random.randint(1, 100) <= 80:
                    save['Player_Health'] -= Enemy_Attack
                    time.sleep(1)
                    show_popup('Enemy Hit You')
                else:
                    time.sleep(1)
                    show_popup('Enemy Missed')
            elif save['Player_Health'] >= save['Player_Health'] / 100 * 20:
                if enemy_percentage <= 30 and random.randint(1, 100) <= 80:
                    save['Player_Health'] -= Enemy_Attack * 2
                    time.sleep(1)
                    show_popup('Enemy Hit You Hard')
                elif 30 < enemy_percentage < 90 and random.randint(1, 100) <= 90:
                    save['Player_Health'] -= Enemy_Attack
                    time.sleep(1)
                    show_popup('Enemy Hit You')
                elif enemy_percentage >= 90 and random.randint(1, 100) <= 95:
                    Enemy_Health += Enemy_Defence
                    time.sleep(1)
                    show_popup('Enemy Healed')
                else:
                    time.sleep(1)
                    show_popup('Enemy Failed')


def level_up():
    save['Player_Health'] = save['sph'] + save['floor'] * 3
    save['Player_Attack'] = save['spa'] + save['floor'] * 3
    save['Player_Defence'] = save['spd'] + save['floor'] * 3


pygame.init()
screen_width = 600
screen_height = 400
clock = pygame.time.Clock()
pygame.display.set_caption('Turn Based RPG')
font = pygame.font.SysFont("Arial", 24)

screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)

load_save()
with open('save.json', 'r') as file:
    save = json.load(file)

Enemy_Health = 0
Enemy_Defence = 0
Enemy_Attack = 0

Enemy_Stats_Fonc()
show_popup('a: attack s: strong attack, likely to miss d: heal')
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            screen_width, screen_height = event.size
            screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
        if keyboard.is_pressed('a'):
            percentage = random.randint(1, 100)
            if percentage <= 80:
                Enemy_Health -= save['Player_Attack']
                show_popup('Successful Attack')
                enemy_selected_move()
            else:
                show_popup('Missed')
                enemy_selected_move()
        if keyboard.is_pressed('s'):
            percentage = random.randint(1, 100)
            if percentage <= 40:
                Enemy_Health -= (save['Player_Attack'] * 4) - Enemy_Defence
                show_popup('Successful Strong Attack')
                show_popup("                                             ", (100, 128, 255), (100, 128, 255), 0.3)
                enemy_selected_move()
            else:
                show_popup('Missed')
                enemy_selected_move()
        if keyboard.is_pressed('d'):
            percentage = random.randint(1, 100)
            if percentage <= 60:
                save['Player_Health'] += save['Player_Defence']
                show_popup('Successfully healed')
                enemy_selected_move()
            else:
                show_popup("Didn't Worked")
                enemy_selected_move()
        if keyboard.is_pressed("p"):
            save = reset(save)
    screen.fill((100, 128, 255))
    player_info_lines = [
        "Player",
        f"High Score: {save['point']}",
        f"Floor: {save['floor']}",
        f"Attack: {save['Player_Attack']}",
        f"Defence: {save['Player_Defence']}",
        f"Health: {save['Player_Health']}",
        f"Losses: {save['Lost']}"
    ]

    # noinspection PyUnboundLocalVariable
    enemy_info_lines = [
        "Enemy",
        f"Health: {Enemy_Health}"
    ]

    y_offset = 0

    for i, line in enumerate(player_info_lines):
        line_surface = font.render(line, True, (0, 0, 0))
        screen.blit(line_surface, (10, y_offset + (i * 30)))
    for i, line in enumerate(enemy_info_lines):
        enemy_line_surface = font.render(line, True, (0, 0, 0))
        screen.blit(enemy_line_surface, (screen_width - enemy_line_surface.get_width() - 5, y_offset + (i * 30)))

    if Enemy_Health <= 0:
        if save['point'] == save['floor']:
            save['point'] += 1
        save['floor'] += 1
        show_popup('You have won!')
        level_up()
        Enemy_Stats_Fonc()
    if save['Player_Health'] <= 0:
        show_popup('You have lost')
        save['Lost'] += 1
        save = reset(save)


    pygame.display.flip()



with open('save.json', 'w') as file:
    json.dump(save, file)

pygame.quit()
