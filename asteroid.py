from circleshape import CircleShape
import pygame
from constants import *
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")
        
        random_angle = random.uniform(20,50)
        a1_movement = self.velocity.rotate(random_angle)
        a2_movement = self.velocity.rotate(-random_angle)

        a1_radius = self.radius - ASTEROID_MIN_RADIUS
        a2_radius = self.radius - ASTEROID_MIN_RADIUS

        a1 = Asteroid(self.position.x,self.position.y,a1_radius)
        a2 = Asteroid(self.position.x,self.position.y,a2_radius)

        a1.velocity = a1_movement * 1.2
        a2.velocity = a2_movement * 1.2
