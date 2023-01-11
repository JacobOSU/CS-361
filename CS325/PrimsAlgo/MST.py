# Name: Jacob Summers
# Date: 11.17.22
# Course: CS 325 Section 400
# Assignment 8
# Description: Method uses Prim's algorithm to make a Minimum Spanning tree with of parameter passed graph. I spent
#               several days trying to get the min heap implementation and could not figure it out in time. Used brute
#               force implementation from module as baseline and altered it to work with all connected graphs.

import heapq

def Prims(G):
    """Uses Prim's algorithm to create an MST connecting all vertices in parameter passed graph with the minimum
    weighted edges. Input: graph passed to method via adjacency matrix, with a list containing lists of each edge weight
    to every other vertex in the graph. If vertices are not connected, weight is 0. Output: returns list of tuples which
    each contain two vertices and an edge weight, indicating which edges were connected connected to form the MST;
    including the weights of the edges used in the MST. In summary, the output will be a list of tuples in the format
    (v1, v2, w), with v1 and v2 representing the vertices used in the MST, and w being the weight of the edge
    between them. Order of vertices/edge in the tuple does not matter."""
    infinity = 10**10
    Vertices = len(G)
    answer = []
    visited = [0]*len(G)
    no_edge = 0
    visited[0] = True

    while (no_edge < Vertices - 1):
        minimum = infinity
        x = 0
        y = 0
        for i in range(Vertices):
            if visited[i]:
                for j in range(Vertices):
                    if ((not visited[j]) and G[i][j]):
                        if minimum > G[i][j]:
                            minimum = G[i][j]
                            x = i
                            y = j
        answer.append((x, y, G[x][y]))
        visited[y] = True
        no_edge += 1

    return answer

#graph_matrix = [[0, 8, 5, 0, 0, 0, 0], [9, 0, 10, 2, 18, 0, 0], [5, 10, 0, 3, 0, 16, 0],
 #               [0, 2, 3, 0, 12, 30, 14], [0, 18, 0, 12, 0, 0, 4], [0, 0, 16, 30, 0, 0, 26], [0, 0, 0, 14, 4, 26, 0]]
#print(Prims(graph_matrix))