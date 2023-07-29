
class Solution:
    def invertTree(self, root):
        if root:
            # Swap the left child and the right child
            root.left, root.right = root.right, root.left
            # Invert the left subtree
            self.invertTree(root.left)
            # Invert the right subtree
            self.invertTree(root.right)
        return root
