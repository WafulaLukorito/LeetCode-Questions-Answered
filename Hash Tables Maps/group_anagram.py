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
#     def find_hash(self, s):
#         return ''.join(sorted(s))

#     def group_anagrams(self, strs: List[str]) -> List[List[str]]:
#         answers = []
#         m={}

#         for str in strs:
#             hashed_str= self.find_hash(str)
#             if (hashed_str not in m):
#                 m[hashed_str] = []
#             m[hashed_str].append(str)

#         for val in m.values():
#             answers.append(val)

#         return answers


# strs = ["eat","tea","tan","ate","nat","bat"]

# s = Solution()

# result = s.group_anagrams(strs)

# print (result)

# * Second Attempt

# from typing import List


# class Solution:

#     def find_hash(self, str):
#         return ''.join(sorted(str))

#     def group_anagrams(self, strs:List[str]) -> List[List[str]]:
#         answers = []
#         m = {}

#         for str in strs:
#             hashed_str=self.find_hash(str)
#             if (hashed_str not in m):
#                 m[hashed_str]=[]
#             m[hashed_str].append(str)

#         for val in m.values():
#             answers.append(val)

#         return answers

# s = Solution()


# *Third Attempt

# from typing import List


# class Solution:

#     def find_hash(self, s):
#         return ''.join(sorted(s))

#     def group_anagrams(self, strs:List[str]) -> List[List[str]]:
#         answers = []
#         m = {}

#         for s in strs:
#             hashed_s = self.find_hash(s)
#             if (hashed_s not in m):
#                 m[hashed_s] = []
#             m[hashed_s].append(s)

#         for val in m.values():
#             answers.append(val)

#         return answers


# s = Solution()

# strs = ["cat", "ant", "act", "tac", "tan", "sad"]

# results = s.group_anagrams(strs)
# print(results)


# *Whiteboarding Attempt

class Solution:

    def hashed_string(self, s):
        return "".join(sorted(s))

    def group_anagrams(self, strs: list[str]) -> list[list[str]]:
        answers = []
        m = {}

        for s in strs:
            hashed_s = self.hashed_string(s)
            if (hashed_s not in m):
                m[hashed_s] = []
            m[hashed_s].append(s)

        for val in m.values():
            answers.append(val)

        return answers


s = Solution()

strs = ["cat", "dog", "god", "act", "tac", "man"]

result = s.group_anagrams(strs)

print(result)


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