# Remove Nth Node From End of List
"""
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?
"""

# *Time Complexity: O(2n) = O(n)
# *Space Complexity: O(1)


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# One Solution
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # *Create a dummy node to point to the head
        dummy = ListNode(0)
        dummy.next = head
        # *Create a fast pointer and a slow pointer
        fast = dummy
        slow = dummy
        # *Move the fast pointer n nodes ahead
        for i in range(n):
            fast = fast.next
        # *Move the fast pointer to the end of the list
        while fast.next:
            fast = fast.next
            slow = slow.next
        # *Remove the node
        slow.next = slow.next.next
        return dummy.next

# Another Solution


class Solution:
    
    
    
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # *Create a dummy node to point to the head
        dummy = ListNode(0)
        dummy.next = head
        # *Create a fast pointer and a slow pointer
        fast = dummy
        slow = dummy
        # *Move the fast pointer n nodes ahead
        for i in range(n):
            fast = fast.next
        # *Move the fast pointer to the end of the list
        while fast.next:
            fast = fast.next
            slow = slow.next
        # *Remove the node
        slow.next = slow.next.next
        return dummy.next


# *Main function to test the above solution
def main():
    print("TESTING REMOVE NTH NODE FROM END OF LIST...")
    # *Test Case 1
    test_head = ListNode(1)
    test_head.next = ListNode(2)
    test_head.next.next = ListNode(3)
    test_head.next.next.next = ListNode(4)
    test_head.next.next.next.next = ListNode(5)
    test_n = 2
    test_solution = Solution()
    test_result = test_solution.removeNthFromEnd(test_head, test_n)
    print(test_result.val)
    print(test_result.next.val)
    print(test_result.next.next.val)
    print(test_result.next.next.next.val)
    print("END OF TESTING...")


main()


# l1 = ListNode(1)
# l1.next = ListNode(2)
# l1.next.next = ListNode(3)
# l1.next.next.next = ListNode(4)
# l1.next.next.next.next = ListNode(5)

# # Print l1
# print("l1: ", end="")
# while l1:
#     print(l1.val, end=" ")
#     l1 = l1.next

# s = Solution()
# s.removeNthFromEnd(l1, 2)

# print("")

# # Print l1
# print("l1: ", end="")
# while l1:
#     print(l1.val, end=" ")
#     l1 = l1.next
