import pygame

FONT_STYLE = 'freesansbold.ttf'
from dino_runner.utils.constants import COLORS, SCREEN_HEIGHT, SCREEN_WIDTH

class TextUtils:

    FONT_STYLE = 'freesansbold.ttf'

    def get_score(self, points):
        font = pygame.font.Font(self.FONT_STYLE, 20)

        Text = font.render('points:' + str(points), True, COLORS['blue'])
        Text_rect = Text.get_rect()
        Text_rect.center = (1000, 40)
        return Text, Text_rect
    
    def get_centered_message(self, message, width = SCREEN_WIDTH//2, heigth = SCREEN_HEIGHT//2):
        font = pygame.font.Font(self.FONT_STYLE, 20)

        Text = font.render(message, True, COLORS['black'])
        Text_rect = Text.get_rect()
        Text_rect.center = (width, heigth)
        return Text, Text_rect
    
    def get_text_surface(self, time_to_show):
    
        font = pygame.font.Font(self.FONT_STYLE, 20)

        Text = font.render('Shield total time:' + str(time_to_show), True, COLORS['red'])
        Text_rect = Text.get_rect()
        Text_rect.center = (1000, 40)
        return Text, Text_rect