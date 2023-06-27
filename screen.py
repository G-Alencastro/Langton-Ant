from lib2to3.pgen2.token import GREATER
import pygame
from pygame.locals import *
from main import *

pygame.init()

def draw_gens(ant):
    rect_side = screen_size[0]/len(ant.grid[0])
    colors = ('WHITE', 'RED', 'GREEN', 'PURPLE')

    for x in range(len(ant.grid)):
        for y in range(len(ant.grid[0])):
            pygame.draw.rect(screen, colors[ant.grid[x][y]], ((x*rect_side, y*rect_side), (rect_side-1, rect_side-1)))

screen_size = (601, 601)
screen = pygame.display.set_mode(screen_size)

ant = Ant([25, 25], (50, 50))

fps = 10
clock = pygame.time.Clock()

while True:
    clock.tick(fps)
    screen.fill('BLACK')

    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            if event.key == K_UP:
                fps += 1
            if event.key == K_DOWN:
                fps -= 1

        if event.type == QUIT:
            pygame.quit()


    draw_gens(ant)
    ant.walk()
    

    pygame.display.update()

