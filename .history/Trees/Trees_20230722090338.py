"""Trees implementation"""

class Node:
    def __init__(self, value):
        self.left= None
        self.right = None
        self.data = value
        
def inorder(node):
    if node:
        #recur left
        inorder(node.left)
        #print node
        print(node.data, end=" ")
        #recur right
        inorder(node.right)

def preorder(node):
    if node:
        #print node
        print (node.data, end=" ")
        #recur left
        preorder(node.left)
        #recur right
        preorder(node.right)
        

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

#* Inorder traversal
#Start from leftmost node and keep going left until you reach a node with no left child
#Then print the root node
# go to the right child of the root node and repeat the process
print ("inorder")
inorder(root)

print ("\n preorder")
preorder(root)


