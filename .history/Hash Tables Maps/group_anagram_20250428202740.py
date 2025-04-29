"""
    Given an array of strings strs, group the anagrams together. You can return the answer in any order.

   An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once

   #Example 1:
    Input: strs = ["eat","tea","tan","ate","nat","bat"]
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
    #Example 2:
    Input: strs = [""]
    Output: [[""]]
    #Example 3:
    Input: strs = ["a"]
    Output: [["a"]]

   LeetCode 49. Group Anagrams
    https://leetcode.com/problems/group-anagrams/
    # Topics: Hash Table, String
    Complexity: Time: O(N*M*Log(M))--- N --> Length of input array
    Difficulty: Medium

    #? Time Complexity O(N*M*Log(M))---
    N --> Length of input array
    M --> Length of biggest string in array

    N--> Due to loop over input array
    M * Log(M)--> due to the fact that we sort each string when we pass over it in the loop.

    #? Space: O(N)-- use hashmap to store our data

    """
from collections import defaultdict

def groupAnagrams(strs):
    anagram_map = defaultdict(list)  # Automatically initializes new keys with []
    for s in strs:
        sorted_s = tuple(sorted(s))
        anagram_map[sorted_s].append(s)  # No need to check if key exists
    return list(anagram_map.values())


# *** Another Very simple solution ***

# def group_anagrams(strs):
#     m ={}
    
#     for word in strs:
#         s = "".join(sorted(word))
#         if s in m:
#             m[s].append(word)
#         else:
#             m[s]=[word]
    
#     return list(m.values())


# def group_anagrams(s):
#     ln = len(strs):
#         if ln <= 1:
#             return [strs]
#         d = {}
#         for i in strs:
#             s = "".join(sorted(i))
#             if s in d.keys():
#                 d[s].append(i)
#             else:
#                 d[s] = [i]

#         return d.values()

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

# def group_anagrams(strs):
#     if len(strs) <= 1:
#         return strs

#     m = {}
#     for str in strs:
#         hs = "".join(sorted(str))
#         if hs in m:
#             m[hs].append(str)
#         else:
#             m[hs] = [str]

#     return m.values()

def group_anagrams(strs):
    if len(strs) < 2:
        return strs

    m = {}
    for s in strs:
        s_hashed = "".join(sorted(s))
        if s_hashed not in m:
            m[s_hashed] = [s]
        else:
            m[s_hashed].append(s)
    return list(m.values())


strs = ["cat", "dog", "god", "act", "tac"]

result = group_anagrams(strs)

print(result)


# strs = ["cat", "dog", "god", "act", "tac", "man"]

# result = str(group_anagrams(strs))

# print(result)

# strs = ["cat", "dog", "god", "act", "tac", "man"]

# result = group_anagrams(strs)

# print(result)
