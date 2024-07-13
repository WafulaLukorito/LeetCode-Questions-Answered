"""

1. Maximum Sum Subarray of Size K (easy)  Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any contiguous subarray of size ‘k’.
  
    
"""

def max_sub_array_of_size_k(k, arr):
    #Time complexity O(n)
    if len(arr) < k:
        return -1
    
    max_sum = sum(arr[:k])
    window_sum = max_sum
    
    for i in range (len(arr)-k):
        window_sum = window_sum - arr[i] + arr[i+k]
        max_sum = max(max_sum, window_sum)
        
    return max_sum

my_arr = [2, 1, 5, 1, 3, 2]
k = 3
print(max_sub_array_of_size_k(k, my_arr)) #9

    """
    2. Longest Substring without repeating characters (medium) Given a string, find the length of the longest substring which has no repeating characters.
    """

def non_repeat_substring(str):
    #Time complexity O(n)
    window_start = 0
    max_length = 0
    char_index_map = {}
    
    for window_end in range(len(str)):
        right_char = str[window_end]
        
        if right_char in char_index_map:
            window_start = max(window_start, char_index_map[right_char] + 1)
        
        char_index_map[right_char] = window_end
        max_length = max(max_length, window_end - window_start + 1)
        
    return max_length