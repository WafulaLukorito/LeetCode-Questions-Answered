"""
Letter Combinations of a Phone Number
Medium
Leetcode: 17
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
"""

class Solution:
    
    def backtracking(self, ans, cur, digits, index, mapping):
        if index==len(digits):
            ans.append(cur[:])
            return
        for letter in mapping[digits[index]]:
            cur.append(letter)
            self.backtracking(ans, cur, digits, index+1, mapping)
            cur.pop()
    
    def letterCombinations(self, digits):
        if len(digits)==0:
            return []
        mapping = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
                   "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        ans=[]
        cur=[]
        self.backtracking(ans, cur, digits, 0, mapping)
        return ans

solution = Solution()

# Test case
digits = "23"
expected_output = ["ad","ae","af","bd","be","bf","cd","ce","cf"]

output = solution.letterCombinations(digits)

if output==expected_output:
    print ("Test Passed!", output)