import pygame
from dino_runner.utils.constants import SCREEN_WIDTH


class Bird(Obstacle):
    def __init__(self):
        self.image = self.image
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = 250

    def update(self, game_speed, obstacles):
        self.rect.x -= game_speed
        if self.rect.x <= 0:
            obstacles.pop()

    def draw(self, screen):
        screen.blit(self.image, self.rect)