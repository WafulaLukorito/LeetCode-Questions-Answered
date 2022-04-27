"""
Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, return the number of tuples (i, j, k, l) such that:

0 <= i, j, k, l < n
nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0

#? Time Complexity: O(N^2)--- N is the maximum size of the 4 input arrays. We do a nested loop twice.

#?Space Complexity: O(N)-- Due to usage of maps

"""
def four_sum_ii (nums1, nums2, nums3, nums4):
    m = {}
    answer = 0

    len1, len2, len3, len4 = len(nums1), len(nums2), len(nums3), len(nums4)

    for i in range(0, len1):
        x = nums1[i]
        for j in range (0, len2):
            y = nums2[j]
            if (x+y) in m:
                m[x+y] += 1
            m[x+y] = 1

    for i in range (0, len3):
        x = nums3[i]
        for j in range(0, len4):
            y = nums4[j]
            target = -(x+y)
            if target in m:
                answer += m[target]
    return answer

















# def four_sum_ii(nums1, nums2, nums3, nums4):
#     m = {}
#     result = 0

#     len1= len(nums1)
#     len2 = len(nums2)
#     len3 = len(nums3)
#     len4 = len(nums4)

#     for i in range(0, len1):
#         x = nums1[i]
#         for j in range(0, len2):
#             y = nums2[j]

#             if ((x+y) not in m):
#                 m[x+y] = 0
#             m[x+y]+=1

#     for i in range(0, len3):
#         x=nums3[i]
#         for j in range(0,len4):
#             y= nums4[j]
#             goal = -(x+y)
#             if goal in m:
#                 result += m[goal]
#     return result


# *************************SECOND ATTEMPT***************************************

# def four_sum_ii(nums1, nums2, nums3, nums4):
#     answer = 0
#     m = {}

#     for i in range (0, len(nums1)):
#         x = nums1[i]
#         for j in range (0, len(nums2)):
#             y = nums2[j]

#             if (x+y) not in m:
#                 m[x+y]=0
#             m[x+y] +=1

#     for i in range (0, len(nums3)):
#         x = nums3[i]
#         for j in range (0, len(nums4)):
#             y= nums4[j]
#             goal = -(x+y)
#             if goal in m:
#                 answer += m[goal]

#     return answer


# ******Third Attempt**********

# def four_sum_ii(nums1, nums2, nums3, nums4):
#     answer = 0
#     m = {}

#     for i in range(0, len(nums1)):
#         x = nums1[i]
#         for j in range(0, len(nums2)):
#             y = nums2[j]

#             if (x+y) not in m:
#                 m[x+y] = 0
#             m[x+y] += 1

#     for i in range(0, len(nums3)):
#         x= nums3[i]
#         for j in range(0, len(nums4)):
#             y = nums4[j]
#             goal = -(x+y)
#             if goal in m:
#                 answer += m[goal]
#     return answer


#*Whiteboarding Solution****
# def four_sum_ii(nums1, nums2, nums3, nums4):
#     answer = 0
#     m = {}

#     for i in range(0, len(nums1)):
#         x= nums1[i]
#         for j in range (0, len (nums2)):
#             y = nums2[j]

#             if (x+y) not in m:
#                 m[x+y] = 0
#             m[x+y]+=1

#     for i in range (0, len(nums3)):
#         x= nums3[i]
#         for j in range (0, len(nums4)):
#             y = nums4[j]

#             goal = -(x+y)
#             if goal in m:
#                 answer +=m[goal]

#     return answer




nums1 = [1, 2]
nums2 = [-2, -1]
nums3 = [-1, 2]
nums4 = [0, 2]

result = four_sum_ii(nums1, nums2, nums3, nums4)

print(result)
