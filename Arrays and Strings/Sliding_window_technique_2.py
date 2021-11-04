
# *Given an array of integers of size N, find maximum sum of K consecutive elements.

# def max_sum (arr, window_size):
#     array_size = len (arr)
#     if (array_size <= window_size):
#         print("Invalid problem!")
#         return -1

#     window_sum = sum([arr[i] for i in range (window_size)])
#     max_sum = window_sum

#     for i in range(array_size - window_size):
#         window_sum = window_sum - arr[i] + arr[i+window_size]
#         max_sum = max(window_sum, max_sum)

#     return max_sum


# arr = [20, 50, 70, 390, -410, 5, 6, 8, 345, 432, -54]

# k = 3

# answer = max_sum(arr, k)
# print (answer)


# *Attempt 2

# def max_sum(arr, window_size):
#     array_size = len(arr)
#     if (array_size < window_size):
#         print("Invalid operation!")
#         return -1

#     else:
#         current_sum = sum([arr[i] for i in range(window_size)])
#         max_sum = current_sum

#         for i in range(array_size - window_size):
#             current_sum = current_sum - arr[i] + arr[i + window_size]
#             max_sum = max(max_sum, current_sum)
#         return max_sum


# arr = [-7, 9, -8, 6, 1, -12, 13, -20, 7, 10, 12, -13, 15, -19, -14, -15, -4, -3, 16, -19]


# k = 2

# result = max_sum(arr, k)
# print(result)

# *Attempt 3

# def max_sum (arr, window_size):
#     array_size = len(arr)

#     if (array_size < window_size):
#         print ("Invalid operation!")
#         return -1
#     else:
#         current_sum = sum([arr[i] for i in range (window_size)])
#         max_sum = current_sum

#         for i in range (array_size - window_size):
#             current_sum = current_sum - arr[i] + arr[i + window_size]

#             max_sum = max (max_sum, current_sum)

#         return max_sum


# arr = [-7, 9, -8, 6, 1, -12, 13, -20, 7, 10, -13, -13, 15, -19, -14, -15, -4, -3, 16, -19] #?prints 22

# k = 2

# result = max_sum(arr, k)
# print (result)

# * Whieboarding Answer

# def max_sum(arr, window_size):
#     array_size = len (arr)
#     if (array_size < window_size):
#         print ("Invalid operation, check your input!")
#         return None
#     else:
#         current_sum = sum([arr[i] for i in range(window_size)])
#         max_sum = current_sum

#         for i in range (array_size - window_size):
#             current_sum = current_sum - arr[i] + arr[i+window_size]
#             max_sum = max (max_sum, current_sum)

#         return max_sum


# *---------- 2 MONTHS LATER----------

# def max_sum(arr, k):

#     current_sum = sum([arr[i] for i in range(k)])

#     max_sum = current_sum
#     i = 0

#     while (i < len(arr)-k):
#         current_sum = current_sum - arr[i] + arr[i+k]
#         max_sum = max(max_sum, current_sum)
#         i += 1
#     return (max_sum)


#*Attempt 2

# def max_sum(arr, k):
#     if (k> len(arr)):
#         print ("Invalid Operation! Window cannot be bigger than array")
#     else:
#         curr_sum = sum([arr[i] for i in range (k)])
#         max_sum =curr_sum

#         for i in range(len(arr)-k):
#             curr_sum = curr_sum - arr[i] + arr[i+k]
#             max_sum = max(max_sum, curr_sum)
#         return max_sum

#*----------WHITEBOARD ATTEMPT----------
#*----------WHITEBOARD ATTEMPT----------

def max_sum (arr, k):
    array_size = len(arr)
    if k > array_size:
        print ("Invalid input! Window size cannot be larger than array")
    else:
        current_sum = sum([arr[i]for i in range (k)])
        max_sum = current_sum

        for i in range(array_size - k):
            current_sum = current_sum - arr[i] + arr[i+k]
            max_sum = max(current_sum, max_sum)
        return max_sum

arr = [20, 50, 70, 390, -410, 5, 6, 8, 345, 432, -54]

k = 3

result = max_sum(arr, k)

if result != None:
    print(result)
