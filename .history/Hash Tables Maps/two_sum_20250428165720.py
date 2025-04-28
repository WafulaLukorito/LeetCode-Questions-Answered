
"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

LeetCode: https://leetcode.com/problems/two-sum/
LeetCode Number: 1
Difficulty: Easy
Topic: Hash Tables, Maps
Company: Amazon, Apple, Facebook, Google, Microsoft, Uber, Yahoo

#? Time O(N): We do a loop over array of size n
#? Space O(N): We create a map to hold a value alongside the index
"""

def two_sum(nums, target):
    my_map = {}
    i = 0
    for num in nums:
        goal = target - num
        if goal in my_map:
            return (my_map[num], i)
        my_map[goal]=i
        i+=1


nums =  [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))














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

# print (f"The numbers that add up to {target} can be found in indices {result[0]} and {result[1]}.")


# * 2022 Solution


# def two_sum(nums, target):

#     nums_to_index = {}

#     for i in range (0, len(nums)):
#         goal = target - nums[i]
#         if goal in nums_to_index:
#             return nums_to_index[goal], i
#         nums_to_index[nums[i]] = i

# def two_sum(nums, target):
#     num_to_index = {}
#     for num in nums:
#         goal = target - num
#         if goal in num_to_index:
#             return num_to_index[goal], nums.index(num)
#         num_to_index[num] = nums.index(num)
#     return (None, None)


# def two_sum(nums, target):
#     # ? Create a dictionary to store the values and their indices
#     dict = {}
#     # ? Loop over the array
#     for i in range(len(nums)):
#         # ? Check if the difference between the target and the current value is in the dictionary
#         if target - nums[i] in dict:
#             # ? If it is, return the indices of the current value and the value in the dictionary
#             return (i, dict[target - nums[i]]
#         # ? If it isn't, add the current value to the dictionary
#         dict[nums[i]] = i


def two_sum(nums, TARGET):
    num_to_index = {}
    for i in range(len(nums)-1):
        goal = TARGET - nums[i]
        if goal in num_to_index:
            return (i, num_to_index[goal])
        num_to_index[nums[i]] = i
    return (None, None)


nums = [5, 6, 4, 7, 2, 9]
target = 11

result = two_sum(nums, target)

print(
    f"The numbers that add up to {target} can be found in indices {result[0]} and {result[1]}.")
