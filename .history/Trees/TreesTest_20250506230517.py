
class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value
        
        
def inorder(node):
    if node:
        inorder(node.left)
        print(node.data)
        inorder(node.right)
        
        
root = Node(4)

root.right=Node(5)
root.left=Node(9)
root.left.left=Node(7)

inorder(root)