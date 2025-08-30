import pygame
import random
from scripts.config import WHITE

class Particle(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect(center=(x, y))
        self.velocity_x = random.randint(-5, 5)
        self.velocity_y = random.randint(-10, -5)
        self.gravity = 0.5
        self.lifetime = 60 # Particle lasts for 60 frames

    def update(self):
        self.velocity_y += self.gravity
        self.rect.x += self.velocity_x
        self.rect.y += self.velocity_y
        self.lifetime -= 1
        if self.lifetime <= 0:
            self.kill() # Remove the particle when its time is up