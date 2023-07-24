
class Node:
    def __init__(self, value)
    self.value = value
    self.left = None
    self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert(value, self.root)
    
    def _insert(self,value, current_node):
        if value > current_node.value:
            if not current_node.right:
                current_node.right=Node(value)
            self._insert(value, current_node.right)
        elif value < current_node.value:
            if not current_node.left:
                current_node.left=Node(value)
            self._insert(value, current_node.left)
        else:
            print ("Node already exists!")

    def find(self, value):
        if not self.root:
            return False
        if value == self.root.value:
            return True
        else:
            return (self._find(value, self.root))
    
    def _find (self, value, current_node):
        if not current_node:
            return False
        if value == current_node.value:
            
        if value > current_node