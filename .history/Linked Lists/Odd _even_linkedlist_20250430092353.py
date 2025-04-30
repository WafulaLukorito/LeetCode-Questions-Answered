# Odd even linkedlist
# Leetcode 328. Odd Even Linked List https: // leetcode.com/problems/odd-even-linked-list/

"""
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:

Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL
Example 2:

Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL
Note:

The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...
"""
# * Time complexity: O(n) where n is the number of nodes in the linked list. We traverse the entire linked list once.
# * Space complexity: O(1) since we do not use any additional data structures.

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None




class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        
        if not head or head.next:
            return head
        odd = head
        even= head.next
        even_head= even
        
        while even and even.next:
            odd.next=even.next
            odd = odd.next
            even.next=odd.next
            even=even.next
        odd.next = even_head
        return head

# class Solution:
#     def oddEvenList(self, head: ListNode) -> ListNode:
#        # Base case
#         if not head:
#             return head
#        # Initialize first nodes of odd and even lists
#         odd = head
#         even = head.next
#         # Remember the first node of even list so that we can connect the even list at the end of odd list.
#         even_head = even
#         # Traverse the list
#         while even and even.next:
#             # Odd nodes are linked to next odd node
#             odd.next = even.next
#             odd = odd.next
#             # Even nodes are linked to next even node
#             even.next = odd.next
#             even = even.next
#         # Link the even list at the end of odd list
#         odd.next = even_head
#         return head


# Main function to run the test cases:


def main():
    print("TESTS")
    # Test 1
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(6)
    head.next.next.next.next.next.next = ListNode(7)
    head.next.next.next.next.next.next.next = ListNode(8)
    head.next.next.next.next.next.next.next.next = ListNode(9)

    print("Input: 1->2->3->4->5->6->7->8->9->NULL")
    print("Output: ", end="")

    result = Solution().oddEvenList(head)
    while result:
        print(result.val, end="->")
        result = result.next
    print("NULL")


main()
