import pygame
from pygame.locals import *
import json
import os
import time
import keyboard

pygame.display.init()
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)


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
        if keyboard.is_pressed('w') or (keyboard.is_pressed('s') and time.time() - last_jump_update_time >= jump_interval):
            self.y_velocity += 5
        elif keyboard.is_pressed('a') and time.time() - last_x_update_time >= x_interval and self.x_velocity > 15:
            self.x_velocity -= 6
        elif keyboard.is_pressed('d') and time.time() - last_x_update_time >= x_interval and self.x_velocity < 15:
            self.x_velocity += 6

        if pygame.sprite.collide_mask(ball, level_1) and self.y_velocity < 0:
            self.y_velocity = 0
        elif collision is not True:
            self.y_velocity -= 0.5

        if self.x_velocity > 0:
            self.x_velocity -= 4.5
        elif self.x_velocity < 0:
            self.x_velocity += 4.5

        self.rect.y -= self.y_velocity
        self.rect.x += self.x_velocity

    def scale_image(self, scale_factor):
        new_width = int(self.image.get_width() * scale_factor)
        new_height = int(self.image.get_height() * scale_factor)
        self.image = pygame.transform.scale(self.image, (new_width, new_height))

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Level(Sprite):
    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y)
        self.rect.width = width
        self.rect.height = height

    def scale_image(self, scale_factor):
        new_width = int(self.image.get_width() * scale_factor)
        new_height = int(self.image.get_height() * scale_factor)
        self.image = pygame.transform.scale(self.image, (new_width, new_height))

    def change_length(self, length):
        original_height = self.image.get_height()
        self.image = pygame.transform.scale(self.image, (length, original_height))
        self.rect.width = length

    def change_height(self, height):
        original_length = self.image.get_width()
        original_height = self.image.get_height()
        self.image = pygame.transform.scale(self.image, (original_length, height))
        self.rect.height = height
        self.rect.y += original_height - height

    def draw(self, screen):
        screen.blit(self.image, self.rect)


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


def detect_black(sprite):
    mask = sprite.mask
    for x in range(sprite.rect.width):
        for y in range(sprite.rect.height):
            if mask.get_at((x, y)):
                return True
    return False


last_jump_update_time = time.time()
jump_interval = 2
last_x_update_time = time.time()
x_interval = 0.5

screen_width = 600
screen_height = 400

ball = Sprite('weirdly_coloured_ball.png.png', 0, 0)
level_1 = Level('test_level-removebg-preview.png', 0, screen_height - 50, screen_width, 50)
level_1.change_length(screen_width)
level_1.change_height(screen_height * 3 / 4)

score = 0
x_velocity = 0
y_velocity = 0
angular_momentum = 0
x_position = 0
y_position = 0

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption('Weirdly Coloured Ball')
font = pygame.font.SysFont("Arial", round(screen_width / 25))

collision = False

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
            level_1.change_length(screen_width)
            level_1.change_height(screen_height * 3 / 4)
            screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
            font = pygame.font.SysFont("Arial", round(screen_width / 25))
    if pygame.sprite.collide_mask(ball, level_1):
        y_velocity = 0
        y_position = level_1.rect.top
        ball.rect.y = level_1.rect.top
        collision = True
    elif collision is not True:
        y_velocity -= 0.5
        collision = False
    ball.update()
    screen.fill((100, 128, 255))
    ball.draw(screen)
    level_1.draw(screen)
    score_text = font.render("Score: {}".format(score), True, (0, 0, 0))
    screen.blit(score_text, (10, 0))
    highscore_text = font.render("High Score: {}".format(save['highscore']), True, (0, 0, 0))
    screen.blit(highscore_text, (screen_width - highscore_text.get_width() - 10, 0))
    pygame.draw.rect(screen, (255, 255, 255), ball.rect, 2)  # White color with a border of 2 pixels
    pygame.draw.rect(screen, (255, 255, 255), level_1.rect, 2)  # White color with a border of 2 pixels

    if detect_black(ball):
        print("Black color detected!")

    if y_velocity == 0:
        y_position = y_position
    else:
        y_position -= y_velocity
    x_position += x_velocity

    pygame.display.flip()
    clock.tick(60)

data = {"highscore": save['highscore']}
with open('save.json', 'w') as file:
    json.dump(data, file)

pygame.quit()
