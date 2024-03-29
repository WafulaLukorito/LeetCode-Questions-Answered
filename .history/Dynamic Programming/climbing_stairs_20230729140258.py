﻿
"""
You are climbing a stair case. It takes n steps to reach to the top. Each time you can either climb 1 or 2 steps.
In how many distinct ways can you climb to the top?

Easy: DP

link: https://leetcode.com/problems/climbing-stairs/

Time Complexity: O(N)
Space Complexity: O(N)

"""
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        dp = [0]*(n+1)
        dp[1] = 1
        for i in range(2, n+1):
            if i == 2:
                dp[i] = 2
            else:
                dp[i] = dp[i-1] + dp[i-2]
        return dp[n]