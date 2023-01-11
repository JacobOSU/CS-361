# Name: Jacob Summers
# Date: 11.28.22
# Course: CS 325 Section 400
# Assignment 9
# Description: Algorithm uses nearest neighbor heuristic approach to find approximate solution to TSP.

def solve_tsp(G):
    """Problem uses heuristic approach to solve the traveling salesman problem."""
    route = [0]
    solution_length = len(G[0]) + 1
    i = 0

    while len(route) < solution_length - 1:
        min_distance = 10 ** 10
        min_vertex = 0

        for j in range(len(G)):
            new_distance = G[i][j]
            if new_distance <= min_distance and new_distance != 0 and j not in route:
                min_distance = new_distance
                min_vertex = j
        route.append(min_vertex)
        i = min_vertex
    route.append(0)

    return route

#graph_matrix =   [
# [0, 2, 3, 20, 1],
# [2, 0, 15, 2, 20],
# [3, 15, 0, 20, 13],
# [20, 2, 20, 0, 9],
# [1, 20, 13, 9, 0],]
#print(solve_tsp(graph_matrix))