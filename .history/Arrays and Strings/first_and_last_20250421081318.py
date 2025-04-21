"""Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 """
class Solution():
    def first_and_last(self, nums, target):
        if not nums:
            return (-1, -1)
        return (self.get_left(nums, target), self.get_right(nums, target))
    
    def get_left(self, nums, target):
        left = 0
        right = len(nums) - 1
        result = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                result = mid  # Store the latest valid position
                right = mid - 1  # Continue searching left
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return result

    def get_right(self, nums, target):
        left = 0
        right = len(nums) - 1
        result = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                result = mid  # Store the latest valid position
                left = mid + 1  # Continue searching right
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return result


s = Solution()
nums = [5, 7, 7, 8, 8, 8, 8, 8, 10]
target = 8
result = s.first_and_last(nums, target)
print(result)  # Output: (3, 7)