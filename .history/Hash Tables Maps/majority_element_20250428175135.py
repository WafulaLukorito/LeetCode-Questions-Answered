
"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Leetcode: https://leetcode.com/problems/majority-element/
Difficulty: Easy


#? Time Complexity: O(2*N) = O(N)---One pass to assign value, separate pass again

#?Space: O(N)--- create a map to track occurrence

#! Use m.get!!!

"""

import operator
from itertools import accumulate, combinations, combinations_with_replacement, permutations
from collections import Counter
from collections import namedtuple


# You can efficiently find the majority element using the Boyer-Moore Voting Algorithm, which runs in O(n) time and O(1) space. Here's the implementation

def majority_element(nums):
    candidate, count = None, 0
    for num in nums:
        if count = 0:
            candidate = num
        else:
            count += (1 if num==candidate else -1)
    return candidate




# def majority_element(nums):
#     n = len(nums)
#     m = {}
#     for num in nums:
#         if num in m:
#             m[num] += 1
#         else:
#             m[num]=1
        
#         if m[num] > n//2:
#                 return num
#     return -1













# def majority_element2(nums):
#     num_to_freq = {}
#     numslen = len(nums)
#     for num in nums:
#         if num not in num_to_freq:
#             num_to_freq[num] = 1
#         else:
#             num_to_freq[num] += 1
#             if num_to_freq[num] > numslen/2:
#                 return num


# nums = [2, 2, 1, 1, 1, 2, 2]
# result = majority_element2(nums)
# print(f"2. The majority element in array {nums} is {result} ")


# def majority_element(nums):
#     m = {}
#     for num in nums:
#         m[num] = m.get(num, 0)+1

#     for num in nums:
#         if(m[num] > len(nums)//2):
#             return num

# *Second Attempt

# def majority_element(nums):
#     m = {}
#     for num in nums:
#         m[num]=m.get(num,0)+1

#     for num in nums:
#         if m[num] > len(nums)//2:
#             return num


# *Third Attempt:

# def majority_element(nums):
#     m={}

#     for num in nums:
#         m[num]=m.get(num,0)+1
#     for num in nums:
#         if m[num] > len(nums)//2:
#             return num

# *Whiteboarding attempt
# from collections import Counter


# def majority_element(nums):
#     m=Counter(nums)
#     print (m)
#     # for num in nums:
#     #     m[num]=m.get(num, 0)+1
#     for num in nums:
#         if m[num] > len(nums)//2:
#             return num


def majority_element(nums):
    my_counter = Counter(nums)
    for key, value in my_counter.items():
        if value > len(nums)//2:
            return key


nums = [2, 2, 1, 1, 1, 2, 2]
result = majority_element(nums)
print(f"The majority element in array {nums} is {result} ")


def majority_eleme(nums):
    m = {}
    for num in nums:
        if num not in m:
            m[num] = 1
        else:
            m[num] = m.get(num, 0)+1
    for num in nums:
        if m[num] > len(nums)//2:
            return num


nums = [2, 2, 1, 1, 1, 2, 2]
result = majority_eleme(nums)
print(f"The majority element in array {nums} is {result} ")


def major_ele(arr):
    myCounter = Counter(arr)
    return myCounter.most_common(1)[0][0]


nums = [2, 2, 1, 1, 1, 2, 2]
result = major_ele(nums)
print(f"The majority element in array {nums} is {result} ")


my_tuple = namedtuple('my_tuple', 'name age')
my_tuple.name = 'John'
my_tuple.age = 30
print(my_tuple.age)  # prints 30

my_tuple2 = ('John', 30, 'Nairobi', 'Kenya', 'inazidi', 'kuenda',
             'mbele', 'pamoja', 'tushirikiane', 'tupendane', 'bendera')
#! print(my_tuple2.find('Kenya'))  #Does not work!! Tuple has no attribute find!
print(my_tuple2.index('Kenya'))  # prints 3

myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
myList.reverse()
print(myList)  # prints [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
rotated_list = myList[3:] + myList[:3]
print(rotated_list)  # prints [4, 3, 2, 1, 10, 9, 8, 7, 6, 5]

a1 = [1, 2, 3]
perm = permutations(a1)
print(list(perm))
perm2 = permutations(a1, 2)
print(list(perm2))

a2 = [1, 2, 3, 4]
comb = combinations(a2, 3)
print(list(comb))

comb2 = combinations_with_replacement(a2, 2)
print(list(comb2))

a3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a3acc = accumulate(a3)
print(list(a3acc))

a3_multipy_cummulatively = list(accumulate(a3, operator.mul))
print(a3_multipy_cummulatively)

a3_divide_cummulatively = list(accumulate(a3, operator.truediv))
print(a3_divide_cummulatively)
print()

a31 = [3, 5, 7, 9, 3, 2, 45, 31, 1]
# Returns the maximum of the current and previous elements
a31acc = accumulate(a31, max)
print(list(a31acc))
