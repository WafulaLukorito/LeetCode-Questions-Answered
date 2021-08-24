
# * Given an unsorted array of integers nums, return the length of the longest continuous increasing subsequence (i.e. subarray). The subsequence must be strictly increasing.

# *A continuous increasing subsequence is defined by two indices l and r (l < r) such that it is [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] and for each l <= i < r, nums[i] < nums[i + 1].
# *Sliding window:

# *Longest Increasing Subsequence
# def longest_increasing(nums):
#     if len(nums) == 1:
#         return 1

#     i, j = 0, 0
#     max_length = 0
#     while j < len(nums):
#         j += 1  # slide the window
#         max_length = max(max_length, (j-i))
#         # when condition is violated, reset the window
#         if j < len(nums) and nums[j-1] >= nums[j]:
#             i = j

#     return max_length


# nums = [1, 2, 3, 0, 2, 4, 5, 6, 7, 8, 9, 10, 3]

# result = longest_increasing(nums)

# print(f"The longest increasing subarray is {result} indices long")


# *Attempt 2

# def longest_increasing(nums):
#     if (not nums):
#         return 0

#     if (len(nums) == 1):
#         return 1

#     i = 0
#     j = 0

#     max_length = 0

#     for num in range(len(nums)):
#         j += 1
#         max_length = max(max_length, j - i)

#         if ( j < len(nums) and nums[j] <= nums[j-1]):
#             i = j
#     return max_length


# nums = [1, 2, 3, 0, 2, 4, 5, 6, 7, 8, 9, 10,  3]

# result = longest_increasing(nums)

# print(f"The longest increasing subarray is {result} indices long")

# def longest_increasing(nums):

#     if not nums:
#         return 0

#     if (len(nums) == 1):
#         return 1

#     i = 0
#     j = 0
#     max_size = 0

#     for num in nums:
#         j += 1
#         max_size = max(max_size, j-i)

#         if (j < len(nums) and nums[j] <= nums[j-1]):
#             i = j

#     return max_size


# nums = [954,955]
# #[1, 2, 3, 0, 2, 4, 5, 6, 7, 8, 9, 10,  3]

# result = longest_increasing(nums)

# print(f"The longest increasing subarray is {result} indices long")

# *Whiteboarding solution

def longest_increasing (nums):
    if not nums:
        return 0
    if (len(nums) == 1):
        return 1

    i = 0
    j = 0
    max_size = 0

    while (j < len(nums)):
        j+=1
        max_size = max (max_size, j-i)

        if (j < len(nums) and nums[j] < nums[j-1]):
            i = j

    return max_size





nums = [1, 2, 3, 0, 2, 4, 5, 6, 7, 8, 9, 10,  3]

result = longest_increasing(nums)

print(f"The longest increasing subarray is {result} indices long")

