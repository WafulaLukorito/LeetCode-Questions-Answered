
"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
#? Time O(N): We do a loop over array of size n
#? Space O(N): We create a map to hold a value alongside the index
"""


# def two_sum(nums, target):
#     my_dict = {}
#     for num in nums:
#         goal = target- num
#         if goal in my_dict:
#             return (my_dict[goal], nums.index(num))
#         my_dict[num]= nums.index(num)

# #* Another solution:
# def two_sum(nums,target):
#         m = {}
#         n = len(nums)
#         for i in range(0,n):
#             goal = target - nums[i]
#             if(goal in m):
#                 return [m[goal], i]
#             m[nums[i]] = i

# #*Another way
# def twoSum(nums, target):
# 	num_to_index = {}
# 	for i, num in enumerate(nums):
# 		if target - num in num_to_index:
# 			return (i, num_to_index[target - num])
# 		num_to_index[num] = i


# *third attempt

# def two_sum(nums, target):
#     nums_to_index = {}
#     for i in range(0,len(nums)):
#         goal = target - nums[i]
#         if goal in nums_to_index:
#             return nums_to_index[goal], i
#         nums_to_index[nums[i]] = i

# *Whiteboard Solution

# def two_sum(nums, target):
#     nums_to_index = {}

#     for i in range(0, len(nums)):
#         goal = target - nums[i]
#         if goal in nums_to_index:
#             return nums_to_index[goal], i
#         nums_to_index[nums[i]]= i

# nums= [3,3]
# target = 6

# result = two_sum(nums, target)

#print (f"The numbers that add up to {target} can be found in indices {result[0]} and {result[1]}.")


# * 2022 Solution


# def two_sum(nums, target):

#     nums_to_index = {}

#     for i in range (0, len(nums)):
#         goal = target - nums[i]
#         if goal in nums_to_index:
#             return nums_to_index[goal], i
#         nums_to_index[nums[i]] = i

def two_sum(nums, target):
    nums_to_index = {}

    for i in range(0, len(nums)):
        goal = target - nums[i]
        if goal in nums_to_index:
            return nums_to_index[goal], i
        nums_to_index[nums[i]] = i


nums = [5, 6, 4, 7, 2, 9]
target = 6

result = two_sum(nums, target)

print(
    f"The numbers that add up to {target} can be found in indices {result[0]} and {result[1]}.")
