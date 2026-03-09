# Pygame docs: https://www.pygame.org/docs/

import sys
import pygame
import random


def main():
    pygame.init()  # must be called before using any pygame functionality
    screen = pygame.display.set_mode((600, 400))  # create a 600x400 windo
    apple_x, apple_y = move_apple(screen)
    snake_game(screen, apple_x, apple_y)



def snake_game(screen, apple_x, apple_y):
    clock = pygame.time.Clock()  # used to control the loop speed
    x_direction = 0
    y_direction = 0
    player_x = 20
    player_y = 20
    snake_body = [[player_x, player_y]]
    #make sure the player cant move backwards
    up = 0
    down = 0
    left = 0
    right = 0

    while True:

        victory(snake_body)
        player_failed(snake_body)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # user closed the window
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    left, right = 0, 0
                    up = 1
                    x_direction = 0
                    y_direction = -20
                elif event.key == pygame.K_DOWN:
                    left, right = 0, 0
                    down = 1
                    x_direction = 0
                    y_direction = 20
                elif event.key == pygame.K_LEFT:
                    up, down = 0, 0
                    left = 1
                    y_direction = 0
                    x_direction = -20
                elif event.key == pygame.K_RIGHT:
                    up, down = 0, 0
                    right = 1
                    y_direction = 0
                    x_direction = 20
                else:
                    pass
        if up == 1 and down == 1 or left == 1 and right == 1:
            sys.exit("you failed")
        player_x += x_direction
        player_y += y_direction

        # if player hit side of screen
        player_x, player_y = got_to_edges(player_x, player_y)

        #snake ate apple?
        # 5 == div
        if apple_x + 5 >= player_x and apple_x - 5 <= player_x and apple_y + 5 >= player_y and apple_y - 5 <= player_y:
            apple_x, apple_y = move_apple(screen)
            snake_body.insert(0, snake_body[-1])

        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (0, 220, 0), pygame.Rect(apple_x, apple_y, 20, 20))  # the apple
    
        snake_body.insert(0, [player_x, player_y])
        snake_body.remove(snake_body[-1])

        print_snake(snake_body, screen)
        pygame.display.flip()  # push everything drawn this frame to the actual screen
        clock.tick(10)  # wait enough time so the loop runs at most 10 times per second


def victory(snake_body):
    """
    check the length of the snake and if it's the size of the board exit and print win
    (600 * 400) \ (20 * 20) = 60
    :param snake_body:
    :return:
    """
    if len(snake_body) == 60:
        sys.exit("you won")



def print_snake(snake_body, screen):
    """
    display all the snake on the screen
    :param snake_body:
    :param screen:
    :return: none
    """
    for i in range(len(snake_body)):
        flag = 0
        for i2 in range(len(snake_body[i])):
            if flag == 0:
                player_x_move = snake_body[i][i2]
                flag += 1
            else:
                player_y_move = snake_body[i][i2]

        pygame.draw.rect(screen, (220, 0, 220), pygame.Rect(player_x_move, player_y_move, 20, 20))


def move_apple(screen):
    """
    give a new random location (x,y) for apple
    :param screen:
    :return:  apple_x, apple_y
    """
    apple_x = random.randrange(1, 600, 20)
    apple_y = random.randrange(1, 400, 20)
    return apple_x, apple_y


def got_to_edges(player_x, player_y):
    """
    when snake hit the end of the screen he will regenerate from the other side
    :param: player_x, player_y
    :return: player_x, player_y
    """
    screen_x = 600
    screen_y = 400
    if player_y < 0:
        player_y = screen_y - 20
    elif player_y >= screen_y:
        player_y = 0
    if player_x >= screen_x:
        player_x = 0
    elif player_x < 0:
        player_x = screen_x - 20
    return player_x, player_y


def player_failed(snake_body):
    """
    check if user failed
    :param snake_body:
    :return: none
    """
    for i in range(len(snake_body)-1):
        if snake_body[0][0] == snake_body[i + 1][0] and snake_body[0][1] == snake_body[i + 1][1]:
            sys.exit("end")


if __name__ == '__main__':
    main()
