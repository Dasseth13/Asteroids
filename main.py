from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
import pygame
import sys
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    fps = pygame.time.Clock()
    dt = 0.0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)

    asteroidfield = AsteroidField()
    pl = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #keeps things refreshing
        screen.fill("black")
        updatable.update(dt)

        #checks collision of an asteroid with player
        for ast in asteroids:
            if ast.collides_with(pl):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        #checks collosion of asteroid with shots
        for ast in asteroids:
            for sh in shots:
                if ast.collides_with(sh):
                    log_event("asteroid_shot")
                    ast.kill()
                    sh.kill()

        for d in drawable:
            d.draw(screen)

        pygame.display.flip()
        dt = fps.tick(60) / 1000

if __name__ == "__main__":
    main()
