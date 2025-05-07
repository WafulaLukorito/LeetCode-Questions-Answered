
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
        
def preorder(node):
    if node:
        print (node.data)
        preorder(node.left)
        preorder(node.right)

def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data)


root = Node(4)

root.left=Node(5)
root.right=Node(6)
root.left.left=Node(7)

postorder(root)