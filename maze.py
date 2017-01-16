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
import random


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

        
def create_node_list(maze):
    """Creates a list of every viable node (not wall) of the maze"""
    
    n_list = []

    for i in range(maze.shape[1]):
        for j in range(maze.shape[0]):

            if maze[i][j] == 1:
                node = str(j) + ":" + str(i)
                n_list.append(Node(node))

    return n_list


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

            
def display(maze, start, goal, path):
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

    #displays the start of the path with a yellow circle
    ax.add_patch(Circle((start[0], start[2]), .3,color='yellow', alpha=1))

    # displays evry step of the path with a green circle
    # only if the path exists

    if path:        
        for node in path[1:-1]:
            ax.add_patch(Circle((node[0], node[2]),
                                .3,color='green', alpha=1))
    else: pass
        
    # displays the goal of the path with a red circle
    ax.add_patch(Circle((goal[0], goal[2]), .3, color='red', alpha=1))

    plt.xlim(-.5, maze.shape[1]-.5)
    plt.ylim(-.5, maze.shape[0]-.5)
    ax.invert_yaxis()
    plt.show()


def depth_search_simple(graph, top_level, goal, path = []):
    """Searchs the nodes for a path from start to goal"""
    
    path = path + [top_level]

    # if the goal was reached, stop the search
    if top_level == goal:
        return path
    
    # look in the under levels of the node (expand), to search for the goal
    for node in graph[top_level]:

        # see if this path was already visited (avoid loops)
        if node not in path:

            # repeat the search for every node of the under level
            under_level = depth_search_simple(graph, node, goal, path)

            # return if the node has no branches to expand
            if under_level:
                return under_level
    return None


# modified search to output all the paths

def depth_search_all(graph, top_level, goal, path=[]):
    """Populates the list of all possible paths"""
    
    path = path + [top_level]

    # if a (new) path was found, append it to the paths' list
    if top_level == goal:
        path_list.append(path)

    # look in the under levels of the node (expand), to search for the goal       
    for node in graph[top_level]:

        # see if this path was already visited (avoid loops)
        if node not in path:
            
            # repeat the search for every node of the under level
            under_level = depth_search_all(graph, node, goal, path)

            # return if the node has no branches to expand
            if under_level:
                return under_level
    return None
    
#################

def main():
    """Runs the program"""

    #### Aufgabe 6.2 a) Graph-Repräsentation

    try:
        # Create the valid nodes' list    
        node_list = create_node_list(maze)

        # Create and print the graph of the nodes for this maze
        graph = create_graph(maze, node_list)
        
        print("\nThe graph representation for this maze is:")
        pprint.pprint(graph)

    except Exception:
        print("No valid maze was given!")



    #### Aufgabe 6.2 b) Berechnen ob es einen Pfad zu seinem Ziel gibt
    path =[]
    
    # Set start and end nodes                             
    start = "1:1"
    goal = "7:7"

    # Search for existing paths (no loops), given the allowed movement
    # for the robot. Use the function depth_search_simple    
    try:
        path = depth_search_simple(graph,start,goal)
        
        # output if a path can be followed
        if path:
            print("\nAt least one path exist from {} to {}.".
                  format(start, goal))
        else:
            print("\nFor this maze there is no path from {} to {}.".
                  format(start, goal))

    #### Aufgabe 6.2 c) Berechne alle möglichen Pfade
                  
        global path_list
        path_list = []

        # populate the path list with the function depth_search_all,
        # which looks for all possible paths:
        depth_search_all(graph, start, goal)

        # output all the possible paths
        if path_list:
            print("\nPossible path(s): {}".format(len(path_list)),
                  *path_list, sep = "\n", end = "\n")
        else:
            pass


    #### Aufgabe 6.2 d) Kürzester Pfad von start bis goal

        # Create a dictionary with the path and it's necesary steps
        path_dict = {}

        if path_list:
            
            for path in path_list:
                path_dict[tuple(path)] = len(path) - 1

            # get the path(s) which need(s) the least steps
            min_steps = min(path_dict.values())

            # make a list with the paths that need these minimum steps
            shortest_path = [path for path, steps
                             in path_dict.items() if steps == min_steps]

            print("\nShortest path(s): {}".format(len(shortest_path)),
                  *shortest_path, sep = "\n", end = "\n")

        else:
            print("No shortest: There are no possible paths")

        
    #### Aufgabe 6.2 e) Display Funktion

        # Display the maze and the shortest path
        # Modified version of display function was used (from line 105)

        if path_list:
            
            # if there is only one short path, display it;
            # if there are more, choose one randomly for display
            
            shortest = random.choice(shortest_path)
            display(maze, start, goal, shortest)

        else:
            display(maze, start, goal, [])


    except Exception:
        print("Start or goal not valid!")
    


if __name__ == "__main__":
    main()


