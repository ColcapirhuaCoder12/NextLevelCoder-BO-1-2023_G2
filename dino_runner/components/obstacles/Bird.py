from dino_runner.components.obstacles.obstacle import Obstacle
import random
class Bird(Obstacle): 
    
    def __init__(self, image_list, type):
        super().__init__(image_list, type)
        self.rect.y = random.randint(80, 100)
       
        
        