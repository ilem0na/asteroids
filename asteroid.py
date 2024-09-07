from circleshape import CircleShape
import pygame
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x  = x 
        self.y = y
        
    def draw(self, screen):
        points = self.triangle()
        color = (255, 255, 255)  # White color
        line_width = 2
        pygame.draw.circle(screen, "white", (int(self.x), int(self.y)), self.radius, line_width)