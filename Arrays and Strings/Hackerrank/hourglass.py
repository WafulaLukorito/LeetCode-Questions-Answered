
# Hourglass
"""Given a 6x6 2D Array, arr:
    1 1 1 0 0 0
    0 1 0 0 0 0
    1 1 1 0 0 0
    0 0 0 0 0 0
    0 0 0 0 0 0
    0 0 0 0 0 0
    An hourglass in A is a subset of values with indices falling in this pattern in arr's graphical representation:
    a b c
      d
    e f g
    There are 16 hourglasses in arr, and an hourglass sum is the sum of an hourglass' values.
    Calculate the hourglass sum for every hourglass in arr, then print the maximum hourglass sum.
    """
# Complete the hourglassSum function below.


def hourglassSum(arr):
    max_sum = -float('inf')
    for i in range(4):  # row index
        for j in range(4):
            top = sum(arr[i][j:j+3])
            mid = arr[i+1][j+1]
            bottom = sum(arr[i+2][j:j+3])
            hourglass = top + mid + bottom
            if hourglass > max_sum:
                max_sum = hourglass
    return max_sum


arr = [[1, 1, 1, 0, 0, 0],
       [0, 1, 0, 0, 0, 0],
       [1, 1, 1, 0, 0, 0],
       [0, 0, 2, 4, 4, 0],
       [0, 0, 0, 2, 0, 0],
       [0, 0, 1, 2, 4, 0]]

print(hourglassSum(arr))  # 19

mylist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(mylist[1:6])  # [1, 2, 3, 4, 5]
