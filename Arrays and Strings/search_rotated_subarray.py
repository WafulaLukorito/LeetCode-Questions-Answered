
def search (nums, target):
    #* FIND ROTATION POINT
    if len(nums) == 1:
        mid = 0
    left, right = 0, len(nums)-1

    while left <= right:
        mid = (left+right)//2
        mid_next= (mid+1) % len(nums)
        mid_prev = (mid -1) % len(nums)

        if (nums[mid]<nums[mid-1] and nums[mid]<nums[mid+1]):
            mid = mid
        elif (nums[mid]> nums[right]):
            left = mid +1
        else:
            right = mid -1

    #* Split Array into two 
    if mid == 0:
        return -1
    if (target < nums[mid] ) or (target > nums[mid_prev]):
        return -1
    else:
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            left2 = 0
            right2 = mid -1
            while left2 <= right2:
                mid2= (left2+ right2)//2
                if target == nums[mid2]:
                    return mid2
                elif target > nums[mid2]:
                    left2 = mid2+1
                else:
                    right = mid2 -1
        else:
            left3= mid + 1
            right3 = len(nums)-1
            while left3 <= right3:
                mid3 = (left3 +right3) //2
                if target == nums[mid3]:
                    return mid3
                elif target > nums [mid3]:
                    left3 = mid3+1
                else:
                    right = mid3-1
    return -1

nums = [4,5,6,7,0,1,2]
target = 0

answer = search(nums, target)

print(answer)



