from dino_runner.components.Obstacles.Obstacle import Obstacle
import random

class Cactus(Obstacle):

    def __init__(self, image_list, type):
        super().__init__(image_list, type)
        self.type = random.randint(0, 2)
        self.rect.y = 325