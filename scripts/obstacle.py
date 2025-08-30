import pygame
import random
from scripts.config import SCREEN_WIDTH, SCREEN_HEIGHT, OBSTACLE_SPEED, RED

class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        width = 50
        height = 50
        
        self.image = pygame.Surface((width, height))
        self.image.fill(RED)  # Red color
        
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH + random.randint(0, 200)
        self.rect.y = SCREEN_HEIGHT - height
        
    def update(self):
        self.rect.x -= OBSTACLE_SPEED
        if self.rect.right < 0:
            self.kill()