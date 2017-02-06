import sys, pygame
pygame.init()

size = width, height = 800, 480
speed = [2,2]
BLACK = 0, 0, 0
WHITE = 255, 255, 255

screen = pygame.display.set_mode(size)

ball = pygame.draw.circle(screen, WHITE, [400, 240], 15)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    ball
    pygame.display.flip()
