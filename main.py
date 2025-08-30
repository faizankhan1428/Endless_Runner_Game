import pygame
import sys
from scripts.config import (
    SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BLACK, BLUE, RED, FPS,
    OBSTACLE_SPEED, PLAYER_GRAVITY, PLAYER_JUMP_VELOCITY
)
from scripts.player import Player
from scripts.background import Background
from scripts.obstacle import Obstacle
from scripts.particles import Particle
import os

# 1. Initialize Pygame
pygame.init()

# 2. Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Endless Runner")

# Set up the game clock
clock = pygame.time.Clock()

# Set up fonts
font = pygame.font.Font(None, 36)

# Custom events
SPAWN_OBSTACLE = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_OBSTACLE, 2000)

SCORE_EVENT = pygame.USEREVENT + 2
pygame.time.set_timer(SCORE_EVENT, 1000)

# High score functions
def load_high_score():
    if not os.path.exists("highscore.txt"):
        return 0
    try:
        with open("highscore.txt", "r") as file:
            return int(file.read())
    except (IOError, ValueError):
        return 0

def save_high_score(score):
    with open("highscore.txt", "w") as file:
        file.write(str(score))

# Game over and menu screens
def game_over_screen(score, high_score):
    background = Background()  # Create a new background object
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                waiting = False

        # Continuously update and draw the background
        background.update()
        screen.blit(background.image, background.rect1)
        screen.blit(background.image, background.rect2)
        
        game_over_text = font.render("Game Over", True, RED)
        score_text = font.render(f"Score: {score}", True, BLACK)
        high_score_text = font.render(f"High Score: {high_score}", True, BLACK)
        restart_text = font.render("Press Space to Restart", True, BLACK)

        screen.blit(game_over_text, game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50)))
        screen.blit(score_text, score_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)))
        screen.blit(high_score_text, high_score_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)))
        screen.blit(restart_text, restart_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100)))

        pygame.display.flip()
        clock.tick(FPS)

def main_menu():
    background = Background()
    waiting_for_start = True
    while waiting_for_start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                waiting_for_start = False
        
        # Continuously draw and update the background on the menu screen
        background.update()
        screen.blit(background.image, background.rect1)
        screen.blit(background.image, background.rect2)

        menu_title = font.render("Endless Runner", True, BLACK)
        start_text = font.render("Press Space to Start", True, BLACK)
        
        screen.blit(menu_title, menu_title.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50)))
        screen.blit(start_text, start_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)))
        
        pygame.display.flip()
        clock.tick(FPS)

# Main game loop
def run_game():
    high_score = load_high_score()
    
    main_menu()

    while True:
        # Reset game variables for a new round
        score = 0
        all_sprites = pygame.sprite.Group()
        obstacles = pygame.sprite.Group()
        particles = pygame.sprite.Group()
        
        background = Background()
        player = Player(100, SCREEN_HEIGHT - 50)
        
        all_sprites.add(player)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        player.jump()
                if event.type == SPAWN_OBSTACLE:
                    new_obstacle = Obstacle()
                    all_sprites.add(new_obstacle)
                    obstacles.add(new_obstacle)
                if event.type == SCORE_EVENT:
                    score += 1
            
            # Update all sprite groups
            player.update(all_sprites)
            obstacles.update()
            particles.update()
            background.update()

            # Collision detection
            if pygame.sprite.spritecollide(player, obstacles, False):
                running = False
            
            # Drawing to the screen
            screen.blit(background.image, background.rect1)
            screen.blit(background.image, background.rect2)
            
            all_sprites.draw(screen)
            particles.draw(screen)

            # Draw the scores
            score_text = font.render(f"Score: {score}", True, BLACK)
            high_score_text = font.render(f"High Score: {high_score}", True, BLACK)
            screen.blit(score_text, (10, 10))
            screen.blit(high_score_text, (10, 50))
            
            pygame.display.flip()
            clock.tick(FPS)
        
        # Handle game over state
        if score > high_score:
            high_score = score
            save_high_score(high_score)
        
        game_over_screen(score, high_score)

if __name__ == "__main__":
    run_game()