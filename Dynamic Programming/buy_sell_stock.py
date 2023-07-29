
"""
    121. Best Time to Buy and Sell Stock
    Easy: DP
    
    link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
    
    Given an array of integers prices where prices[i] is the price of a given stock on the ith day.
    You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
    Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
    
    Example 1:
    Input: prices = [7,1,5,3,6,4]
    Output: 5
    Explanation:
    Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
    Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
    
    Time Complexity: O(N) where N is the number of prices in the array
    Space Complexity: O(1)
    """
    
def max_profit(prices):
    buyPrice= float('infinity')
    profit = 0
    
    for i in range(len(prices)):
        if prices[i]< buyPrice:
            buyPrice=prices[i]
        curr_prof = prices[i] - buyPrice
        profit = max(profit, curr_prof)
    
    return profit

prices = [7,1,5,3,6,4]
print (max_profit(prices))