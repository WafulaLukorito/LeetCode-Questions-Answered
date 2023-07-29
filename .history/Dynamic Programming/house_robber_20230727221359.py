
"""
#! Leetcode: 198. House Robber
Link: https://leetcode.com/problems/house-robber/

You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is
that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
Given a list of non-negative integers representing the amount of money of each house,
determine the maximum amount of money you can rob tonight without alerting the police.

Easy: DP

"""

def rob (nums):
    if not nums:
        return 0
    
    n = len(nums)
    
    max_cum_array= [0]*n
    max_cum_array[0]=nums[0]
    
    for i in range (1, n):
        if i == 1:
            max_cum_array[1]=max(nums[0],nums[1])
        else:
            max_cum_array[i]= max(max_cum_array[i-1], max_cum_array[i-2]+nums[i])
    
    return max_cum_array[-1]

print (rob([1,2,3,1])) # 4
print (rob([2,7,9,3,1])) # 12