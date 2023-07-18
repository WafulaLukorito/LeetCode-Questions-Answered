"""
Letter Combinations of a Phone Number
Medium
Leetcode: 17
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

"""
class Solution:
    def backtracking(self, digits, m, cur, ans, index):
        if (index > len(digits)):
            return
        if (len(cur)==len(digits)):
            ans.append(cur[:])
            return
        
        currentDigit = digits[index]
        currentString = m[currentDigit]
        
        
        #!Important
        for i in range(len(currentString)):
            self.backtracking(digits, m, cur+currentString, ans, index+1)
        
    def combinations(self, digits):
        ans = []
        if (len(digits)==0):
            return ans
        
        m = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
                   "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        
       
        cur = ""
        self.backtracking(digits, m, cur, ans, 0)
        return ans

solution = Solution()

# Test case
digits = "23"
expected_output = ["ad","ae","af","bd","be","bf","cd","ce","cf"]

output = solution.combinations(digits)

if output==expected_output:
    print ("Test Passed!", output)
