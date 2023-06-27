import pygame
from pygame.locals import *
import json
import os
import time


# save data handling


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
    save = {'score': 0, 'ClickingPower': 1, 'IdleScore': 0}
    return save


last_score_update_time = time.time()
idle_score_interval = 2
# game init

pygame.init()
screen = pygame.display.set_mode((400, 300))
screen_width = 400
screen_height = 300
clock = pygame.time.Clock()
pygame.display.set_caption('Clicker Game')

def draw_button():
    pygame.draw.rect(screen, (0, 0, 0), button_rect)
    screen.blit(button_text, button_text_rect)
    pygame.draw.rect(screen, (0, 0, 0), CP_button_rect)
    screen.blit(CP_button_text, CP_button_text_rect)


def show_popup(message):
    popup_font = pygame.font.Font(None, 36)
    popup_text = popup_font.render(message, True, (255, 255, 255))
    popup_rect = popup_text.get_rect(center=(screen_width // 2, screen_height // 2))
    pygame.draw.rect(screen, (0, 0, 0), (popup_rect.x - 10, popup_rect.y - 10, popup_rect.width + 20, popup_rect.height + 20))
    screen.blit(popup_text, popup_rect)
    pygame.display.update()
    time.sleep(3)


button_font = pygame.font.Font(None, 30)
button_text = button_font.render("Click me!", True, (255, 255, 255))
button_text_rect = button_text.get_rect(center=screen.get_rect().center)
button_rect = button_text_rect.inflate(10, 10)

CP_button_font = pygame.font.Font(None, 30)
CP_button_text = CP_button_font.render("Clicking Power +", True, (255, 255, 255))
CP_button_text_rect = CP_button_text.get_rect(bottomleft=(10, screen.get_height() - 24))
CP_button_rect = CP_button_text_rect.inflate(15, 15)


load_save()
with open('save.json', 'r') as file:
    save = json.load(file)

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                save['score'] += 1 * save['ClickingPower']
                print("Button clicked! Score:", save['score'])
            elif CP_button_rect.collidepoint(event.pos):
                if save['score'] >= save['ClickingPower'] * 5:
                    save['score'] -= save['ClickingPower'] * 5
                    save['ClickingPower'] += 1
                else:
                    show_popup("Score Must Be More Than CP * 5")
    if time.time() - last_score_update_time >= idle_score_interval:
        save['score'] += save['IdleScore']
        last_score_update_time = time.time()

    screen.fill((0, 128, 255))
    draw_button()
    font = pygame.font.SysFont("Arial", 24)
    score_text = font.render("Score: {}".format(save['score']), True, (0, 0, 0))
    screen.blit(score_text, (10, 0))
    CP_font = pygame.font.SysFont("Arial", 24)
    CP_text = CP_font.render("Clicking Power: {}".format(save['ClickingPower']), True, (0, 0, 0))
    screen.blit(CP_text, (400 - CP_text.get_width() - 5, 0))
    pygame.display.flip()
    clock.tick(60)

data = {"score": save['score'], "ClickingPower": save['ClickingPower'], "IdleScore": save["IdleScore"]}
with open('save.json', 'w') as file:
    json.dump(data, file)

pygame.quit()
