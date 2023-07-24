
class Node:
    def __init__(self, value):
        self.data = value
        self.left=None
        self.right=None
        
class BST:
    def __init__(self):
        self.root=None
        
    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert(value, self.root)
    
    def _insert(self, value, current_node):
        if value < current_node.data:
            if current_node.left:
                self._insert(value, current_node.left)
            else:
                current_node.left=Node(value)
        elif value > current_node.data:
            if current_node.right:
                self._insert(value, current_node.right)
            else:
                current_node.right= Node(value)
        else:
            print ("Node already exists!")
            
            
    def find(self, value):
        if value==self.root.data:
            return True
        else:
            self._find(value, self.root)
    
    def _find(self, value, current_node):
        if current_node.data > value:
            if current_node.left==None:
                return False
            elif (current_node.left.data == value):
                    return True
            else:
                self._find(value, current_node)
        else:
            if current_node.right == None:
                return False
            elif current_node.right.data == value:
                return True
            else:
                self._find(value, current_node)
    
class Node:
    def __init__(self, value):
        self.value=value
        self.right=None
        self.left=None

class BST:
    def __init__(self, value):
        
        