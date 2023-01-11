# Name: Jacob Summers
# Date: 10.23.22
# Class: CS 325 Section 400
# Assignment 4, problem 2
# Description: Function takes a set as parameter and returns the power set.

import copy

def powerset(inputSet):
    """Method takes set as parameter and returns the powerset of the given set. Uses dynamic programming and backtracking
    to solve solution without solving for already solved solutions."""
    result = []
    pointer = len(inputSet) - 1
    powerset_helper(pointer, [], inputSet, result)
    return result

def powerset_helper(pointer, choices_made, input, result):
    """Helper method to powerset function."""
    if pointer < 0:
        result.append(copy.deepcopy(choices_made))
        return
    choices_made.append(input[pointer])
    powerset_helper(pointer-1, choices_made, input, result)
    choices_made.pop()
    powerset_helper(pointer -1, choices_made, input, result)

#test_set = [1,2,3]
#print(powerset(test_set))


