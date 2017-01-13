"""
Fle for EPR exercise 10.2.
"""

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,Circle
import numpy as np


def display(maze, position, goal):
    """
    draw the labyringth, current position, goal and the shortest path
    """
    fig = plt.figure(0)
    fig.clf()
    ax = plt.gca()
    for x in range(maze.shape[1]):
        for y in range(maze.shape[0]):
            if maze[y,x] == 0:
                ax.add_patch(Rectangle((x-.5,y-.5), 1., 1., alpha=1))

    ax.add_patch(Circle((position[0], position[1]), .3,color='yellow', alpha=1))
    ax.add_patch(Circle((goal[0], goal[1]), .3, color='red', alpha=1))

    plt.xlim(-.5, maze.shape[1]-.5)
    plt.ylim(-.5, maze.shape[0]-.5)
    ax.invert_yaxis()
    plt.show()


def get_neighbors(maze, x, y):
    """
    utility-function to compute _valid_ neighbors of a cell,
    so we do not index out of bounds
    """
    n = []
    if x+1 < maze.shape[1]:
        n.append([x+1, y])
    if x-1 >= 0:
        n.append([x-1, y])
    if y+1 < maze.shape[0]:
        n.append([x, y+1])
    if y-1 >= 0:
        n.append([x, y-1])
    return n


def create_graph(maze):
    """
    compute the graph representation of the map
    """
    graph = {}
    
    
    # your code here
    
    return graph


maze = np.array([[0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 1, 0, 1, 0, 0, 1, 0],
                 [0, 1, 1, 1, 1, 1, 1, 0],
                 [0, 1, 1, 1, 0, 1, 0, 0],
                 [0, 1, 0, 0, 0, 1, 0, 0],
                 [0, 1, 1, 0, 1, 0, 1, 0],
                 [0, 1, 1, 1, 1, 1, 1, 0],
                 [0, 0, 0, 0, 0, 0, 1, 1]
        ])

graph = create_graph(maze)

