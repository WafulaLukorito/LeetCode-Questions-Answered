# Linked_list_cycle
# LeetCode - https://leetcode.com/problems/linked-list-cycle/

"""
Given a linked list, determine if it has a cycle in it.

#* Time Complexity O(n) --> Single loop over our list
#* Space Complexity O(1) --> We only use two extra varibale, no external data structures are used. 
"""


# class Solution(object):
#     def hasCycle(self, head):
#         """
#         :type head: ListNode
#         :rtype: bool
#         """
#         if not head:
#             return False
#         slow = head
#         fast = head
#         while fast.next and fast.next.next:
#             slow = slow.next
#             fast = fast.next.next
#             if slow == fast:
#                 return True
#         return False


def hasCycle(head):
    if not head:
        return False

    hare = head
    tortoise = head

    while hare and tortoise and hare.next:
        hare = hare.next.next
        tortoise = tortoise.next
        if (tortoise == hare):
            return True

    return False
