    """
    Kth Smallest Element in a BST
    
    Link: https://leetcode.com/problems/kth-smallest-element-in-a-bst/
    Medium - Tree, DFS
    
    Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
    
    Note:
    You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
    
    Time Complexity: O(N): N is the number of nodes in the tree
    
    """
    
# def kthSmallest(root, k):
#     #*Create a stack
#     stack = []
    
#     #*Create a pointer to the root node
#     current_node = root
    
#     #*Create a counter
#     count = 0
    
#     #*While stack is not empty or current node is not null
#     while stack or current_node:
        
#         #*While current node is not null
#         while current_node:
            
#             #*Append current node to stack
#             stack.append(current_node)
            
#             #*Move current node to left child
#             current_node = current_node.left
        
#         #*Pop from stack
#         current_node = stack.pop()
        
#         #*Increment counter
#         count+=1
        
#         #*If counter is equal to k, return current node
#         if count == k:
#             return current_node.val
        
#         #*# only traverse the right subtree if kth element is not found
#         current_node = current_node.right
    
#     return None

def kth_smallest(current_node, k):


def _kth_smallest(current_node,k):
    if not current_node:
        return []
    
    
    
    
    count = 0
    while count <= k:
        left = _kth_smallest(current_node.left, k)
        root = [current_node]
        right = _kth_smallest(current_node.right, k)
        
        m
        count +=1
        if count ==k:
            return 
    
    
    
    
    
    
    
    
    
    

    """
    This code would work, but it's not the most efficient. It always traverses the whole tree, even if the kth smallest element is found. There are other more efficient methods using iterative in-order traversal which stops once the kth smallest is found.
    """

def kth_smallest(current_node, k):
    # Base case
    if not current_node:
        return []

    # In-order traversal: left -> root -> right
    left = kth_smallest(current_node.left, k)
    root = [current_node.val]  # Make the root a single-item list
    right = kth_smallest(current_node.right, k)
    
    # Combine the results
    my_list = left + root + right

    # Return k-th smallest element, if it exists
    return my_list[k - 1] if len(my_list) >= k else None


class Solution:
    def kth_smallest(self, root, k):
        self.current_node = root
        self.k = k
        self.res = self._kth_smallest(self.current_node)
        return self.res.val if self.res else None
    
    def _kth_smallest(current_node):
        if not current_node:
            return
        self._kth_smallest(current_node.left)
        if self.k ==0:
            self.res = current_node
        self.k -=1
        self._kth_smallest(current_node.right)