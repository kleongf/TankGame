import pygame
import random


class Ball(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()
        self.velocity = [random.randint(4, 8), random.randint(4, 8)]

    def setxy(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = random.randint(-8, 8)

class Paddle(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()

    def setxy(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def left(self, amount):
        self.rect.x -= amount

    def right(self, amount):
        self.rect.x += amount

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

pygame.init()
screen = pygame.display.set_mode((800, 600))

sprites = pygame.sprite.Group()
paddle1 = paddle.Paddle(WHITE, 100, 10)
paddle1.setxy(400, 560)
sprites.add(paddle1)

ball1 = ball.Ball(WHITE, 10, 10)
ball1.setxy(400, 540)
sprites.add(ball1)

playing = True

clock = pygame.time.Clock()
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle1.left(5)
    if keys[pygame.K_RIGHT]:
        paddle1.right(5)

    if ball1.rect.y > 590:
        ball1.velocity[1] = -ball1.velocity[1]
    if ball1.rect.y < 50:
        ball1.velocity[1] = -ball1.velocity[1]
    if ball1.rect.x < 50:
        ball1.velocity[0] = -ball1.velocity[0]
    if ball1.rect.x > 750:
        ball1.velocity[0] = -ball1.velocity[0]

    if pygame.sprite.collide_mask(ball1, paddle1):
        ball1.rect.x -= ball1.velocity[0]
        ball1.rect.y -= ball1.velocity[1]
        ball1.bounce()


    sprites.update()

    screen.fill(BLACK)

    sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
