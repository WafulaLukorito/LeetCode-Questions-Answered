
    """
    Description: Given a list of weights and values, find the maximum value that can be obtained by taking weights such that the sum of the weights is less than or equal to a given limit. You cannot break an item, either pick the complete item or don’t pick it (0-1 property).
    
    Link: https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/
    
    Complexity: O(n) time, O(n) space
    

    Returns:
        _type_: _description_
    """

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