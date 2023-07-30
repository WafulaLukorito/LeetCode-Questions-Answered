
    """
    LeetCode Problem 5: Longest Palindromic Substring
    Medium: DP, String
    Link: https://leetcode.com/problems/longest-palindromic-substring/
    
    Given a string s, return the longest palindromic substring in s.
    
    """

def longest_palindrome(s):
    n = len(s)
    if n<=2:
        return s if s == s[::-1] else s[0]
    
    dp=[[False for _ in range (n)] for _ in range (n)]
    start=0
    max_size=0
    
    #For 1 char .. Every char is palindrome
    for i in range(n):
        dp[i][i]= True
        max_size = 1
    
    #for 2 char
    
    for i in range(n-1):
        if s[i]==s[i+1]:
            dp[i][i+1]=True
            start=i
            max_size=2
            
    #For 3 char+
    
    for window_size in range (3, n+1):
        for i range(n-window_size +1):
            end = i+ window_size -1
            if s[i]==s[end] and dp[i+1][end-1]:
                dp[i][j]=True
                start = i
                max_size=window_size
                
    return s[start:start+max_size]
                
            