import pygame
from circleshape import CircleShape
from constants import *
from shots import Shots

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        #self.position = pygame.Vector2(x, y)
        self.rotation = 0
        self.timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        points = self.triangle()
        color = (255, 255, 255)  # White color
        line_width = 2
        pygame.draw.polygon(screen, color, points, line_width)
        
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_s] | keys[pygame.K_DOWN]:
            self.move(dt) 
        if keys[pygame.K_w] | keys[pygame.K_UP]:
            self.move(dt)
        if keys[pygame.K_a] | keys[pygame.K_LEFT]:
            self.rotate(-dt)
        if keys[pygame.K_d] | keys[pygame.K_RIGHT]:
            self.rotate(dt)
        if self.timer > 0:
            self.timer -= dt
        if keys[pygame.K_SPACE] or self.timer <= 0:
            self.shoot()   
       

    def shoot(self):
        shot = Shots(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        self.timer = PLAYER_SHOOT_COOLDOWN
        
            
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
        
        