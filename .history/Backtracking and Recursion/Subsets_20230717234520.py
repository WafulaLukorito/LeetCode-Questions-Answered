"""Leetcode Problem #78: Subsets
    Given a set of distinct integers, nums, return all possible subsets (the power set).
        Note: The solution set must not contain duplicate subsets.
"""

class Solution:
    def solution(self, nums, ans, cur, index):
        if index > len(nums):
            return
        ans.append(cur[:])
        for i in range(index, len(nums)):
            if nums[i] not in cur:
                cur.append(nums[i])
                self.solution(nums, ans, cur, i+1)
                #Decision not to include
                cur.pop()
        return

    def subsets(self, nums):
        ans = []
        cur = []
        self.solution(nums, ans, cur, 0)
        return ans

