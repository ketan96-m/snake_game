import pygame
import random
import time

#Initialize the pygame module
pygame.init()
#Create window
disp_width, disp_height = 1000,1000
colours = {
    'red': (255, 0, 0),
    'blue': (0, 0, 255),
    'white': (255,255,255),
    'black': (0,0,0),
    'green': (0, 255, 0)
}
disp = pygame.display.set_mode((disp_width, disp_height),)
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()

snake_block = 10
font_style = pygame.font.Font('freesansbold.ttf', 32)

def update_food(disp_width, disp_height):
    foodx = round(random.randrange(0, disp_width)/10)* 10
    foody = round(random.randrange(0, disp_height)/10)*10
    return foodx, foody

def display_message(msg, color, x, y, center = False):
    mesg = font_style.render(msg, True, color)
    if center:
        textRect = mesg.get_rect()
        textRect.center = (x//2, y//2)
        disp.blit(mesg, textRect)
    else:
        disp.blit(mesg, (x, y))

def extend_snake(snake_list):
    for x, y in snake_list:
        pygame.draw.rect(disp, colours['blue'], [x, y, snake_block ,snake_block])

def gameloop():
    x1, y1 = disp_width/2, disp_height/2
    x1_change, y1_change = 0, 0
    game_over = False
    game_halt = False
    foodx, foody = update_food(disp_width, disp_height)
    snake_list = []
    snake_length = 1
    score = 0
    while not game_over:
        while game_halt:
            display_message('You Lost! Press Q-Quit or C-Restart', colours['red'], disp_width, disp_height, center = True)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_halt = False
                    elif event.key == pygame.K_c:
                        gameloop()
                elif event.type == pygame.QUIT:
                    game_over = True
                    game_halt = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block
                elif event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0

        snake_list.append((x1, y1))
        if len(snake_list) > snake_length:
            del snake_list[0]

        for x,y in snake_list[:-1]:
            if x == x1 and y == y1:
                game_halt = True

        if x1 >= disp_width or x1 < 0 or y1 >= disp_height or y1 < 0:
            display_message('Hit the wall', colours['red'], disp_width/2, disp_height/2)
            game_halt = True
            pygame.display.update()

        if x1 == foodx and y1 == foody:
            print('Yummy')
            foodx , foody = update_food(disp_width, disp_height)
            snake_length += 1
            score += 1

        x1 += x1_change
        y1 += y1_change
        disp.fill(colours['black'])
        # inner_rect = pygame.Rect(disp_height-snake_block, disp_width-snake_block)
        # inner_rect.center(disp_width//2, disp_height//2)
        # disp.blit(innter_rect)
        pygame.draw.rect(disp, colours['red'], (foodx, foody, snake_block, snake_block))
        extend_snake(snake_list)
        display_message(f'Score:{str(score)}', colours['green'], snake_block*2, snake_block*2)
        pygame.display.update()
        clock.tick(20)

    pygame.quit()
    quit()
gameloop()

