"""You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list."""
# Merge sorted linked lists
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#         self.prev = None


# def merge_sorted_lists(l1, l2):
#     """Time Complexity: O(M+N), At every call of recursion, we are adding one node to the output.

# Space Complexity: O(M+N), Stack space will be used in recursion.

# """
#     if l1 is None:
#         return l2
#     if l2 is None:
#         return l1
#     if l1.data < l2.data:
#         l1.next = merge_sorted_lists(l1.next, l2)
#         return l1
#     else:
#         l2.next = merge_sorted_lists(l1, l2.next)
#         return l2

# l1 = Node(1)
# l1.next = Node(3)
# l1.next.next = Node(5)
# l1.next.next.next = Node(7)
# l1.next.next.next.next = Node(9)

# l2 = Node(2)
# l2.next = Node(4)
# l2.next.next = Node(6)
# l2.next.next.next = Node(8)
# l2.next.next.next.next = Node(10)

# l3 = merge_sorted_linked_lists(l1, l2)
# while l3 is not None:
#     print(l3.data)
#     l3 = l3.next

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def merge_sorted_linked_lists(l1, l2):
    if not l1:
        return l2
    if not l2:
        return l1

    curr = ListNode(0)
    ans = curr

    while (l1 and l2):
        if (l1.val < l2.val):
            curr.next = l1
            l1 = l1.next
            curr = curr.next
        else:
            curr.next = l2
            l2 = l2.next
            curr = curr.next

    while (l1):
        curr.next = l1
        l1 = l1.next
        curr = curr.next

    while (l2):
        curr.next = l2
        l2 = l2.next
        curr = curr.next

    return ans.next



def merge_sorted_linked_lists(l1, l2):
    if not l1 and l2:
        raise ValueError("Both lists empty!")
    if not l1:
        return l2
    if not l2:
        return l1
    
    temp_node = Node(0)
    current = temp_Node
    
    while l1 and l2:
        if l1 < l2:
            current.next = l1
            l1=l1.next
        else:
            current.next = l2
            l2 = l2.next
        