

def canSum(targetSum, numbers, memo=None):
    """Function returns boolean indicating if possible to generate target sum using numbers from array."""
    if targetSum == 0:
        return True
    if targetSum < 0:
        return False
    if memo is None:
        memo = {}
    if targetSum in memo:
        return memo[targetSum]
    for index in range(len(numbers)):
        remainder = targetSum - numbers[index]
        if canSum(remainder, targetSum, memo) is True:
            memo[targetSum] = True
        return True

    memo[targetSum] = False
    return False




target = 7
nums = [2,3]

print(canSum(target, nums))
print(canSum(7, [5,3,4,7]))
print(canSum(7, [2,4]))
print(canSum(8, [2,3,5]))
print(canSum(300, [7,14]))