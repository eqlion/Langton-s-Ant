#!/usr/bin/env python3

import pygame
import random

from math import sin, cos, sqrt

from Ant import Ant
from Square import Square

# Initialize the game engine
pygame.init()

# Setting base RGB colors
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]

# Setting the size of the screen
width = 1920
height = 1080
size = 5

# Testing whether width and height have allowed values
if width % size != 0 or height % size != 0:
    raise ValueError("Width and height have to be evenly divisible by size")

# Creating the sreen and its frame
screen = pygame.display.set_mode([width, height])
pygame.display.set_caption("Langton's Ant")

clock = pygame.time.Clock()
done = False

squares = []

# Calculating numbers of squares horizontally and vertically
nx = width // size
ny = height // size

ant = Ant(nx,ny)

# Filling the squares list with Square objects
for i in range(0, width, size):
    line = []
    for j in range(0, height, size):
        line.append(Square(i,j))
    squares.append(line)

# Function that draws squares on the screen
def show(squares):
    global size
    for i in squares:
        for j in i:
            color = BLACK if j.state else WHITE
            pygame.draw.rect(screen, color, [j.x,j.y,size,size])

screen.fill(BLACK)

# Main loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()

    show(squares)

    # This loop allows to do more moves per frame update as it significantly
    # increases the performance and boost the movement speed
    # To set speed back to normal change 50 to 1
    for _ in range(50):
        x = ant.x
        y = ant.y

        if squares[x][y].state:
            ant.rotate_left()
        else:
            ant.rotate_right()
        squares[x][y].flip()

        ant.move()

    # Updating the screen
    pygame.display.flip()

    # Limiting the updates of the screen per second
    # The loop and the limit allow 50 * 60 = 3000 ant moves per second
    clock.tick(60)

pygame.quit()
