"""Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]


#? Time Complexity = O(N)--- O(N)+O(N)---two loops over array

#? Space Complexity = O(1) ---- did not use additional memory space

    """

# * ----2 months later ----*

# def is_valid_mountain(arr):

#     if len(arr) < 3:
#         return False
#     i = 1
#     while ((i < len(arr)) and (arr[i] > arr [i-1] )):
#         i+=1

#     if (i==1 or i == len(arr)):
#         return False

#     while ((i < len(arr)) and (arr[i] < arr[i-1])):
#         i+=1

#     return i == len(arr)


def is_valid_mountain(arr):

    if len(arr) < 3:
        return False

    i = 1
    while (i < len(arr) and arr[i] > arr[i-1]):
        i += 1

    if (i == 1 or i == len(arr)):
        return False

    while (i < len(arr) and arr[i] < arr[i-1]):
        i += 1

    return i == len(arr)


arr = [0, 3, 2, 1]

arr_2 = [9, 8, 6, 7]

result = is_valid_mountain(arr)
result_2 = is_valid_mountain(arr_2)

print(f"it is {result} that {arr} is a Valid Mountain Array")
print(f"it is {result_2} that {arr_2} is a Valid Mountain Array")
