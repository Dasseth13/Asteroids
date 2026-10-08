import circleshape
from logger import log_event
import pygame
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
import random

class Asteroid(circleshape.CircleShape):

    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self) -> None:
        self.kill()

        # if asteroid is smallest size already, it is gone
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # if asteroid is medium or large, split into next smaller size
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        first_new_velo = self.velocity.rotate(angle)
        second_new_velo = self.velocity.rotate(-1 * angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        ast1 = Asteroid(self.position[0], self.position[1], new_radius)
        ast2 = Asteroid(self.position[0], self.position[1], new_radius)
        ast1.velocity = first_new_velo * 1.2
        ast2.velocity = second_new_velo * 1.2
