
"""
#! Leetcode: 198. House Robber
# Say you are a house robber who can't rob two adjacent houses. 
You are given a list of non-negative integers representing the amount of money of each house.
Determine the maximum amount of money you can rob tonight without alerting the police.
"""

# #? Time Complexity: O(N) --> N is the length of the input array. We will iterate through the array once.
# #? Space Complexity: O(N) --> N is the length of the input array. We will store the results in a separate array.

def rob(nums):
    n = len(nums)
    if n == 0:
        return 0
    
    dp = [0]*n 
    dp[0] = nums[0]

    for i in range(1, n):
        if (i ==1):
            dp[i] = max(nums[0], nums[1])
        else:
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
    
    return dp[-1]

print (rob([1,2,3,1])) # 4
print (rob([2,7,9,3,1])) # 12