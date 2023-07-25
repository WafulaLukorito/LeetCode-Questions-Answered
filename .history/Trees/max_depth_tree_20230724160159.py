    """
    #Leetcode 104. Maximum Depth of Binary Tree
    #Easy: Tree, DFS, BFS
    #Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/
    
    Given a binary tree, find its maximum depth.
    The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
    
    Note: A leaf is a node with no children.
    
    Example:
    Given binary tree [3,9,20,null,null,15,7], return its depth = 3.
    
    Time complexity: O(n) where n is the number of nodes in the tree
    Space complexity: O(n) where n is the number of nodes in the tree
    
    """

def max_tree_depth(root):
    if root is None:
        return 0
    else:
        left_depth = max_tree_depth(root.left)
        right_depth = max_tree_depth(root.right)
        
        if left_depth > right_depth:
            return left_depth+1
        else:
            return right_depth+1  #*Note: +1 is for the root node