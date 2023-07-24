import pygame
from pygame.locals import *
import json
import os
import time
import keyboard


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
        if keyboard.is_pressed('w') and self.airborne == False:
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


pygame.display.init()
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((0, 0), pygame.RESIZABLE, pygame.SHOWN)

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption('Weirdly Coloured Ball')
font = pygame.font.SysFont("Arial", round(screen_width / 25))

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
        ball.rect.x = 220
        ball.rect.y = 220
        ball.y_velocity = 0

    if ball.rect.colliderect(level.rect):
        ball.y_velocity = 0
        ball.airborne = False
    elif ball.rect.colliderect(platform.rect):
        ball.y_velocity = 0
        ball.airborne = False
    else:
        ball.y_velocity = ball.y_velocity - 0.5
    screen.fill((100, 128, 255))
    ball.update()
    ball.draw()
    level.draw()
    platform.draw()
    pygame.draw.rect(screen, (255, 255, 255), level.rect, 3)
    pygame.draw.rect(screen, (255, 255, 255), platform.rect, 3)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
