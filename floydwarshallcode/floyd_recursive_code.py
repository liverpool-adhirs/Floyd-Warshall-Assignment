"""
This is the recursive Floyd-Warshall algorithm.
"""

INF = float('inf')
# if there is no distance between two vertices, INF as the variable to represent this.

def floyd_warshall_recursive(dist, k, i, j, n):
    """
    A recursive version of the Floyd-Warshall algorithm.
    
    :param dist: The distance matrix where dist[i][j] is the shortest distance from i to j
    :param k: The current index of the vertex being considered as an intermediate vertex
    :param i: The current source vertex
    :param j: The current destination vertex
    :param n: The total number of vertices in the graph
    """
    # Base case: When all vertices have been considered as intermediate vertices
    if k == n:
        return dist[i][j]

    # Recursive case: Consider vertex k as an intermediate vertex and update dist[i][j]
    #Path without vertex k
    path_without_k = floyd_warshall_recursive(dist, k + 1, i, j, n)
    # Path with vertex k
    path_with_k = floyd_warshall_recursive(dist, k + 1, i, k, n) + \
             floyd_warshall_recursive(dist, k + 1, k, j, n)

    # Update the shortest path using the minimum  of these 3 values.
    dist[i][j] = min(dist[i][j], path_without_k, path_with_k)

    return dist[i][j]

def floyd_warshall(graph):
    """
    Initializes the distance matrix and starts the recursive process.
    
    :param graph: The graph represented as a matrix where graph[i][j] is the distance from i to j
    """
    n = len(graph)
    # Initialize distance matrix
    dist = [[graph[i][j] for j in range(n)] for i in range(n)]

    # Start the recursive process for each pair (i, j)
    for i in range(n):
        for j in range(n):
            floyd_warshall_recursive(dist, 0, i, j, n)
    print_solution(dist,n)
    return dist


# A utility function to print the solution
def print_solution(dist,n):
    """
    The print function used to display the Floyd-Warshall graph[i][j]
    
    :param dist: The graph represented as a matrix where graph[i][j] is the distance from i to j.
	:param v: The number of vertices in the graph
    """

    print("Following matrix shows the shortest distances between every pair of vertices")
    for i in range(n):
        for j in range(n):
            if dist[i][j] == INF:
                print(f"{'INF':^8}", end=" ")
            else:
                print(f"{dist[i][j]:^8}", end=" ")
            if j == n-1:
                print()
