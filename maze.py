# Maze Generator

import pygame
import time
from const import *
from functions import *

# Initialize
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Generator")
clock = pygame.time.Clock()

# Create variables that have the state of the maze
SQUARES_PER_SIDE = WIDTH // SQUARE_SIZE         # Number of squares per side

# Each cell of the maze is composed by 4 letters (l)eft, (u)p, (d)own, (r)ight that identifies which walls they have
maze = [['lurd' for i in range(SQUARES_PER_SIDE)] for j in range(SQUARES_PER_SIDE)]

current = (0, 0)            # Maze starts being generated in top left corner


# Create lists that contain the cells that were already visited and the ones that were not
unvisited = [(i, j) for i in range(SQUARES_PER_SIDE) for j in range(SQUARES_PER_SIDE)]
unvisited.remove(current)

visited = [current]

drawing = True
finished = False
solving = True

while not finished:


    # Listen to events
    for event in pygame.event.get():

        # In case red cross is clicked it closes the window
        if event.type == pygame.QUIT:
            finished = True
            pygame.quit()



    while drawing:
        
        # Set FPS
        clock.tick(FPS)
        
        
        # Draw
        screen.fill(BGCOLOR)
        drawMaze(maze, screen, SQUARE_SIZE, current)

        
        # Creating Maze
        maze, current, visited, unvisited, solution, drawing = nextMove(current, maze, unvisited, visited)


        # Render
        pygame.display.flip()

        print


    while solving:
        # Set FPS
        clock.tick(FPS)
        
        
        # Draw
        screen.fill(BGCOLOR)
        drawMaze(maze, screen, SQUARE_SIZE, current)

        # Defining start and end points
        start = START
        end = END

        # Calling solving function
        path, solving = find_route(start, end, SQUARE_SIZE)
        
        
        # Render
        pygame.display.flip()

# When the loop finished we close pygame
pygame.quit()
