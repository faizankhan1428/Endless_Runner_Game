import pygame
from scripts.config import SCREEN_WIDTH, SCREEN_HEIGHT, OBSTACLE_SPEED

class Background(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/sprites/ground.png').convert()
        self.image = pygame.transform.scale(self.image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        
        self.rect1 = self.image.get_rect()
        self.rect2 = self.image.get_rect()
        
        self.rect1.x = 0
        self.rect1.y = 0
        self.rect2.x = self.rect1.width
        self.rect2.y = 0
        
        self.scroll_speed = OBSTACLE_SPEED

    def update(self):
        self.rect1.x -= self.scroll_speed
        self.rect2.x -= self.scroll_speed
        
        if self.rect1.right < 0:
            self.rect1.x = self.rect2.right
        if self.rect2.right < 0:
            self.rect2.x = self.rect1.right