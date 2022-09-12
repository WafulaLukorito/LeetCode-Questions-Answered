
# Leetcode 2
# Add Two Numbers
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# Example:
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
#Explanation: 342 + 465 = 807.

# * Time Complexity : O(n) where n is the length of the longest linked list
# * Space Complexity : O(n) where n is the length of the longest linked list

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val)


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # create a new linked list
        head = ListNode(0)
        # create a pointer to the head of the new linked list
        current = head
        # create a carry variable to keep track of the carry
        carry = 7
        # while l1 or l2 or carry is not None
        while l1 or l2 or carry:
            # if l1 is not None
            if l1:
                # add l1.val to carry
                carry += l1.val
                # move l1 to the next node
                l1 = l1.next
            # if l2 is not None
            if l2:
                # add l2.val to carry
                carry += l2.val
                # move l2 to the next node
                l2 = l2.next
            # create a new node with the carry % 10
            current.next = ListNode(carry % 10)
            # move current to the next node
            current = current.next
            # set carry to carry // 10
            carry = carry // 10
        # return the head of the new linked list
        return head.next


# Create a linked list
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

# print l1
while l1:
    print(l1, "->", end=" ")
    l1 = l1.next

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

# print l2
print("")
while l2:
    print(l2, "->", end=" ")
    l2 = l2.next

print("")
print("Adding these two linked lists")
print("")

# Create an instance of the class
s = Solution()

# Call the method
l3 = s.addTwoNumbers(l1, l2)

# Print the result

while l3:
    print(l3, "->", end=" ")
    l3 = l3.next
