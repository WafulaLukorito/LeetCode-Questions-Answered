
""" Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 #? Can use three methods:
 1. sort array and check if nums[i] == nums [i-1]
 2. Create set and check if set is equal to array.
 #?3. Use map to track items --- Time O(N)--- single loop over input array. Space O(N)--- We create map to track
"""

# def contains_duplicates(nums):
#     nums_to_occurences = {}
#     for num in nums:
#         if num in nums_to_occurences:
#             return True
#         nums_to_occurences[num]=1
#     return False

#*Second attempt

def contains_duplicates(nums):
    nums_to_number = {}
    for num in nums:
        if nums in nums_to_number:
            return True
        nums_to_number[num]=1
    return False


#*Whiteboarding Attempt

def contains_duplicates(nums):
    nums_to_number = {}
    for num in nums:
        if num in nums_to_number:
            return True
        nums_to_number[num]=1
    return False


nums1 = [1,2,3,4,1]
nums2=[1,2,3,4,5,6]

result1 = contains_duplicates(nums1)
result2 = contains_duplicates(nums2)

print(f"It is {result1} that array {nums1} contains duplicates")
print(f"It is {result2} that array {nums2} contains duplicates")


