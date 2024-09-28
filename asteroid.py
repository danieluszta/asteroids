import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y,radius)
    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,2)
    def update(self,dt):
        self.position += self.velocity * dt
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_vector_1 = self.velocity.rotate(random.uniform(20,50))
            new_vector_2 = self.velocity.rotate(-random.uniform(20,50))
            asteroid_1 = Asteroid(self.position,new_radius,new_radius)
            asteroid_1.velocity = new_vector_1 * 1.2
            asteroid_2 = Asteroid(self.position,new_radius,new_radius)
            asteroid_2.velocity = new_vector_2 * 1.2
            

