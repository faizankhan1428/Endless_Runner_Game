import pygame
import random
from scripts.config import PLAYER_GRAVITY, PLAYER_JUMP_VELOCITY, SCREEN_HEIGHT, BLUE
from scripts.particles import Particle

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocity_y = 0
        self.is_jumping = False
        self.on_ground = True

    def update(self, all_sprites_group):
        self.velocity_y += PLAYER_GRAVITY
        self.rect.y += self.velocity_y
        
        # Check for landing
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.velocity_y = 0
            
            # Create landing particles only if we just landed from a jump
            if not self.on_ground:
                self.on_ground = True
                for _ in range(10):
                    particle = Particle(self.rect.midbottom[0], self.rect.midbottom[1], random.randint(3, 8))
                    all_sprites_group.add(particle)
            
            self.is_jumping = False
        
        # If we are in the air, we are not on the ground
        if self.rect.bottom < SCREEN_HEIGHT:
            self.on_ground = False

    def jump(self):
        # Only allow jumping if the player is on the ground
        if self.on_ground:
            self.is_jumping = True
            self.velocity_y = PLAYER_JUMP_VELOCITY