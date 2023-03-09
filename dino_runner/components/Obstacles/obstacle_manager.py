from dino_runner.components.obstacles.cactus import Cactus, Lcactie
from dino_runner.components.obstacles.Bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD
import random

import pygame

class ObstacleManager:

    def __init__(self):
        self.obstacles = []

    def update(self, game):
        index = random.randint(0,2)
        

        if len(self.obstacles) == 0:
            if index == 0:
                self.obstacles.append(Cactus(SMALL_CACTUS))
            elif index == 1:
                self.obstacles.append(Lcactie(LARGE_CACTUS))
            elif index == 2: 
                self.obstacles.append(Bird(BIRD, 0))
            
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.shield:
                    pygame.time.delay(500)
                    game.playing = False
                    break
                else:
                    self.obstacles.remove(obstacle)
            
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []