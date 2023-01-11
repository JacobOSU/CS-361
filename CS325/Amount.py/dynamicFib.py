# Function returns nth number in fibonacci sequence.
# Time complexity: O(n)
# Space complexity: O(n)


def fib(n, memo=None):
    """Function returns the nth number in the fibonacci sequence using recursion and dynamic programming."""
    if memo is None:
        memo = {}
    if n <= 2:
        return 1
    if n in memo:
        return memo[n]
    return fib(n-1) + fib(n-2)

list = [1,2,3,4,5,6,7,8,9]
for element in list:
    print(fib(element))