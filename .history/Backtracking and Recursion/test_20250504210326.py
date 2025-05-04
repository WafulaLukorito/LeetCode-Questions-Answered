class Solution:
    def solution(self, nums, ans, cur, index):
        if index > len (nums):
            return
        ans.append(cur[:])
        for i in range (index, len(nums)):
            if nums[i] not in cur:
                cur.append(nums[i])
                self.solution(nums, ans, cur, i+1)
                cur.pop()
        
    def subsets(self, nums):
        cur = []
        ans = []
        self.solution(nums, ans, cur, 0)
        return ans

# Test case
nums = [1, 2, 3]
expected_output = [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]

output = solution.subsets(nums)

if output==expected_output:
    print ("Test Passed!", output)