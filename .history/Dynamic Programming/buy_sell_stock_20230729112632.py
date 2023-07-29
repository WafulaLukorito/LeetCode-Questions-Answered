
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
    
def max_profit(arr):
    n = len(arr)
    max_prof=[-float('infinity')]*n
    max_prof[0]=0
    
    for i in range (1, n):
        curr_prof = nums[i] - max_prof[i-1]
        max_prof[i] = max(curr_prof, max_prof[i-1])
        i+=1
    return max_prof[-1]

prices = [7,1,5,3,6,4]
print (max_profit(prices))