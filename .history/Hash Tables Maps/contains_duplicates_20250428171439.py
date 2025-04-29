
""" Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Leetcode 217. Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/
# Topics: Array, Hash Table
# Complexity: Time: O(N)--- N --> Length of input array
# Difficulty: Easy

 #? Can use three methods:
 1. sort array and check if nums[i] == nums [i-1]
 2. Create set and check if set is equal to array.
 #?3. Use map to track items --- Time O(N)--- single loop over input array. Space O(N)--- We create map to track
 #4. Use Counter
"""
def contains_duplicates(nums):
    my_map ={}
    for num in nums:
        if num in my_map:
            return True
        my_map[num]=1
    return False


nums1 = [1, 2, 3, 4, 1]
nums2 = [1, 2, 3, 4, 5, 6]

result1 = contains_duplicates(nums1)
result2 = contains_duplicates(nums2)

print(f"It is {result1} that array {nums1} contains duplicates")
print(f"It is {result2} that array {nums2} contains duplicates")











# def contains_duplicates(nums):
#     nums_to_occurences = {}
#     for num in nums:
#         if num in nums_to_occurences:
#             return True
#         nums_to_occurences[num]=1
#     return False

# *Second attempt

from collections import Counter


from collections import Counter

def contains_duplicates(nums):
    return any(count > 1 for count in Counter(nums).values())


nums1 = [1, 2, 3, 4, 1]
nums2 = [1, 2, 3, 4, 5, 6]

result1 = contains_duplicates(nums1)
result2 = contains_duplicates(nums2)

print(f"It is {result1} that array {nums1} contains duplicates")
print(f"It is {result2} that array {nums2} contains duplicates")


def contains_dups(nums):
    m = {}
    for num in nums:
        if num in m:
            return True
        m[num] = 1
    return False


nums1 = [1, 2, 3, 4, 1]
nums2 = [1, 2, 3, 4, 5, 6]

result1 = contains_dups(nums1)
result2 = contains_dups(nums2)

print(f"It is {result1} that array {nums1} contains duplicates")
print(f"It is {result2} that array {nums2} contains duplicates")
