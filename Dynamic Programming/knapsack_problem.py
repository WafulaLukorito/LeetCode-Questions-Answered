"""
Given values and weights of n items, we want to put these items in a knapsack of capacity W to get the maximum total value in the knapsack.

"""
#Convert code to java

from collections import defaultdict


def knaps (weights, values, defaultdict = defaultdict(int)):
    
    n = len(weights)
    if n==0:
        return 0
    dp = [0]*n
    
    for weight in weights:
        if weight <= knapsack:
            dp[weight] = max(dp[weight], dp[knapsack-weight]+values[weight])
    
    return dp[-1]

print(knaps([1,2,3,1], [1,2,3,1], 4)) # 4