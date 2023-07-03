import pygame
import os
import json
import random
import time


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
    save = {'point': 0, 'floor': 0, 'Player_Attack': Player_Attack, 'Player_Defence': Player_Defence, 'Player_Health': Player_Health}
    return save


def Enemy_Stats_Fonc():
    global Enemy_Health
    global Enemy_Attack
    global Enemy_Defence
    Enemy_Attack = random.randint(1, 13) * (save['floor'] * 0.5)
    Enemy_Defence = random.randint(1, 15) * (save['floor'] * 0.5)
    Enemy_Health = random.randint(1, 15) * (save['floor'] * 0.5)
    return Enemy_Attack, Enemy_Health, Enemy_Defence


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


Enemy_Stats_Fonc()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            screen_width, screen_height = event.size
            screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
    screen.fill((100, 128, 255))
    player_info_lines = [
        "Player",
        f"Point: {save['point']}",
        f"Floor: {save['floor']}",
        f"Attack: {save['Player_Attack']}",
        f"Defence: {save['Player_Defence']}",
        f"Health: {save['Player_Health']}"
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

    time.sleep(1)
    Enemy_Health -= 10
    if Enemy_Health <= 0:
        save['point'] += 1
        save['floor'] += 1
        Enemy_Stats_Fonc()

    pygame.display.flip()


data = {"point": save['point'], "floor": save['floor'], "Player_Attack": save["Player_Attack"],
        'Player_Defence': save['Player_Defence'], 'Player_Health': save['Player_Health']}

with open('save.json', 'w') as file:
    json.dump(data, file)

pygame.quit()
