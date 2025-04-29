
'''
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
#?The functions get and put must each run in O(1) average time complexity.

LeetCode 146. LRU Cache
LeetCode URL: https://leetcode.com/problems/lru-cache/
Difficulty: Medium

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4

'''
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)  # Mark as recently used
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)  # Update and mark as recent
        else:
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last=False)  # Evict LRU
        self.cache[key] = value


# from collections import deque
    
# class LRUCache:
    
#     def __init__(self, capacity: int):
#         self.c = capacity
#         self.m = dict()
#         self.deq = deque()
        
#     def get(self, key: int) -> int:
#         if key in self.m:
#             value = self.m[key]
#             self.deq.remove(key)
#             self.deq.append(key)
#             return value
#         else:
#             return -1
        
#     def put(self, key: int, value: int) -> None:
#         if key not in self.m:
#             if len(self.deq) == self.c:
#                 oldest = self.deq.popleft()
#                 del self.m[oldest]
#         else:
#             self.deq.remove(key)
        
#         self.m[key] = value
#         self.deq.append(key)




# from collections import deque

# class  LRUCache:

#     def __init__(self, capacity: int):
#         self.c = capacity
#         self.m = dict()
#         self.deq = deque()

#     def get (self, key:int) -> int:
#         if key in self.m:
#             value = self.m[key]
#             self.deq.remove(key)
#             self.deq.append(key)
#             return value
#         else:
#             return -1

#     def put (self, key: int, value: int) -> None:
#         if key not in self.m:
#             if len(self.deq) == self.c:
#                 oldest = self.deq.popleft()
#                 del self.m[oldest]
#         else:
#             self.deq.remove(key)

#         self.m[key] = value
#         self.deq.append(key)


# # *-----2022 ATTEMPT--------------

# from collections import deque


# class LRUCache:

#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.cache = {}
#         self.deq = deque()

#     def get(self, key):
#         if key in self.cache:
#             value = self.cache[key]
#             self.deq.remove(key)
#             self.deq.append(key)
#             return value
#         return -1

#     def put(self, key, value):
#         if key in self.cache:
#             self.cache[key] = value
#             self.deq.remove(key)
#             self.deq.append(key)
#         else:
#             if len(self.deq) == self.capacity:
#                 oldest = self.deq.popleft()
#                 del self.cache[oldest]
#             self.cache[key] = value
#             self.deq.append(key)


# # *----------------------*

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# *----------------------*
