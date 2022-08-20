# Complete the 'matchingStrings' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY strings
#  2. STRING_ARRAY queries
#

# *My solution
def matchingStrings(strings, queries):
    # Write your code here
    arr = []
    for i in queries:
        arr.append(strings.count(i))
    return arr

# def matchingStrings(strings, queries):
#     # Write your code here
#     return [strings.count(i) for i in queries]
