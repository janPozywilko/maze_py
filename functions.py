
import pygame
import random
import time
from const import *


solution = {}

def drawMaze(maze, surface, square_size, current):
    # Show current cell position in blue
    pygame.draw.rect(surface,
                     (0, 0, 255),
                     (current[1] * square_size,
                      current[0] * square_size,
                      square_size,
                      square_size),
                     )

    for i, line in enumerate(maze):
        for j, element in enumerate(line):

            if 'l' in element:
                pygame.draw.line(surface,
                                 (0, 0, 0),  
                                 (j * square_size, i * square_size),  
                                 (j * square_size, i * square_size + square_size),  
                                 2  
                                 )

            if 'u' in element:
                pygame.draw.line(surface,
                                 (0, 0, 0),
                                 (j * square_size, i * square_size),
                                 (j * square_size + square_size, i * square_size),
                                 2
                                 )

            if 'r' in element:
                pygame.draw.line(surface,
                                 (0, 0, 0),
                                 (j * square_size + square_size, i * square_size),
                                 (j * square_size + square_size, i * square_size + square_size),
                                 2
                                 )

            if 'd' in element:
                pygame.draw.line(surface,
                                 (0, 0, 0),
                                 (j * square_size, i * square_size + square_size),
                                 (j * square_size + square_size, i * square_size + square_size),
                                 2
                                 )


def nextMove(current, maze, unvisited, visited):

    drawing = True
    neighbours = []

    if current[0] + 1 < len(maze) and (current[0] + 1, current[1]) in unvisited:
        neighbours.append((current[0] + 1, current[1]))

    if current[1] + 1 < len(maze) and (current[0], current[1] + 1) in unvisited:
        neighbours.append((current[0], current[1] + 1))

    if current[0] - 1 >= 0 and (current[0] - 1, current[1]) in unvisited:
        neighbours.append((current[0] - 1, current[1]))

    if current[1] - 1 >= 0 and (current[0], current[1] - 1) in unvisited:
        neighbours.append((current[0], current[1] - 1))

    # If there is at least one possible movement
    if len(neighbours) > 0:

        # We choose a element randomly
        nextPos = random.choice(neighbours)

        # Now we need to now where to move
        if current[0] == nextPos[0]:  # Means it is in the same line
            if nextPos[1] > current[1]:  # Means we go right
                direction = 'r'
                maze[current[0]][current[1]] = maze[current[0]][current[1]].replace('r',
                                                                                    '')  # Remove right wall of current
                maze[nextPos[0]][nextPos[1]] = maze[nextPos[0]][nextPos[1]].replace('l',
                                                                                    '')  # Remove left wall of nextPos
                solution[(nextPos[0], nextPos[1])] = current[0], current[1]

            else:  # Means we go left
                direction = 'l'
                maze[current[0]][current[1]] = maze[current[0]][current[1]].replace('l',
                                                                                    '')  # Remove left wall of current
                maze[nextPos[0]][nextPos[1]] = maze[nextPos[0]][nextPos[1]].replace('r',
                                                                                    '')  # Remove righ wall of nextPos
                solution[(nextPos[0], nextPos[1])] = current[0], current[1]

        else:  # Means it is in the same column
            if nextPos[0] > current[0]:  # Means we go down
                direction = 'd'
                maze[current[0]][current[1]] = maze[current[0]][current[1]].replace('d',
                                                                                    '')  # Remove down wall of current
                maze[nextPos[0]][nextPos[1]] = maze[nextPos[0]][nextPos[1]].replace('u',
                                                                                    '')  # Remove up wall of nextPos
                solution[(nextPos[0], nextPos[1])] = current[0], current[1]

            else:  # Means we go up
                direction = 'u'
                maze[current[0]][current[1]] = maze[current[0]][current[1]].replace('u',
                                                                                    '')  # Remove up wall of current
                maze[nextPos[0]][nextPos[1]] = maze[nextPos[0]][nextPos[1]].replace('d',
                                                                                    '')  # Remove down wall of nextPos
                solution[(nextPos[0], nextPos[1])] = current[0], current[1]

        # Update position of current and add it to visited and remove it from unvisited
        current = nextPos
        if current not in visited:
            visited.append(current)

        if current in unvisited:
            unvisited.remove(current)

    # If there are no possible movements
    else:
        # If we are not in the initial situaltion of only (0, 0) in visited
        if len(visited) > 1:
            visited = visited[:-1]  # We remove the last element to go one step back since we are in a dead end
            current = visited[-1]  # We update current to be the new last element

        else:
            current = (0, 0)
            drawing = False


    return maze, current, visited, unvisited, solution, drawing

def solution_plot(x, y, surface, square_size):
    pygame.draw.rect(surface,
                     (0, 255, 0),
                     (y * square_size + square_size/2,
                      x * square_size + square_size/2,
                      square_size/4,
                      square_size/4),
                      0
                     )

screen = pygame.display.set_mode((WIDTH, HEIGHT))

def find_route(start, end, square_size):
    solving = True
    x, y = end[0], end[1]
    solution_plot(x, y, screen, SQUARE_SIZE)

    pygame.draw.rect(screen,
                     (255, 0, 0),
                     (y * square_size ,
                      x * square_size ,
                        square_size,
                      square_size),
                      0
                     )

    path = []
    while (x, y) != (start[0], start[1]):
        solution_plot(x, y, screen, SQUARE_SIZE)
	time.sleep(0.3)
        path.append((x, y))
        x, y = solution[x , y]
        solving = False
    return path, solving
