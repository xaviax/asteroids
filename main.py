import sys

import pygame

from asteroid import Asteroid
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player
from asteroidfield import AsteroidField
from logger import log_event
from shot import Shot



def main():
    print(f"Starting Asteroids with pygame version:{pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH} \nScreen height: {SCREEN_HEIGHT}")

    pygame.init()
    clock_object=pygame.time.Clock()
    dt=0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    #Before the game loop starts:
    updatable=pygame.sprite.Group()
    drawable=pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers=(updatable,drawable)
    player =Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)


    Asteroid.containers=(asteroids,updatable,drawable)
    AsteroidField.containers=(updatable)
    AsteroidField()

    Shot.containers=(shots,updatable,drawable)



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        log_state()
        screen.fill('black')
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event('player_hit')
                print("Game over!")
                sys.exit()

            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()




        for draw_this in drawable:
                draw_this.draw(screen)


        #player.update(dt)
        #player.draw(screen)
        pygame.display.flip()
        time_last_called=clock_object.tick(60)
        dt=time_last_called/1000




if __name__ == "__main__":
    main()
