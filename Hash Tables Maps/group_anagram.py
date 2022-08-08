"""
    Given an array of strings strs, group the anagrams together. You can return the answer in any order.

   An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once

    #? Time Complexity O(N*M*Log(M))---
    N --> Length of input array
    M --> Length of biggest string in array

    N--> Due to loop over input array
    M * Log(M)--> due to the fact that we sort each string when we pass over it in the loop.

    #? Space: O(N)-- use hashmap to store our data

    """
# from typing import List
# class Solution:

#     def findHash(self, str):
#         return "".join(sorted(str))  #* sort a string


#     def group_anagrams(self, strs):
#         answers = []
#         m = {}

#         for s in strs:
#             hashed = self.findHash(s)
#             if hashed not in m:
#                 m[hashed] = []
#             m[hashed].append(s)

#         for p in m.values():
#             answers.append(p)

#         return answers


# *** Another Very simple solution ***

# def group_anagrams(s):
#     ln  = len(strs)
#     if ln <=1:
#         return [strs]
#     d = {}
#     for i  in strs:
#         s = ''.join (sorted (i))
#         if s in d.keys():
#             d[s].append(i)
#         else:
#             d[s] = [i]

#     return d.values()

# strs = ["cat", "dog", "god", "act", "tac", "man"]

# result = group_anagrams(strs)

# print(result)


# def group_anagrams(strs):
#     if len(strs) <= 1:
#         return [strs]
#     hs_to_str = {}

#     for str in strs:
#         hs = "".join(sorted(str))
#         if hs in hs_to_str:
#             hs_to_str[hs].append(str)
#         else:
#             hs_to_str[hs] = [str]

#     grouped = (hs_to_str.values())
#     res = []
#     for item in grouped:
#         res.append(item)
#     return res

def group_anagrams(strs):
    if len(strs) <= 1:
        return strs

    m = {}
    for str in strs:
        hs = "".join(sorted(str))
        if hs in m:
            m[hs].append(str)
        else:
            m[hs] = [str]

    return m.values()


strs = ["cat", "dog", "god", "act", "tac", "man"]

result = group_anagrams(strs)

print(result)
