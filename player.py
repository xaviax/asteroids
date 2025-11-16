from pygame.examples.glcube import rotate

from circleshape import CircleShape
from constants import PLAYER_RADIUS, LINE_WIDTH, SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_TURN_SPEED, PLAYER_SPEED, \
    PLAYER_SHOOT_SPEED, SHOT_RADIUS, PLAYER_SHOT_COOLDOWN_SECONDS
import pygame
from shot import Shot

class Player(CircleShape):
    def __init__(self,x,y):
        super().__init__(x,y,PLAYER_RADIUS)

        self.rotation=0
        self.cooldown_timer=0


    # in the Player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen,'white',self.triangle(),LINE_WIDTH)


    def rotate(self,dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self,dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

    def update(self,dt):
        keys = pygame.key.get_pressed()
        self.cooldown_timer-=dt

        if keys[pygame.K_a]:
            self.rotate(-1*dt)


        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_w]:
            self.move(dt)

        if keys[pygame.K_s]:
            self.move(-1*dt)

        if keys[pygame.K_SPACE]:

            self.shoot()


    def shoot(self):

        if self.cooldown_timer > 0:
            return True

        else:
            self.cooldown_timer = PLAYER_SHOT_COOLDOWN_SECONDS

        shot =Shot(self.position.x,self.position.y,SHOT_RADIUS)
        vector=pygame.Vector2(0, 1)
        rotated_vector = vector.rotate(self.rotation)
        scaled_rotated_vector=rotated_vector * PLAYER_SHOOT_SPEED
        shot.velocity=scaled_rotated_vector




