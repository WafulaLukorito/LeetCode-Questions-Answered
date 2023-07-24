
class Node:
    def __init__(self, value):
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
    
    def _insert(self, value, current_node):
        if value > current_node.value:
            if not current_node.right:
                current_node.right=Node(value)
                return
            self._insert(value, current_node.right)
        elif value < current_node.value:
            if not current_node.left:
                current_node.left=Node(value)
                return
            self._insert(value, current_node.left)
        else:
            raise ValueError ("Node already exists!")

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
            return True
        elif value > current_node.value:
            return self._find(value, current_node.right)
        else:
            return self._find(value,current_node.left)


# Create instance of BST
tree = BST()

# Test case 1: Empty tree
assert not tree.find(1), "Test case 1 failed"

# Test case 2: Single-node tree
tree.insert(1)
assert tree.find(1), "Test case 2 failed"

# Test case 3: Multi-node tree
tree.insert(2)
tree.insert(0)
tree.insert(3)
assert tree.find(2), "Test case 3 failed"
assert tree.find(0), "Test case 3 failed"
assert tree.find(3), "Test case 3 failed"
assert not tree.find(4), "Test case 3 failed"

# Test case 4: Duplicates
try:
    tree.insert(1)
except ValueError:
    pass  # This is what we want to happen
else:
    assert False, "Test case 4 failed"

print("All test cases passed!")
