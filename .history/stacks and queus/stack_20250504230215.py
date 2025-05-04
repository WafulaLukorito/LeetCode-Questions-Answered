    """Stack implementation as a list
    """
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)  # O(1)

    def pop(self):
        if not self.is_empty():  # Add check for empty stack
            return self.stack.pop()  # O(1)
        else:
            return None  # Or raise an exception, depending on desired behavior

    def peek(self):
        if not self.is_empty():  # Add check for empty stack
            return self.stack[-1]   # O(1)
        else:
            return None  # Or raise an exception

    def is_empty(self):
        return not self.stack  # More Pythonic and still O(1)

    def size(self):
        return len(self.stack)  # O(1)

    def __str__(self):
        return str(self.stack)  # O(n) - Note: String conversion can be O(n) in the worst case

# Example Usage:
my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
print(my_stack)          # Output: [1, 2]
print(my_stack.peek())     # Output: 2
print(my_stack.pop())      # Output: 2
print(my_stack.is_empty()) # Output: False
print(my_stack.size())     # Output: 1

class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        return self.stack.append(item)
    
    def pop(self):
        return self.stack.pop()
    
    def peek(self):
        return sel.f.stack[-1]
    
    def is_empty(self):
        return self.stack ==[]
    
    def size(self):
        return len(self.stack)
    def __str__(self):
        return str(self.stack)


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