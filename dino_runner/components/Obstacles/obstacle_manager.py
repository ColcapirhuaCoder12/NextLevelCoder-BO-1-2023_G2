from dino_runner.components.obstacles.cactus import Cactus, LCactie
from dino_runner.components.obstacles.Bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD


import pygame

class ObstacleManager:

    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            self.obstacles.append(Cactus(SMALL_CACTUS))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dinosaur_rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                game.playing = False
                break
            
            if len(self.obstacles) == 0:
                self.obstacles.append(LCactie(LARGE_CACTUS))

            for obstacle in self.obstacles:
                obstacle.update(not game.game_speed, self.obstacles)
                if game.player.dinosaur_rect.colliderect(obstacle.rect):
                 pygame.time.delay(500)
                 game.playing = False
                 break 
            
            if len(self.obstacles) == 1 and isinstance(self.obstacles[0], Cactus):
                self.obstacles.append(Bird(BIRD, 0))
        
            for obstacle in self.obstacles:
                 obstacle.update(not game.game_speed, self.obstacles)
                 if game.player.dinosaur_rect.colliderect(obstacle.rect):
                  pygame.time.delay(500)
                  game.playing = False
                  break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)