# Function calculates number of ways to travel down a m x n grid.
# Time complexity: O(n*m)
# Space complexity: O(n+m)

def gridTraveler(x, y, memo=None):
    """Function calculates number of ways for a person to travel to a space in mxn grid using memoization and dynamic
     programming."""
    if memo is None:
        memo = {}
    if x or y == 1:
        return 1
    if x or y == 0:
        return 0
    key = x + "," + y
    if key in memo:
        return memo[key]
    memo[key] = gridTraveler(x-1, y, memo) + gridTraveler(x, y-1, memo)
    return memo[key]


#print(gridTraveler(1,1))
print(gridTraveler(2, 3))
print(gridTraveler(3,2))
print(gridTraveler(3,3))
print(gridTraveler(18,18))