
"""
You are climbing a stair case. It takes n steps to reach to the top. Each time you can either climb 1 or 2 steps.
In how many distinct ways can you climb to the top?

Easy: DP

link: https://leetcode.com/problems/climbing-stairs/

Time Complexity: O(N)
Space Complexity: O(N)

"""

def climb_stairs(n):
    nums_cum = 