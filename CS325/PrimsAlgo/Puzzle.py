# Name: Jacob Summers
# Date: 11.20.22
# Course: CS 325 Section 400
# Assignment 8
# Description: Program uses BFS to find the shortest path in a 2D maze.

import copy


def solve_puzzle(Board, Source, Destination):
    """Function uses BFS to find the shortest distance between start and ending vertices on 2D graph. Function returns
    the vertices visited of shortest path or None if no path is possible."""
    board_copy = copy.deepcopy(Board)
    puzzle_answer = dijkstra(board_copy, Source, Destination)
    return puzzle_answer


def dijkstra(graph, start, end, path=None, answer=None):
    if path is None:
        path = []
        answer = []

    source = start

    x, y = start
    m, n = end
    cardinal_directions = [0, 1, 0, -1, 0]

    if graph[0] == '-':
        while x <= n:
            if graph[x] == '-':
                path.append((0, x))
                x += 1
        if x == n + 1:
            return path

    if len(graph[0]) == 1:
        print('graph is: ', graph)
        if x < m:
            while x <= m and 0 <= x <= len(graph) - 1:
                if graph[x] == ['-']:
                    path.append((x, 0))
                    x += 1
            if x == m + 1:
                print('wtf path: ', path)
                return path
        if x > m:
            while x >= m and 0 <= x <= len(graph) - 1:
                if graph[x] == ['-']:
                    path.append((x, 0))
                    x -= 1
            if x == m - 1:
                print('wtf path: ', path)
                return path

    if x == m and y == n:
        answer.append(copy.deepcopy(path))
    graph[x][y] = '#'
    neighbor = 0
    next_start = start
    while neighbor < 4 and next_start != end:
        new_row = x + cardinal_directions[neighbor]
        new_column = y + cardinal_directions[neighbor + 1]
        if new_row >= 0 and new_row <= len(graph) - 1 and new_column >= 0 and new_column <= len(graph[0]) - 1:
            if graph[new_row][new_column] == '-':
                path.append((new_row, new_column))
                next_start = new_row, new_column
                dijkstra(graph, next_start, end, path, answer)
        neighbor += 1
    graph[x][y] = '-'

    if answer is None or len(answer) == 0:
        return None
    shortest_path = len(answer[0])

    for paths in answer:
        if len(paths) < shortest_path:
            shortest_path = len(paths)

    for all_paths in answer:
        if len(all_paths) == shortest_path:
            the_answer = all_paths
    submit = []
    submit.append(source)
    for element in the_answer:
        submit.append(element)
    return submit


# Puzzle = [
#    ['-', '-', '-', '-', '-'],
#     ['-', '-', '#', '-', '-'],
#     ['-', '-', '-', '-', '-'],
#     ['#', '-', '#', '#', '-'],
#     ['-', '#', '-', '-', '-']]


# Puzzle2 = [
#    ['-', '-', '-'],
#    ['-', '-', '-'],
#    ['-', '-', '-']]

# Puzzle3 = ['-', '-', '-', '-']
#puzzle4 = [['-'], ['-'], ['-'], ['-'], ['-']]

# start_1 = (0,0)
# end_1 = (4,4)

# start_2 = (0,2)
# end_2 = (2,2)

# start_3 = (0,0)
# end_3 = (4, 0)
# print(solve_puzzle(Puzzle, start_2, end_2))
# print(solve_puzzle(Puzzle, start_1, end_1))
# print(solve_puzzle(Puzzle, start_3, end_3))

# start4 = (3, 0)
# end4 = (0, 0)
# print(solve_puzzle(puzzle4, start4, end4))

