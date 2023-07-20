    """Stack implementation as a list
    """
class Stack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item) # O(1)
    def pop(self):
        return self.stack.pop() # O(1)
    def peek(self):
        return self.stack[-1]  # O(1)
    def is_empty(self):
        return self.stack == [] # O(1)
    def size(self):
        return len(self.stack) # O(1)
    def __str__(self):
        return str(self.stack) # O(1)
    
class Stack:
    def __init__(self):
        self.stack = []
    
    def get_size(self):
        return len(self.stack)
        
    def push(self, item):
        self.stack.append(item)
    
    def pop (self):
        if len(self.stack) > 0:
            return self.stack.pop()
        
    def get_head(self):
        if not self.stack:
            return None
        return self.stack[-1]
    
    def __str__(self):
        return str(self.stack)