import sys, pygame, random, time
pygame.init()

SIZE = width, height = 800, 480
BLACK = 0, 0, 0
WHITE = 255, 255, 255
RADIUS = 15
# rand_seed = random.seed(pygame.time.Clock.tick())
# rand_num = random.choice([-1,1])
delta_x = 1 #direction of ball
delta_y = 1
ball_coordinate = [400, 240]
left_coordinate = [50, 200, 30, 100] #x, y, width, height for left slider
right_coordinate = [700, 200, 30, 100] #Right slider
not_done = True


SCREEN = pygame.display.set_mode(SIZE)
TITLE = pygame.display.set_caption("Pong")


def move_left_slider():
    if event.type == pygame.KEYDOWN: #if 'w' key pressed, move up
        if event.key == pygame.K_w and left_coordinate[1] >= 5: #aestheticly pleasing
            SCREEN.fill(BLACK)
            left_coordinate[1] -= 1
            pygame.time.delay(1)

    if event.type == pygame.KEYDOWN: #if 'w' key pressed, move down
        if event.key == pygame.K_s and left_coordinate[1] <= 375:
            SCREEN.fill(BLACK)
            left_coordinate[1] += 1
            pygame.time.delay(1)


def move_ball():

    global delta_x
    global delta_y
    pygame.time.wait(5)
    SCREEN.fill(BLACK)

    #Within borders, move ball
    if ball_coordinate[1] >= 20 and ball_coordinate[1] <= 465:
        ball_coordinate[0] += delta_x
        ball_coordinate[1] += delta_y

        #if it hits the top or bottom, bounce the ball at an angle
        if ball_coordinate[1] == 20 or ball_coordinate[1] == 465:
            delta_y *= -1

        #if it hits the left or right wall, reset ball at center
        if ball_coordinate[0] == 20 or ball_coordinate[0] == 785:
            ball_coordinate[0] = 400
            ball_coordinate[1] = 240
            delta_x *= -1 
            delta_y *= -1


        #if ball hits left slider, bounce back at an angle
        # if ball_coordinate[1] < (left_coordinate[1] + left_coordinate[3]/2) and ball_coordinate[1] > (left_coordinate[1] - left_coordinate[3]/2) and ball_coordinate[0] < (left_coordinate[0] + 38):
        if ball_coordinate[0] == left_coordinate[0] + left_coordinate[2] and ball_coordinate[1] <= left_coordinate[1] + left_coordinate[3] and ball_coordinate[1] >= left_coordinate[1]:
            delta_x *= -1
            #38 = left side of slider + width + 7.5 for half of radius of ball

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
