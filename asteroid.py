from circleshape import CircleShape
import pygame
import random
from constants import *


class Asteroid(CircleShape):
    def __init__(self,x,y,radius,velocity=None):
        super().__init__(x, y, radius)
        self.radius = radius
        self.velocity = velocity if velocity is not None else pygame.Vector2(0, 0)
    def draw(self, screen):
        pygame.draw.circle(screen,color="white",center=(self.position.x, self.position.y),radius=self.radius,width=2)
    def update(self, dt):
        self.position += self.velocity * dt


    def split(self):
            # Always kill this asteroid
        self.kill()

            # If this asteroid is at the smallest size, don't split
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
            # Compute new radius
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Generate random angle for splitting
        random_angle = random.uniform(20, 50)

            # Create two new velocities in opposite directions
        vel1 = self.velocity.rotate(random_angle) * 1.2
        vel2 = self.velocity.rotate(-random_angle) * 1.2

        # Spawn two new smaller asteroids at the same position
        a1 = Asteroid(self.position.x, self.position.y, new_radius)
        a1.velocity = vel1

        a2 = Asteroid(self.position.x, self.position.y, new_radius)
        a2.velocity = vel2






