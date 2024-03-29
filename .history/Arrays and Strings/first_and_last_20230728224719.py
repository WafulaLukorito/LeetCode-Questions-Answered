"""Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 """
# from typing import List
# class Solution:
#     def get_left(nums, target):
#         left = 0
#         right = len(nums) -1

#         while (left <= right):
#             mid = (left + right)//2
#             if (nums[mid] == target):
#                 if (mid-1 >= 0 and nums[mid-1] != target or mid == 0):
#                     return mid
#                 right = mid -1
#             elif (nums[mid] > target):
#                 right = mid -1
#             else:
#                 left = mid+1
#         return -1


#     def get_right(nums, target):
#         left = 0
#         right = len(nums) -1

#         while (left <= right):
#             mid = (left + right)//2
#             if (nums[mid] == target):
#                 if (mid + 1 >= 0 and nums[mid+1] != target or mid == len(nums) ):
#                     return mid
#                 left = mid+1
#             elif (nums[mid] > target):
#                 right = mid-1
#             else:
#                 left = mid +1
#         return -1

# def first_and_last( self, nums, target):
#     left = self.get_left(nums, target)
#     right = self.get_right(nums, target)
#     return  [left, right]

# * Second Attempt

class Solution():
    def first_and_last(self, nums, target):
        if not nums:
            return (-1, -1)
        if len(nums)==1:
            return (0, 0)
        return (self.get_left(nums,target), self.get_right(nums,target))
    
    def self.get_left(self, nums, target):
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left+right)//2
            if left == right:
                if nums[mid] == target:
                    if nums[mid-1] != target:
                        return mid
                    else:
                        return -1
            if nums[mid] == target:
                if nums[mid-1] !=target:
                    return mid
                else:
                    right = mid-1
            if nums[mid]> target:
                left = mid+1
            if nums[mid]<target:
                right = mid-1
        return -1

    def self.get_right(self, nums, target):
        left=0
        right=len(nums) -1
        while left <= right:
            mid = (left+right)//2
            if left == right:
                if nums[mid]==target:
                    if nums[mid+1] != target:
                        return mid
                    else:
                        return -1
            
            if nums[mid] ==target:
                if nums[mid+1] != target:
                        return mid
                else:
                    left = mid+1
            if nums[mid]> target:
                left = mid+1
            if nums[mid]<target:
                right = mid-1
        return -1



s=Solution()

nums=[5, 7, 7, 8, 8, 8, 8, 8, 10]

target=8

result=s.first_and_last(nums, target)

print(f"For the target {target} in list {nums}: \n First occurrence is {get_first(nums, target)} \n last occurrence is {get_last(nums, target)}")

# class Solution:
# 	def searchRange(self, nums: List[int], target: int) -> List[int]:
# 		if len(nums) == 0:
# 			return [-1,-1]
# 		if len(nums) == 1:
# 			if nums[0] != target:
# 				return [-1,-1]
# 			else:
# 				return [0,0]

# 		left = self.findleft(nums,target)
# 		right = self.findright(nums,target)
# 		return [left,right]

# 	def findleft(self,nums,target):
# 		pl = 0
# 		pr = len(nums) - 1
# 		while pl <= pr:
# 			mid = pl + (pr-pl)//2
# 			if nums[mid] == target:
# 				if mid == 0:
# 					return mid
# 				else:
# 					if nums[mid-1] != target:
# 						return mid
# 					else:
# 						pr = mid - 1
# 			elif nums[mid] < target:
# 				pl = mid + 1
# 			else:
# 				pr = mid -1

# 		return -1

# 	def findright(self,nums,target):
# 		pl = 0
# 		pr = len(nums) - 1
# 		while pl <= pr:
# 			mid = pl + (pr-pl)//2
# 			if nums[mid] == target:
# 				if mid == len(nums) - 1:
# 					return mid
# 				else:
# 					if nums[mid + 1] != target:
# 						return mid
# 					else:
# 						pl = mid + 1
# 			elif nums[mid] < target:
# 				pl = mid + 1
# 			else:
# 				pr = mid -1

# 		return -1
