import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH
from constants import SCREEN_HEIGHT
from constants import SCREEN_WIDTH
from constants import ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius )

    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        #This covers the case of the smallest possible asteroid. It does not split, it just gets deleted.
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("Asteroid Split")
        split_angle = random.uniform(20, 50)
        new_asteroid_velocity_1 = self.velocity.rotate(split_angle)
        new_asteroid_velocity_2 = self.velocity.rotate(-1 * split_angle)
        new_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
        new_asteroid_1.velocity = new_asteroid_velocity_1 * 1.2
        new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
        new_asteroid_2.velocity = new_asteroid_velocity_2 * 1.2

