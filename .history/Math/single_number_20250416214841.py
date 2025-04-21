"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

2*(a+b+c) - (a+a+b+b+c) = c

(a+b+c) => summation of unique elements
(a+a+b+b+c) => current sum

#? Time complexity: O(2*N) = O(N): We pass over input array once, then pass separately oer the set

#? Space complexity: Constant, due to usage of a set.

"""

# def find_single(nums):
#     sum_set = sum(set(nums))
#     current_sum = sum(nums)

#     return (2*sum_set) - current_sum


# *Second attempt

# def find_single(nums):
#     set_sum = sum(set(nums))
#     current_sum = sum(nums)

#     return 2*set_sum - current_sum


# *Third attempt

# def find_single(nums):
#     sum_set= sum(set(nums))
#     current_sum = sum (nums)

#     return 2*sum_set - current_sum

# *Whiteboarding Attempt
def find_single(nums):
    my_set = set(nums)
    intended_sum = 2 * (sum(my_set))
    current_sum = sum(nums)
    single = intended_sum - current_sum
    return single


nums = [4, 1, 2, 1, 2]

result = find_single(nums)

print(f"The lonesome number in {nums} is {result}")
