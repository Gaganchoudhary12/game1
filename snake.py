import pygame
import random
import os
#x = pygame.init()

#creating window
gamewin= pygame.display.set_mode((800,500))
pygame.display.set_caption("Gagan's Game")
#colore
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
snake_size = 12

pygame.font.init()
font = pygame.font.SysFont(None, 55)

def score_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gamewin.blit(screen_text, [x, y])


def plote_snk(window,color,snk_list,snk_size):
    for x,y in snk_list:
        pygame.draw.rect(gamewin, black, [x,y,snake_size,snake_size])
# Game_loop
def gameloop():
    # game specific variables
    Exit_game = False
    Game_over = False
    food_x = random.randint(90, 650)
    food_y = random.randint(90, 400)
    snake_x = 145
    snake_y = 165
    velocity_x = 0
    velocity_y = 0
    init_velocity = 2
    food_size = 12
    fps = 60
    if(not os.path.exists("high")):
        with open("high","w") as f:
            f.write("0")
    else:
        with open("high", "r") as f:
            hiscore = f.read()

    clock = pygame.time.Clock()
    score = 0
    snk_list = []
    snk_length = 1

    while not Exit_game:
        if Game_over:
            with open("high", "w") as f:
                f.write(str(hiscore))
            gamewin.fill(white)
            score_screen("Game Over Enter to continue Your score:"+str(score),red,10,250)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Exit_game = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    gameloop()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                         velocity_x = + init_velocity
                         velocity_y = 0
                    if event.key == pygame.K_LEFT:
                         velocity_x = - init_velocity
                         velocity_y = 0

                    if event.key == pygame.K_UP:
                         velocity_y = - init_velocity
                         velocity_x = 0
                    if event.key == pygame.K_DOWN:
                         velocity_y = + init_velocity
                         velocity_x = 0


            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y
            if abs(snake_x - food_x) < 8 and abs(snake_y - food_y) < 8:
                score += 1
                food_x = random.randint(0, 700)
                food_y = random.randint(0, 400)
                init_velocity += .05
                snk_length +=5
                if score>int(hiscore):
                    hiscore = score


            gamewin.fill(white)
            score_screen("score:"+str(score) + "Hiscore:"+str(hiscore), red, 5, 5)
            pygame.draw.rect(gamewin, red, [food_x, food_y, food_size, food_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                Game_over = True

            if snake_x<0 or snake_x>800 or snake_y<0 or snake_y>500:
                Game_over =True


            #pygame.draw.rect(gamewin, black, [snake_x, snake_y, snake_size, 12])
            plote_snk(gamewin, black, snk_list, snake_size, )
        pygame.display.update()
        clock.tick(fps)


    pygame.quit()
    quit()
gameloop()