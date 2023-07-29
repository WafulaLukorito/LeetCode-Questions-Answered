
"""
You are climbing a stair case. It takes n steps to reach to the top. Each time you can either climb 1 or 2 steps.
In how many distinct ways can you climb to the top?

Easy: DP

link: https://leetcode.com/problems/climbing-stairs/

Time Complexity: O(N)
Space Complexity: O(N)

"""

def climb_stairs(n):
    nums_cum = [0]*(n+1)
    nums_cum[0]=0
    nums_cum[1]=1
    
    for i in range (2, n+1):
        nums_cum[i]=nums_cum[i-1]+2
        
    return nums_cum[-1]

print (climb_stairs(5))