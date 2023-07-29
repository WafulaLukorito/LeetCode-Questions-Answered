
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
  """  
This approach works in O(n) time and O(n) space. However, as we only need the last two values of dp to calculate the next value, we can optimize the space to O(1) by using two variables to store the last two values. This is an example of the space-optimized version:

"""

def climbStairs(n):
    if n <= 2:
        return n
    a, b = 1, 2
    for i in range(3, n + 1):
        a, b = b, a + b
    return b