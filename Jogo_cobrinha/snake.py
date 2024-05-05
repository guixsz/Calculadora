import pygame
from pygame.locals import *
import random

WINDOW_SIZE = (600, 600)
PIXEL_SIZE = 10

def colision(pos1, pos2):
    return pos1 == pos2

def off_limits(pos):
    if 0 <= pos[0] < WINDOW_SIZE[0] and 0<= pos[1] < WINDOW_SIZE[1]:
        return False
    else:
        return True
    
def random_on_grid():
    x = random.randint(0, WINDOW_SIZE[0])
    y = random.randint(0, WINDOW_SIZE[1])
    return x // PIXEL_SIZE * PIXEL_SIZE, y // PIXEL_SIZE * PIXEL_SIZE
    


pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Snake')

snake_pos = [(250, 50), (260, 50), (270, 50)]
snake_surface = pygame.Surface((10, 10))
snake_surface.fill((255, 255, 255))
snake_direction = K_LEFT

apple_surface = pygame.Surface((10, 10))
apple_surface.fill((255, 0, 0))
apple_pos = random_on_grid()

while True:
    pygame.time.Clock().tick(30)
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()
        elif event.type == KEYDOWN:
            if event.key in [K_UP, K_DOWN, K_LEFT, K_RIGHT]:
                snake_direction = event.key

    # Movendo a cobra baseada na direção
    if snake_direction == K_UP:
        snake_pos[0] = (snake_pos[0][0], snake_pos[0][1] - PIXEL_SIZE)
    elif snake_direction == K_DOWN:
        snake_pos[0] = (snake_pos[0][0], snake_pos[0][1] + PIXEL_SIZE)
    elif snake_direction == K_LEFT:
        snake_pos[0] = (snake_pos[0][0] - PIXEL_SIZE, snake_pos[0][1])
    elif snake_direction == K_RIGHT:
        snake_pos[0] = (snake_pos[0][0] + PIXEL_SIZE, snake_pos[0][1])

 
    screen.blit(apple_surface, apple_pos)

    for pos in snake_pos:
        screen.blit(snake_surface, pos)


    for i in range(len(snake_pos) - 1, 0, -1):
        if colision(snake_pos[0], snake_pos[i]):
            pygame.quit()
            quit()
        snake_pos[i] = snake_pos[i-1]

        if off_limits(snake_pos[0]):
            pygame.quit()
            quit()

    pygame.display.update()