from circleshape import CircleShape
from constants import SHOT_RADIUS
from constants import LINE_WIDTH
from constants import SCREEN_WIDTH
from constants import SCREEN_HEIGHT
import pygame

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    def update(self, dt):
        self.position += self.velocity * dt
        #Added to remove shots that are no longer on screen. Should help with resource consumption
        if (
            self.position.x < 0
            or self.position.x > SCREEN_WIDTH
            or self.position.y < 0
            or self.position.y > SCREEN_HEIGHT
        ):
            self.kill()