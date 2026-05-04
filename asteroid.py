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
        self.on_screen = False

    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt
        
        #Added this with the help of Boots to remove Asteroid objects once they were no longer on screen.
        #The idea is to help with performance so we are not considering Asteroids that are no longer 
        #in the game space.
        if not self.on_screen:
            # check if it has entered the screen yet
            if (0 <= self.position.x <= SCREEN_WIDTH and 
                0 <= self.position.y <= SCREEN_HEIGHT):
                self.on_screen = True
        else:
            # only kill it once it has left after entering
            if (self.position.x < 0
                or self.position.x > SCREEN_WIDTH
                or self.position.y < 0
                or self.position.y > SCREEN_HEIGHT):
                self.kill()

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

