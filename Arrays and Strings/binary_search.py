
#*Attempt 1

# def binary_search(arr, target):
#     left = 0
#     right = len(arr) - 1
#     while (left <= right):
#         mid = (left+right)//2 

#         if (target == arr[mid]):
#             return mid
#         elif (target < arr[mid]):
#             right = mid - 1
#         else:
#             left = mid +1

#     return -1




# arr = [ 1, 2, 3, 6]
# target = 7

# result = binary_search(arr, target)

# if result != -1:
#     print ("Value found at index %d" % result)
# else:
#     print ("Sorry, value not found in array")






# #*Attempt 2

# def binary_search(arr, target):
#     left = 0
#     right = len(arr)-1

#     while (left <= right):
#         mid = (left + right)//2
#         if (arr[mid] == target):
#             return mid
#         elif (target < arr[mid]):
#             right = mid -1
#         else:
#             left = mid + 1
#     return -1




# arr = [1,2,3,4,5,6,7,8,9]
# target = 5

# value = binary_search(arr, target)

# if value != -1:
#     print (f"Value {target} was found at index {value}")
# else:
#     print (f"Sorry, the value {target} was not found in this dataset")

#* Attempt 3

# def binary_search(arr, target):
#     left = 0
#     right = len(arr) -1
#     while left <= right:
#         mid = (left + right)//2
#         if (target == arr[mid]):
#             return mid
#         elif (target < arr[mid]):
#             right = mid -1
#         else:
#             left = mid +1
#     return -1

# arr = [1,3,4,6,8,34,23,5,6,9]
# sorted_arr = sorted(arr)

# target = int(input("Enter value you desire to find: \n"))

# value = binary_search(sorted_arr, target)


# if (value != -1):
#     print (f"Value {target} found at sorted array's index {value}")
# else:
#     while value == -1:
#         print(f"Value {target} not found in dataset. Please try another value. \n")
#         target = int(input("Enter another value you desire to find: \n"))
#         value = binary_search(sorted_arr, target) 


#*Whiteboard implementation

#? Time Complexity O(log n)

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while (left <= right):
        mid = (left+right)//2
        if (target == arr[mid]):
            return mid
        elif (target < mid):
            right = mid - 1
        else:
            left = mid + 1
    return -1



arr = [1,2,3,4,5,6]

target = 8

value = binary_search(arr, target)

if (value != -1):
    print(f"Your value {target} has been located at index {value}.")
else:
    print (f"Your value {target} cannot be located in this dataset, we're very sorry.")