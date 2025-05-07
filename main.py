# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")

    # Game loop
    # This is the main loop that runs the game
    # It handles events, updates the game state, and draws the game to the screen
    # It runs until the user quits the game
    while True:
        screen.fill("black")
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
                
        pygame.display.flip()

if __name__ == "__main__":
    main()
    
