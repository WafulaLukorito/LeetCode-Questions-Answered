"""
Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, return the number of tuples (i, j, k, l) such that:

0 <= i, j, k, l < n
nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0

Leetcode: https://leetcode.com/problems/4sum-ii/
Leetcode Number: 454
Difficulty: Medium
Category: Hash Tables Maps
"""

# ? Time Complexity: O(N^2)--- N is the maximum size of the 4 input arrays. We do a nested loop twice.

# ?Space: O(n²) (worst-case storage for sum12_freq).

# ? Approach: We can use a map to store the sum of the first two arrays. Then we can iterate through the last two arrays and check if the sum of the last two arrays is equal to the negative of the sum of the first two arrays. If it is, we can increment the answer by the number of times the sum of the first two arrays occurs.

from collections import defaultdict

def four_sum_ii(nums1, nums2, nums3, nums4):
    sum12_freq = defaultdict(int)
    count = 0
    
    #Sum of first two
    for num1 in nums1:
        for num2 in nums1:
            sum12= num1+num2
            sum12_freq[sum12] += 1
            
    #Sum of next two
    for num3 in nums3:
        for num4 in nums4:
            goal = -(num3+num4)
            count += sum12_freq.get(goal, 0)
    
    return count















# def four_sum_ii(nums1, nums2, nums3, nums4):
#     m = {}
#     answer = 0

#     len1, len2, len3, len4 = len(nums1), len(nums2), len(nums3), len(nums4)

#     for i in range(0, len1):
#         x = nums1[i]
#         for j in range(0, len2):
#             y = nums2[j]
#             if (x+y) in m:
#                 m[x+y] += 1

#     for i in range(0, len3):
#         x = nums3[i]
#         for j in range(0, len4):
#             y = nums4[j]
#             target = -(x+y)
#             if target in m:
#                 answer += m[target]
#     return answer

# def four_sum_ii (nums1, nums2, nums3, nums4):
#     m = {}
#     answer = 0

#     len1, len2, len3, len4 = len(nums1), len(nums2), len(nums3), len(nums4)

#     for i in range(0, len1):
#         x = nums1[i]
#         for j in range (0, len2):
#             y = nums2[j]
#             if (x+y) in m:
#                 m[x+y] += 1
#             m[x+y] = 1

#     for i in range (0, len3):
#         x = nums3[i]
#         for j in range(0, len4):
#             y = nums4[j]
#             target = -(x+y)
#             if target in m:
#                 answer += m[target]
#     return answer


# def four_sum_ii(nums1, nums2, nums3, nums4):
#     sum_map = {}
#     count = 0
#     len1, len2, len3, len4 = len(nums1), len(nums2), len(nums3), len(nums4)
#     for i in range(len(nums1)):
#         for j in range(len1):
#             sum = nums1[i]+nums2[j]
#             if sum not in sum_map:
#                 sum_map[sum] = 1
#             else:
#                 sum_map[sum] += 1
#     for i in range(len(nums3)):
#         for j in range(len(nums4)):
#             goal = -(nums3[i]+nums4[j])
#             if goal in sum_map:
#                 count += sum_map[goal]
#     return count

# def four_sum_ii(nums1, nums2, nums3, nums4):
#     sum_map = {}
#     res = 0
#     len1, len2, len3, len4 = len(nums1), len(
#         nums2), len(nums3), len(nums4)

#     for i in range(len1):
#         x = nums1[i]
#         for j in range(len2):
#             y = nums2[j]
#             my_sum = x+y
#             if my_sum in sum_map:
#                 sum_map[my_sum] += 1
#             sum_map[my_sum] = 1

#     for i in range(len3):
#         x = nums3[i]
#         for j in range(len4):
#             y = nums4[j]
#             goal = - (x+y)
#             if goal in sum_map:
#                 res += sum_map[goal]
#     return res


nums1 = [1, 2]
nums2 = [-2, -1]
nums3 = [-1, 2]
nums4 = [0, 2]

result = four_sum_ii(nums1, nums2, nums3, nums4)

print(result)
