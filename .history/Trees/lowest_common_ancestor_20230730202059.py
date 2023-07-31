"""
Lowest Common Ancestor of a Binary Tree
Medium - Tree, DFS
link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
According to the definition of LCA on Wikipedia:
    “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants
    (where we allow a node to be a descendant of itself).”
    

"""
def find_lca(current_node, p, q):
    if not current_node:
        return current_node
    if current_node ==p or current_node == q:
        return current_node
    
    left= find_lca(current_node.left, p, q)
    right = find_lca(current_node.right, p, q)
    
    if left and right:
        return current_node
    elif left:
        return left
    else:
        return right
