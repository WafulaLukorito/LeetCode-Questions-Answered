# Reverse a singly linked list.
# Example:
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
# Follow up:
# A linked list can be reversed either iteratively or recursively. Could you implement both?

# * Time Complexity: O(n) where n is the number of nodes in the linked list.
# * Space Complexity: O(1) since we are not using any extra space.





# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # def reverseList(self, head: ListNode) -> ListNode:
    #     if not head:
    #         return None
    #     prev = None
    #     curr = head
    #     while curr:
    #         next = curr.next
    #         curr.next = prev
    #         prev = curr
    #         curr = next
    #     return prev

    def reverseList(self, head):
        if not head:
            return None
        prev = None
        curr = head
        
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev
            


if __name__ == "__main__":
    # Create a linked list
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    # Print the linked list
    curr = head
    while curr:
        print(curr.val, end="->")
        curr = curr.next
    print("NULL")
    # Reverse the linked list
    sol = Solution()
    head = sol.reverseList(head)
    # Print the reversed linked list
    curr = head
    while curr:
        print(curr.val, end="->")
        curr = curr.next
    print("NULL")
