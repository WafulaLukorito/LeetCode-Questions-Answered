
"""
Given a string s, find the length of the longest substring without repeating characters.

#? Sliding window technique 

"""

# def longest_substring(myString):
#     """
#     Given a string, find the longest substring without repeating characters.
#     """
#     if len(myString) == 1:
#         return 1
#     left = 0
#     right = 0
#     max_length = 0
#     while right < len(myString):
#         if myString[right] not in myString[left:right]:
#             right += 1
#             max_length = max(max_length, right - left)
#         else:
#             left += 1
#     return max_length


def longest_substring(string):
    """
    Given a string, find the longest substring without repeating characters.
    """
    if len(string) == 1:
        return 1
    left, right = 0, 0
    max_len = 0
    while right < len(string):
        if string[right] not in string[left:right]:
            right += 1
            max_len = max(max_len, right-left)
        else:
            left += 1
    return max_len


print(longest_substring("abcabcbb"))  # 3


string = "abcdabdfghijkla"

result = longest_substring(string)

print(
    f"In the string {string}, the longest substring without repeating characters is \n {result} \n")

string2 = "pwwkew"

result2 = longest_substring(string2)

print(
    f"In the string {string2}, the longest substring without repeating characters is \n {result2}")

string3 = "bbbbb"

result3 = longest_substring(string3)

print(
    f"In the string {string3}, the longest substring without repeating characters is \n {result3}")
