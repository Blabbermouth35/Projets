import pygame
from pygame.locals import *
import json
import os
import time
import keyboard
import random


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
    save = {'highscore': 0}
    return save


class Sprite(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // 8, self.image.get_height() // 8))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x_velocity = 0
        self.y_velocity = 0
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        # Update the ball's position based on keyboard inputs and velocity
        if keyboard.is_pressed('w'):
            if self.rect.colliderect(level.rect):
                self.y_velocity = 0
                self.airborne = False
                self.y_velocity += 10
                self.airborne = True
            elif self.rect.colliderect(platform.rect):
                self.y_velocity = 0
                self.airborne = False
                self.y_velocity += 10
                self.airborne = True
        elif keyboard.is_pressed('a') and time.time() - last_x_update_time >= x_interval and self.x_velocity > -15:
            self.x_velocity -= 2
        elif keyboard.is_pressed('d') and time.time() - last_x_update_time >= x_interval and self.x_velocity < 15:
            self.x_velocity += 2
        else:
            self.x_velocity = 0

        self.rect.y -= self.y_velocity
        self.rect.x += self.x_velocity

        if self.rect.y < 20:
            self.y_velocity = -2

    def draw(self):
        screen.blit(self.image, self.rect)


class Level(Sprite):
    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y)
        self.rect.width = width
        self.rect.height = height

    def draw(self):
        screen.blit(self.image, self.rect)


def show_popup(message):
    popup_font = pygame.font.Font(None, 36)
    popup_text = popup_font.render(message, True, (255, 255, 255))
    popup_rect = popup_text.get_rect(center=(screen_width // 2, screen_height // 2))
    pygame.draw.rect(screen, (0, 0, 0), (popup_rect.x - 10, popup_rect.y - 10, popup_rect.width + 20, popup_rect.height + 20))
    screen.blit(popup_text, popup_rect)
    pygame.display.update()
    time.sleep(0.5)


pygame.display.init()
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((0, 0), pygame.RESIZABLE, pygame.SHOWN)
start_time = 0
time_clock = 0

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption('Weirdly Coloured Ball')
font = pygame.font.SysFont("Arial", round(screen_width / 25))
score = 0

ball = Sprite('weirdly_coloured_ball.png.png', 220, 220)
last_jump_update_time = time.time()
jump_interval = 5
last_x_update_time = time.time()
x_interval = 0.5
collision = False
ball.airborne = True

level = Level('test_level.png', 0, screen_height - 50, screen_width, 50)
cliff = 300
platform = Level('platform.png', level.rect.width + cliff, screen_height - 50, screen_width, 50)
end = Level('platform.png', screen.get_width() - 50, 0, 50, 1000)

load_save()
with open('save.json', 'r') as file:
    save = json.load(file)

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            screen_width, screen_height = event.size
            screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
            font = pygame.font.SysFont("Arial", round(screen_width / 25))
    if keyboard.is_pressed('esc'):
        running = False
    elif keyboard.is_pressed('r'):
        platform = Level('platform.png', level.rect.width + cliff, random.randint(screen_height, screen.get_height()),screen_width, 50)
        level = Level('test_level.png', 0, random.randint(250, screen.get_height()), screen_width, 50)
        ball.rect.x = 220
        ball.rect.y = 220
        ball.y_velocity = 0

    if ball.rect.colliderect(level.rect):
        ball.y_velocity = 0
        ball.airborne = False
    elif ball.rect.colliderect(platform.rect):
        ball.y_velocity = 0
        ball.airborne = False
    elif ball.rect.colliderect(end.rect):
        platform = Level('platform.png', level.rect.width + cliff, random.randint(screen_height, screen.get_height()), screen_width, 50)
        level = Level('test_level.png', 0, random.randint(250, screen.get_height()), screen_width, 50)
        show_popup('Score +1')
        if save['highscore'] == score:
            save['highscore'] += 1
        score += 1
        ball.rect.x = 220
        ball.rect.y = 220
        ball.y_velocity = 0
    else:
        ball.y_velocity = ball.y_velocity - 0.5
    screen.fill((100, 128, 255))
    ball.update()
    ball.draw()
    level.draw()
    platform.draw()
    end.draw()
    high_score_text = font.render("High Score: {}".format(save['highscore']), True, (0, 0, 0))
    screen.blit(high_score_text, (10, 0))
    score_text = font.render("Score: {}".format(score), True, (0, 0, 0))
    screen.blit(score_text, (high_score_text.get_width() + 50, 0))
    reset_text = font.render("R = Reset", True, (0, 0, 0))
    screen.blit(reset_text, (score_text.get_width() + high_score_text.get_width() + 100, 0))
    esc_text = font.render("Esc = Quit", True, (0, 0, 0))
    screen.blit(esc_text, (reset_text.get_width() + score_text.get_width() + 150 + high_score_text.get_width(), 0))
    time_text = font.render(f"Time = {time_clock}", True, (0, 0, 0))
    screen.blit(time_text, (reset_text.get_width() + score_text.get_width() + 200 + high_score_text.get_width() + esc_text.get_width(), 0))
    pygame.draw.rect(screen, (255, 255, 255), level.rect, 3)
    pygame.draw.rect(screen, (255, 255, 255), platform.rect, 3)
    pygame.draw.rect(screen, (100, 255, 150), end.rect, 3)
    pygame.display.flip()
    clock.tick(60)
    ran_time = time.time()
    if ran_time == start_time + 1:
        time_clock += 1
        start_time = time.time()

data = {"highscore": save['highscore']}
with open('save.json', 'w') as file:
    json.dump(data, file)

pygame.quit()
