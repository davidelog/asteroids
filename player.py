import pygame
from circleshape import CircleShape 
from constants import *
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.timer = 0
        self.rotation = 0
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation+90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "orange", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += dt * PLAYER_TURN_SPEED

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rotate(-dt)
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rotate(dt)
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.move(dt)
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shot(dt)
        self.timer -= dt

    def move(self, dt):
        self.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SPEED
        self.position += self.velocity * dt

    def shot(self, dt):
        if self.timer <= 0:
            shot = Shot(self.position.x, self.position.y, SHOT_RADIUS, pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED)
            self.timer = PLAYER_SHOOT_COOLDOWN 
            