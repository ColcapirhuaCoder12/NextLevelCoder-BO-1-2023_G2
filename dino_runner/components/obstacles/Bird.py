from dino_runner.components.obstacles.obstacle import Obstacle
import random

class Bird(Obstacle): 
    
    def __init__(self, image_list, type):
        self.type = 0
        super().__init__(image_list, type)
        self.rect.y = 250
        self.index_bird = 0

    def draw(self, screen):
        if self.index_bird <= 5:
            self.type = 0
        else:
            self.type = 1

        self.index_bird += 1
        
        if self.index_bird >= 10:
            self.index_bird = 0

        screen.blit(self.image_list[self.type], self.rect )


    