
"""
Given two binary strings a and b, return their sum as a binary string.
Time O(N), space 0(1)
"""


# def add_binary(a, b):
#     result = []
#     carry = 0
#     i , j= len(a)-1, len(b) - 1

#     while i >= 0 or j >= 0 or carry:
#         total = carry

#         if i >= 0:
#             total += int(a[i])
#             i -= 1
#         if j >= 0:
#             total += int(b[j])
#             j -= 1

#         result.append(str(total % 2))
#         carry = total // 2

#     return "".join(reversed(result))



#*Second Attempt

# def add_binary(a, b):
#     result = []
#     carry = 0

#     i = len(a)-1
#     j = len(b)-1

#     while (i >= 0 or j >= 0 or carry):
#         total = carry

#         if i >= 0:
#             total += int(a[i])
#             i -= 1
#         if j >= 0:
#             total += int(b[j])
#             j-=1

#         result.append(str(total%2))
#         carry = total // 2
#     return "".join(reversed(result))



#*Third attempt 

# def add_binary(a, b):
#     result = []
#     carry = 0
#     i = len(a) -1
#     j = len(b) - 1

#     while (i>= 0 or j >= 0 or carry):
#         total = carry

#         if i >= 0:
#             total += int(a[i])
#             i -= 1
#         if j >= 0:
#             total += int(b[j])
#             j -= 1
        
#         result.append(str(total%2))
#         carry = total//2
#     return "".join(reversed(result))


#*Whiteboarding solution
def add_binary(a, b):
    result = []
    carry = 0
    i = len(a) -1
    j = len (b)-1

    while (i>= 0 or j>=0 or carry):
        total = carry

        if i >= 0:
            total+=int(a[j])
            i-=1
        
        if j >= 0:
            total += int(b[j])
            j-=1

        result.append(str(total%2))
        carry = total//2
    return "".join((reversed(result)))



a = "1010"
b = "1011"

result = add_binary(a, b)

print(result)
