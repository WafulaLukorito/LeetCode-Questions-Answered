
    """
    322. Coin Change
    Medium
    
    Link: https://leetcode.com/problems/coin-change/
    
    You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount.
    
    
    """


def coinChange(coins, amount):
    # Base cases
    if amount <= 0:         # If the amount is less than or equal to zero, no coins are needed
        return 0
    if min(coins) > amount: # If the smallest coin is greater than the amount, return -1
        return -1
    
    # Initialize dynamic programming table, dp.
    # Each index, i, represents an amount of money, and dp[i] represents the fewest number of coins needed to make up the amount i.
    dp = [float('inf')] * (amount + 1)
    
    # Zero amount requires zero coins
    dp[0] = 0
    
    # Loop through the amounts up to the target amount
    for i in range(1, amount + 1):
        # For each coin, if it's less than or equal to the current amount, i,
        # update dp[i] to be the minimum of its current value and the value for amount (i - coin) plus 1.
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i - coin] + 1, dp[i])
    
    # Return the minimum number of coins needed to make up the amount.
    # If dp[amount] is still infinity, it means we can't make up the amount with the given coins, so return -1.
    return dp[amount] if dp[amount] != float('inf') else -1
