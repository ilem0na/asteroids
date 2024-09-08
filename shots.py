from circleshape import CircleShape
import pygame
from constants import *
import random

class Shots(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.x  = x 
        self.y = y
        
    def draw(self, screen):
        #points = self.triangle()
        color = (255, 255, 255)  # White color
        line_width = 2
        pygame.draw.circle(screen, color, self.position, self.radius, line_width)
        
    def update(self, dt):
        self.position += self.velocity * dt