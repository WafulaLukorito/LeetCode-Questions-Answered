
"""
Given two binary strings a and b, return their sum as a binary string.
Time O(N) ... we do a loop over the maximum length of the 2 strings
 space 0(N)... Create Array that will hold our answer while we are looping
"""


def add_binary(a, b):
    result = []
    carry = 0
    i, j = len(a)-1, len(b)-1

    while (i >= 0 or j >= 0 or carry):
        total = carry

        if i >= 0:
            total += int(a[i])
            i -= 1

        if j >= 0:
            total += int(b[j])
            j -= 1

        carry = total // 2
        result.append(str(total % 2))

    return "".join(reversed(result))


a = "1010"
b = "1011"

result = add_binary(a, b)

print(result)
