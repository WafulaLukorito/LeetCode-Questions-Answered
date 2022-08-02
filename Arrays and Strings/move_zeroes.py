

# *Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

#!Note that you must do this in-place without making a copy of the array.

nums = [0, 2, 3, 0, 7, 5, 0, 9, 0]


# j = 0
# for num in nums:
#     if num == 0:
#         nums.remove(num)
#         j += 1

# nums = nums+([0]*j)
# print(nums)

# nums = [0, 2, 3, 0, 7, 5, 0, 9, 0]


def move_zeroes(nums):
    for num in nums:
        if num == 0:
            nums.remove(num)
            nums.append(0)
    return (nums)


print(move_zeroes(nums))
