    """
    Leetcode: 104. Maximum Depth of Binary Tree
    Easy: BFS, DFS
    Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/
    
    Given a binary tree, find its maximum depth.
    
    The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
    
    Note: A leaf is a node with no children.
    
    Time complexity: O(n) where n is the number of nodes in the tree
    space complexity: O(n) where n is the number of nodes in the tree
    """

def maxDepth(root: TreeNode) -> int:
    if not root:
        return 0
    left = maxDepth(root.left)+1
    right = maxDepth(root.right)+1
    
    return max(left, right)
