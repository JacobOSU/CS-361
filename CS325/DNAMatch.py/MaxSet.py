# Name: Jacob Summers
# Date: 10.20.22
# Course: CS 325 Section 400
# Assignment 4
# Description: Function takes array and returns the maximum sum subsequence of nonconsecutive elements.


def max_independent_set(nums):
    """Takes array of numbers as parameter and returns the subsequence of numbers that results in the largest sum
    with the requirement that no two numbers in the sum are consecutive numbers in the array. Returns the resulting
    subsequence."""
    i = 0
    cache = [None]*len(nums)
    new_cache = []
    if len(nums) == 0:
        return []

    while i < len(nums):
        if i == 0:
            cache[i] = nums[0]
        if i == 1:
            cache[i] = max(nums[1], nums[0])
        if i > 1:
            cache[i] = max(cache[i-1], nums[i] + cache[i-2], nums[i])

        i += 1

    if cache[-1] < 0:
        return []
    if cache[-1] == 0:
        return [0]

    i = len(nums) - 1
    while i > 1:
        if cache[i] - nums[i] == cache[i-2] or cache[i] - nums[i] <= 0:
            if nums[i] > 0:
                new_cache.append(nums[i])
            i -= 2
        else:
            i-=1
    if i == 1:
        last_element = max(nums[i], nums[i-1])
        if last_element > 0:
            new_cache.append(last_element)
    if i == 0:
        if nums[i] > 0:
            new_cache.append(nums[i])

    new_cache.reverse()
    return new_cache


#nums = [-1, -1, -1, 2, 3, 4, 5]
#print(max_independent_set(nums))