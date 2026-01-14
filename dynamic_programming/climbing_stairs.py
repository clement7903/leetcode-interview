"""
Given an input integer n, count the number of distinct ways to climb to n using just 1 or 2 steps each time.
"""
def climbStairs(n: int, cache = {1: 1,2: 2}) -> int: 
    """
    Brute force approach is to iterate through all possible unique combinations of 1s & 2s until the floor is reached. There are 2 possible ways to solve:
    a. Use n as the starting value, keep deducting n until reaches 0. Increase the counter by 1. Repeat this loop... This will be too slow!

    b. Recognise that the way to 
        n = 1:
        1 -> 1 
        => the number of ways to climb is just 1 (aka. 1 step)

        n = 2:
        2 -> 1 + 1
        2 -> 2
        => the number of ways to climb is 2 (aka. take 1 step followed by another step OR take 2 steps at once)

        n = 3:
        3 -> 1 + 1 + 1
        3 -> 1 + 2
        3 -> 2 + 1
        => the number of ways to climb is 3 (aka. if 1st step taken = 1, then the number of ways to climb remainder 2 steps is climbStairs(2). If 1st step taken = 2, then the number of ways to climb remainer 1 step is climbStairs(1).)

        n = 4:
        => if 1st step taken = 1, then the number of ways to climb remainder 3 is climbStairs(3). if 1st step taken = 2, then number of ways to climb remainder 2 is climbStairs(2).
    """
    if n in cache:
        return cache[n]
    else:
        cache[n] = climbStairs(n-1) +climbStairs(n-2)

    return climbStairs(n)

print(climbStairs(45))