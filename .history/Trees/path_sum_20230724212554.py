
    """
    # 112 Path Sum
    Easy: Tree, DFS, BFS
    Link: https://leetcode.com/problems/path-sum/
    
    Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
    
    #Time complexity: O(n) where n is the number of nodes in the tree
    
    #Space complexity: O(n) where n is the number of nodes in the tree
    
    """
class Solution:
    def has_path_sum(self, root, sum):
        return self._hasSum(root, sum, 0)
    def _hasSum(self, curr_node, sum, curr_sum):
        if not curr_node:
            return False
        curr_sum+=curr_node.val
        if (curr_sum==sum and not curr_node.left and not curr_node.right):
            return True
        else:
            return ((self._hasSum(curr_node.left, sum, curr_sum) or (self._hasSum(curr_node.right, sum, curr_sum))))