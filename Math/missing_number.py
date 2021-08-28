
"""Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?

#? Use Gauss Formula

#?Time Complexity O(n) as we loop over elements of array once

#? Space complexity O(1)
    """

# def missing_number(nums):
#     current_sum = sum(nums)
#     n = len(nums)
#     intended_sum = n * ((n+1)/2)
#     return int (intended_sum - current_sum)




# #*Attempt 2


# def missing_number(nums):
#     n = len(nums)
#     current_sum = sum(nums)
#     intended_sum= n * (n+1)/2
#     return intended_sum -current_sum


# def missing_number(nums):
#     n = len(nums)
#     current_sum=sum(nums)
#     intended_sum = n* (n+1)/2
#     return int(intended_sum - current_sum)



#*Whiteboarding Solution


def missing_number(nums):
    n = len(nums)
    current_sum = sum (nums)
    intended_sum = n * (n+1)/2
    return int(intended_sum - current_sum)



nums = [9,6,4,2,3,5,7,0,1] #8

result=  missing_number(nums)

print (f"The missing number in {nums} is {result}.")