

# *Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

#!Note that you must do this in-place without making a copy of the array.

nums = [0, 2, 3, 0, 7, 5, 0, 9, 0]


# - Issue:
# - nums.remove(num) modifies the list while iterating, which can lead to unexpected behavior.
# - The final step (nums = nums + ([0] * j)) creates a new list, violating the in-place requirement.
# - Verdict: ❌ Not truly in-place (modifies list structure and creates a new one)


# j = 0
# for num in nums:
#     if num == 0:
#         nums.remove(num)
#         j += 1

# nums = nums+([0]*j)
# print(nums)

# nums = [0, 2, 3, 0, 7, 5, 0, 9, 0]


# - Issue:
# - nums.remove(num) shifts elements, causing multiple passes over the list.
# - nums.append(0) moves zeros to the end but modifies list size dynamically.
# - Verdict: ❌ Not truly in-place (modifies list structure dynamically)

# Modifying while iterating (remove() inside loop) can cause skipped zeros.

# Inefficient because remove() is O(n) per call, making this O(n²) worst-case.


# def move_zeroes(nums):
#     for num in nums:
#         if num==0:
#             nums.remove(num)
#             nums.append(0)
#     return nums




# - Why This Works:
# - Uses a two-pointer technique to swap elements without modifying list structure.
# - Preserves relative order of non-zero elements.
# - Single pass (O(N)), making it efficient.
# - Verdict: ✅ Truly in-place modification (no extra space used)

def move_zeroes(nums):
    zero_p=0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[zero_p]= nums[zero_p], nums[i]
            zero_p +=1
    return nums


print(move_zeroes(nums))


people = [1, 3, 4, 1, 9, 45,  3, 222, 1, 1, 65]
pipsort = sorted(people)
print(people.count(1))
print(people.index(4))
people.sort()
print(people)
print(pipsort)
