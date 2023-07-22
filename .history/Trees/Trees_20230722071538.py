"""Trees implementation"""

class Node:
    def __init__(self, value):
        self.left= None
        self.right = None
        self.data = value

#          1
#        /   \
#       2     3
#      / \   / \
#     4   5 6   7

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right= Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

def print_tree(root):
    if root:
        print_tree(root.left)
        print(root.data)
        print_tree(root.right)

print_tree(root)