"""
Fle for EPR exercise 10.2.
"""

__author__ = "5625448: Lilian Mendoza de Sudan, 6290157: Lars Petersen"
__copyright__ = "Goethe Universitaet 2016"
__credits__ = "none" 
__email__ = "lilian_mendoza@hotmail.com, petersen@informatik.uni-frankfurt.de"


import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle
import numpy as np
import pprint
import time


maze = np.array([[0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 1, 0, 1, 0, 0, 1, 0],
                 [0, 1, 1, 1, 1, 1, 1, 0],
                 [0, 1, 1, 1, 0, 1, 0, 0],
                 [0, 1, 0, 0, 0, 1, 0, 0],
                 [0, 1, 1, 0, 1, 0, 1, 0],
                 [0, 1, 1, 1, 1, 1, 1, 0],
                 [0, 0, 0, 0, 0, 0, 1, 1]
        ])


class Node:
    """Instantiates a (viable) node from the maze."""
    
    def __init__(self, node):
        """Initializes a node"""
        
        self.node = node
        self.neighbors = get_neighbors(maze,
                                       int(self.node[0]),
                                       int(self.node[2]))
    
        self.reachable_neighbor = get_reachable_neighbors(self.neighbors)
        

    def __str__(self):
        """Outputs the information of a node"""

        info = "{}, {} \n{}".format(self.node, self.neighbors,
                                    self.reachable_neighbor)
        return info

        
def create_node_list(maze):
    """Creates a list of every viable node (not wall) of the maze"""
    
    n_list = []

    for i in range(maze.shape[1]):
        for j in range(maze.shape[0]):

            if maze[i][j] == 1:
                node = str(j) + ":" + str(i)
                n_list.append(Node(node))

    return n_list


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


def get_reachable_neighbors(neighbors_list):
    """Gets only the reachable neighbors to a node"""

    reachables = set()
    
    for neighbor in neighbors_list:
        if maze[int(neighbor[1])][int(neighbor[0])] == 1:
            reachables.add(
                (str(neighbor[0]) + ":" + str(neighbor[1]))
                )
    
    return reachables


def create_graph(maze, node_list):
    """
    compute the graph representation of the map
    """
    
    graph = {}
    
    for node in node_list:
        graph[node.node] = node.reachable_neighbor
            
    return graph

            
def display(maze, start, path, goal):
    """
    draw the labyrinth, current position, goal and the shortest path
    """
    
    fig = plt.figure(0)
    fig.clf()
    ax = plt.gca()
    for x in range(maze.shape[1]):
        for y in range(maze.shape[0]):
            if maze[y,x] == 0:
                ax.add_patch(Rectangle((x-.5,y-.5), 1., 1., alpha=1))

    #display the fastest path, begin at start
    ax.add_patch(Circle((start[0], start[1]), .3,color='yellow', alpha=1))
    
    for node in path:
        ax.add_patch(Circle((node[0], node[1]), .3,color='yellow', alpha=1))
        

    ax.add_patch(Circle((goal[0], goal[1]), .3, color='red', alpha=1))

    plt.xlim(-.5, maze.shape[1]-.5)
    plt.ylim(-.5, maze.shape[0]-.5)
    ax.invert_yaxis()
    plt.show()


#################

def main():
    """Runs the program"""

    # Create the valid nodes' list    
    node_list = create_node_list(maze)

    # Create and print the graph of the nodes for this maze
    graph = create_graph(maze, node_list)
    pprint.pprint(graph)

    # Set start and end nodes                             
    start = [1,1]
    goal = [7,7]

    display_path = [[1,2],[1,3],[1,4]]  #########VORLÄUFIG; ZUM TESTEN

    # Display the maze and the shortest path
    display(maze, start, display_path, goal)


if __name__ == "__main__":
    main()


