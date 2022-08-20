
import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#


def dynamicArray(n, queries):
    # Write your code here
    seqList = [[] for _ in range(n)]
    lastAnswer = 0
    result = []
    for query in queries:
        if query[0] == 1:
            seqList[(query[1] ^ lastAnswer) % n].append(query[2])
        elif query[0] == 2:
            index = (query[1] ^ lastAnswer) % n
            lastAnswer = seqList[index][query[2] % len(seqList[index])]
            result.append(lastAnswer)
    return result
