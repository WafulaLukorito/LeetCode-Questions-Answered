
# *Given an array of integers of size N, find maximum sum of K consecutive elements.

# def max_sum(arr, window_size):
#     array_size = len(arr)
#     if (array_size <= window_size):
#         print("Invalid problem!")
#         return -1

#     window_sum = sum([arr[i] for i in range(window_size)])
#     max_sum = window_sum

#     for i in range(array_size - window_size):
#         window_sum = window_sum - arr[i] + arr[i+window_size]
#         max_sum = max(window_sum, max_sum)

#     return max_sum

# def max_sum(arr, k):
#     max_sum = 0
#     for i in range(len(arr) - k + 1):
#         max_sum = max(max_sum, sum(arr[i:i+k]))
#     return max_sum

def max_sum(arr, k):
    N = len(arr)
    window_size = k

    window_sum = sum(arr[:window_size])
    max_sum = window_sum

    for i in range(N-window_size):
        window_sum = window_sum - arr[i] + arr[i+window_size]
        max_sum = max(window_sum, max_sum)

    return (max_sum)


arr = [20, 50, 70, 390, -410, 5, 6, 8, 345, 432, -54]

k = 3

answer = max_sum(arr, k)
print(answer)
