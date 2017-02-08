import sys, pygame
pygame.init()

SIZE = 800, 480  #width, height
speed = [2,0]
BLACK = 0, 0, 0
WHITE = 255, 255, 255
ball_coordinate = 400, 240
left_coordinate = [50, 200, 30, 100] #x, y, width, height
right_coordinate = [700, 200, 30, 100]

screen = pygame.display.set_mode(SIZE)
title = pygame.display.set_caption("Pong")


def move_object():
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_w:
            screen.fill(BLACK)
            left_coordinate[1] -= 1
            # left_coordinate[3] += 1
            pygame.time.delay(10)
            print(left_coordinate[1])
            # print(left_coordinate[3])


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    move_object()

    ball = pygame.draw.circle(screen, WHITE, ball_coordinate, 15)
    left_slider = pygame.draw.rect(screen, WHITE, left_coordinate)
    right_slider = pygame.draw.rect(screen, WHITE, right_coordinate)

    pygame.display.flip()
