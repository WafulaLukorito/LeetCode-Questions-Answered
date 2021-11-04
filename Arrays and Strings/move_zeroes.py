

#*Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

#!Note that you must do this in-place without making a copy of the array.


#*------ 2 MONTHS LATER------ 



nums = [1, 0,2,3,0,7,5,0,9,0,7,0,0, 9]

# j = 0
# n = len(nums)

# for num in nums:
#     if (num != 0):
#         nums[j] = num
#         j+=1

# for i in range(j, n):
#     nums[i] = 0




#* Second Attempt

# j = 0
# for num in nums:
#     if num != 0:
#         nums[j] = num
#         j+=1

# for i in range (j, len(nums)):
#     nums[i] = 0



# print (nums)


#*-------Whiteboarding---------------------------

j = 0

for num in nums:
    if num !=0:
        nums[j] = num
        j+=1

for i in range (j, len(nums)):
    nums[i] = 0



print (nums)

# nums = [0,2,3,0,7,5,0,9,0]

# j=0

# n = len(nums)
# for num in nums:
#     if (num != 0):
#         nums[j] = num
#         j+=1


# for i in range (j, n):
#     nums[i] = 0

# print (nums)


#*Attempt 2

# nums = [0,2,3,0,7,5,0,9,0]

# n = len (nums)

# j= 0

# for num in nums:
#     if (num !=0):
#         nums[j] = num
#         j+=1

# for i in range (j, n):
#     nums[i] = 0

# print (nums)

#*Whiteboarding attempt 

# nums = [0,2,3,0,7,5,0,9,0]

# n = len (nums)

# j = 0

# for num in nums:
#     if (num!=0):
#         nums[j]= num
#         j+=1

# for i in range (j, n):
#     nums[i] = 0

# print (nums)

#*Attempt after a week

# nums = [1, 0,2,3,0,7,5,0,9,0,7,0,0, 9]


# # j = 0
# # k = 0 

# # for num in nums:
# #     if num == 0:
# #         j+=1
# #     else:
# #         nums[k] = num
# #         k+=1
# # for i in range (len(nums) - j, len(nums)):
# #     nums[i] = 0

# print (nums)