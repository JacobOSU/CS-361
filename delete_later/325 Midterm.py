
def canSum(targetSum, numbers, memo={}):
    if targetSum == 0:
        return True
    if targetSum < 0:
        return False
    if targetSum in memo:
        return memo[targetSum]
    for element in range(len(numbers)):
        remainder = targetSum - numbers[element]
        if canSum(remainder, numbers, memo) is True:
            memo[targetSum] = True
            return True
    for key in memo:
        print(key, memo[key])
    return False



def howSum(targetSum, numbers, memo={}):
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None
    if targetSum in memo:
        return memo[targetSum]
    for index in range(len(numbers)):
        remainder = targetSum - numbers[index]

        remainderResult = howSum(remainder, numbers, memo)
        if remainderResult is not None:
            return [numbers[index]]

    return None

print(howSum(7, [2,3]))