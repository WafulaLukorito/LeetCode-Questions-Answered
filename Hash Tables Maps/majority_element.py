
"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

#? Time Complexity: O(2*N) = O(N)---One pass to assign value, separate pass again

#?Space: O(N)--- create a map to track occurrence 

#! Use m.get!!!

"""


# def majority_element(nums):
#     m = {}
#     for num in nums:
#         m[num] = m.get(num, 0)+1

#     for num in nums:
#         if(m[num] > len(nums)//2):
#             return num

#*Second Attempt

# def majority_element(nums):
#     m = {}
#     for num in nums:
#         m[num]=m.get(num,0)+1
    
#     for num in nums:
#         if m[num] > len(nums)//2:
#             return num


#*Third Attempt:

# def majority_element(nums):
#     m={}

#     for num in nums:
#         m[num]=m.get(num,0)+1
#     for num in nums:
#         if m[num] > len(nums)//2:
#             return num

#*Whiteboarding attempt
from collections import Counter


def majority_element(nums):
    m=Counter(nums)
    print (m)
    # for num in nums:
    #     m[num]=m.get(num, 0)+1
    for num in nums:
        if m[num] > len(nums)//2:
            return num


nums = [2, 2, 1, 1, 1, 2, 2]
result = majority_element(nums)
print(f"The majority element in array {nums} is {result} ")
