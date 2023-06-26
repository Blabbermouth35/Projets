import pygame
from pygame.locals import *
import json
import os


# save data handling
with open('save.json', 'r') as file:
    save = json.load(file)


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
    save = {'score': 0}  # Initialize save with a score of 0
    return save


# game init

pygame.init()
screen = pygame.display.set_mode((400, 300))
clock = pygame.time.Clock()


def draw_button():
    pygame.draw.rect(screen, (0, 128, 255), button_rect)
    screen.blit(button_text, button_text_rect)


button_font = pygame.font.Font(None, 30)
button_text = button_font.render("Click me!", True, (255, 255, 255))
button_text_rect = button_text.get_rect(center=screen.get_rect().center)
button_rect = button_text_rect.inflate(10, 10)

load_save()

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                save['score'] += 1
                print("Button clicked! Score:", save['score'])
    screen.fill((255, 255, 255))
    draw_button()
    pygame.display.flip()
    clock.tick(60)

data = {"score": save['score']}
with open('save.json', 'w') as file:
    json.dump(data, file)

pygame.quit()
