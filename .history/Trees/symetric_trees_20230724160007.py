"""
Leet Code: 101. Symmetric Tree
Easy: Tree, DFS, BFS
Link: https://leetcode.com/problems/symmetric-tree/

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

Example 1:
Input: root = [1,2,2,3,4,4,3]
Output: True

"""


def isMirror(root):
    return _isMirror(root, root)

def _isMirror(node1, node2):
    if node1==None and node2==None:
        return True
    if node1==None or node2==None:
        return False
    return((node1.val==node2.val) and (_isMirror(node1.right, node2.left)) and _isMirror(node1.left, node2.right))