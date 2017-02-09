import sys, pygame
pygame.init()

SIZE = width, height = 800, 480
BLACK = 0, 0, 0
WHITE = 255, 255, 255
RADIUS = 15
delta_x = 1 #speed of ball
delta_y = 1
left = True
ball_coordinate = [400, 240]
left_coordinate = [50, 200, 30, 100] #x, y, width, height for left slider
right_coordinate = [700, 200, 30, 100] #Right slider
not_done = True

SCREEN = pygame.display.set_mode(SIZE)
TITLE = pygame.display.set_caption("Pong")


def move_left_slider():
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_w and left_coordinate[1] >= 5: #aestheticly pleasing
            SCREEN.fill(BLACK)
            left_coordinate[1] -= 1
            pygame.time.delay(1)

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_s and left_coordinate[1] <= 375:
            SCREEN.fill(BLACK)
            left_coordinate[1] += 1
            pygame.time.delay(1)


def move_ball():

    global delta_x
    global delta_y
    pygame.time.wait(10)
    SCREEN.fill(BLACK)

    if ball_coordinate[1] >= 20 and ball_coordinate[1] <= 465:
        ball_coordinate[0] += delta_x
        ball_coordinate[1] += delta_y
        if ball_coordinate[1] == 20 or ball_coordinate[1] == 465:
            delta_x *= -1
            delta_y *= -1

while not_done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            not_done = False

    move_left_slider()
    move_ball()

    ball = pygame.draw.circle(SCREEN, WHITE, ball_coordinate, RADIUS)
    left_slider = pygame.draw.rect(SCREEN, WHITE, left_coordinate)
    right_slider = pygame.draw.rect(SCREEN, WHITE, right_coordinate)

    pygame.display.flip()

pygame.quit()
quit()
