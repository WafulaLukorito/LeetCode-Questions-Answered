
# Complete the 'rotateLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#

def rotateLeft(d, arr):
    # Write your code here
    return arr[d:] + arr[:d]


arr = [1, 2, 3, 4, 5]
d = 4
print(rotateLeft(d, arr))
