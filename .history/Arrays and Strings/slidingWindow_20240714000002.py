"""

1. Maximum Sum Subarray of Size K (easy)  Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any contiguous subarray of size ‘k’.
  
    
"""
    
def max_sun_subarray(arr, k):
    
    if len(arr) < k:
        return, "Invalid Array!"
    
    max_sum = sum(arr[:k])
    window_sum = max_sum
    
    for i in range (len(arr) - k):
        window_sum = window_sum - arr[i] + arr[i+k]
        max_sum = max(max_sum, window_sum)
        
    return max_sum

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = 3
print(max_sun_subarray(arr, k)) # 27