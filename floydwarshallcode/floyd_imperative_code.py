"""
This is the imperative code from the PDF.
"""

import sys
import itertools
NO_PATH = sys.maxsize

def floyd_warshall(distance):
    """ 
    A simple implementation of Floyd's algorithm.
    """
    MAX_LENGTH = len(distance[0])

    for intermediate, start_node,end_node\
    in itertools.product\
    (range(MAX_LENGTH),range(MAX_LENGTH), range(MAX_LENGTH)):
        # Assume that if start_node and end_node are the same
        # then the distance would be zero
        if start_node == end_node:
            distance[start_node][end_node] = 0
            continue

        #return all possible paths and find the minimum
        distance[start_node][end_node] = min(distance[start_node][end_node],
                                             distance[start_node][intermediate]+\
                                             distance[intermediate][end_node])
    #Any value that have sys.maxsize has no path
    print_solution(distance,MAX_LENGTH)
    return distance




# A utility function to print the solution
def print_solution(distance,MAX_LENGTH):
    """
    The print function used to display the Floyd-Warshall graph[i][j]
    
    :param dist: The graph represented as a matrix where graph[i][j] is the distance from i to j.
	:param v: The number of vertices in the graph
    """

    print("Following matrix shows the shortest distances between every pair of vertices")
    for i in range(MAX_LENGTH):
        for j in range(MAX_LENGTH):
            if distance[i][j] == NO_PATH:
                print(f"{'INF':^8}", end=" ")
            else:
                print(f"{distance[i][j]:^8}", end=" ")
            if j == MAX_LENGTH-1:
                print()


#graph = [[0,7,NO_PATH,8],
        # [NO_PATH,0,5,NO_PATH],
        # [NO_PATH,NO_PATH, 0,2],
        #[NO_PATH,NO_PATH,NO_PATH,0]]

#floyd(graph)
