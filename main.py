import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Starting asteroids! \nScreen width: {SCREEN_WIDTH} \nScreen height: {SCREEN_HEIGHT}")
    
    server_clock = pygame.time.Clock()
    dt = 0
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
                
        
        screen.fill((0, 0, 0))  # Fill the screen with black color
        pygame.display.flip()   # Refresh the screen
        dt = server_clock.tick(60) / 1000
    pygame.quit()

if __name__ == "__main__":
    main()