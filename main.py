import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shots import Shots
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    # Create the groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    # creating group for asteroids
    asteroid = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    # Assigning groups to the Asteroid Class && Shots Class
    Asteroid.containers = (asteroid, updatable, drawable)
    Shots.containers = (shots, updatable, drawable)
    
    # Assigning updatable group to AsteroidField Container
    AsteroidField.containers = updatable
    
    
    
    # Assign the groups to the Player class
    Player.containers = (updatable, drawable)
    
    # Create the player object after setting the containers
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    # Creating an asterofield object
    asteroid_field = AsteroidField()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        
        # Draw all drawable objects
        for entity in drawable:
            entity.draw(screen)
        
        pygame.display.flip()
        
        # Update all updatable objects
        for entity in updatable:
            entity.update(dt)
            
        for a in asteroid:
            if a.check_collision(player):
                print("Game Over!")
                pygame.quit()
                return
        
        # Limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()