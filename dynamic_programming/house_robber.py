"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
"""

# Clarifications
# 1. What is the min & max length of the array?
# 2. How many can i rob in total?

# e.g. [4, 1, 10, 9]

# start with 4 -> rob([10,9 ])
# start with 1 -> rob[9]

def rob(nums: list[int]) -> int:
    """
    Naive approach is to iterate and find every possible combination of houses. But that will be too many possibilities.

    Instead try dynamic programming method, either start with robbing 1st or 2nd house:
    1. If rob 1st house, skip 2nd house, then rob the 3rd to the end of the list
    2. If rob 2nd house, skip 1st house & 3rd house, rob the 4th to end of the list

    The following solution might still be very slow for larger list... because there is a need to repeatedly string slice + there are repeated calculations done within each recursive call...
    """
    len_of_list = len(nums)

    # Special cases
    if len_of_list == 1:
        return nums[0]
    elif len_of_list == 2:
        return max(nums[0], nums[1])
    elif len_of_list == 3:
        return max(nums[0] + nums[2], nums[1])
    
    # all other cases
    return max(nums[0] + rob(nums=nums[2:]), nums[1] + rob(nums=nums[3:]))

def rob_optimal_bottom_up_approach(nums: list[int]) -> int:
    """
    At a house i, there are only 2 "local" options:
    1. Rob this house - aka (rob(nums[i-2]) + nums[i]))
    2. Skip this house - aka rob(nums[i-1])

    -> Objective: keep the previous 2 profits and calculate the current profit to decide whether to rob / do not rob this "i" house.

    e.g. [4, 1, 10, 9]

    At i = 0, prev_1 & prev_2 = 0 -> current = 4
    At i = 1, prev_1 = 4 | prev_2 = 0 -> current = 1 -> 
    """
    # Special cases
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    
    prev_2 = 0 
    prev_1 = 0
    # All other cases
    for house in nums:
        current = max(prev_1, prev_2 + house) # up till this house, this is the maximum amount.
        prev_2 = prev_1
        prev_1 = current
    return current

print(rob_optimal_bottom_up_approach([4, 1, 10, 9]))
