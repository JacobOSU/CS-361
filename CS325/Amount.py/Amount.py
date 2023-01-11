# Name: Jacob Summers
# Date: 10.31.22
# Course: 325 Section 400
# Assignment 5
# Description: Algorithm uses backtracking to return the elements within an array which add to the target sum value. 

import copy

def amount(A, S):
    """Method takes a list of values and a target sum as parameters, and returns lists which contain
    combinations of the numbers in the parameter passed array which add up to the target sum."""
    result = []
    amount_helper(A, 0, result, S, [])
    return result

def amount_helper(nums, start, result, remainder, combo):
    """Amount helper function."""
    if remainder == 0 and combo not in result:
        result.append(copy.deepcopy(combo))
        return
    elif remainder < 0:
        return
    for i in range(start, len(nums)):
        combo.append(nums[i])
        amount_helper(nums, i+1, result, remainder-nums[i], combo)
        combo.pop()


#A = [11, 1, 3, 2, 6, 1, 5]
#TargetSum = 8
#print(amount(A, TargetSum))