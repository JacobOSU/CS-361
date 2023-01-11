# Name: Jacob Summers
# Date: 11.9.22
# Course: CS 325 Section 400
# Assignment 7

import heapq

def minEffort(puzzle):
    """Method uses minheap with dijkstra's algorithm to find the shortest path in a m x n grid starting from point 0,0
    ending at space[m][n]. The method then returns the space crossed in the shortest path which took the most effort,
    which is calculated as the difference between the values at each space."""
    return (dijkstra(puzzle))

def dijkstra(graph):
    m, n = len(graph) - 1, len(graph[0]) - 1
    distances = [[10**10]*len(graph[0]) for i in range(len(graph))]
    distances[0][0] = 0
    cardinal_directions = [0, 1, 0, -1, 0]

    pq = [(0,0,0)]
    while len(pq) > 0:
        effort, row, column = heapq.heappop(pq)
        if effort > distances[row][column]:
            continue
        if row == m and column == n:
            return effort
        for neighbor in range(4):
            new_row = row + cardinal_directions[neighbor]
            new_column = column + cardinal_directions[neighbor+1]
            if 0 <= new_row <= m and 0 <= new_column <= n:
                new_effort = max(effort, abs(graph[new_row][new_column] - graph[row][column]))
                if new_effort < distances[new_row][new_column]:
                    distances[new_row][new_column] = new_effort
                    heapq.heappush(pq, (new_effort, new_row, new_column))

puzzle = [[1,3,5],[2,8,3],[3,4,5]]
print(minEffort(puzzle))
