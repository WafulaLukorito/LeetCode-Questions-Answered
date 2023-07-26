﻿
    """
    Leetcode: 155. Min Stack
    Link: https://leetcode.com/problems/min-stack/
    Easy - Stack, Design
    
    Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
    
    push(x) -- Push element x onto stack.
    pop() -- Removes the element on top of the stack.
    top() -- Get the top element.
    getMin() -- Retrieve the minimum element in the stack.
    
    The time complexity for each operation (push, pop, top, getMin) is O(1). 
    The space complexity is O(n), where n is the number of elements in the stack.
    
    """
class min_stack:
    def __init__(self):
        self.my_stack=[]
        self.min_el = float('infinity')
    def push(self, value):
        if value < self.min_el:
            self.min_el = value
        self.my_stack.append((value,self.min_el))
    def pop(self):
        if not self.my_stack:
            raise IndexError("Pop from empty stack")
        self.my_stack.pop()
        if self.my_stack:
            self.min_el= self.my_stack[-1[1]]
        else:
            self.curr_min = float('infinity')
    def top(self):
        if not self.my_stack:
            raise IndexError("Stack is empty")
        return self.my_stack[-1][0]
    def get_min(self):
        if not self.my_stack:
            raise IndexError("Stack is empty")
        return self.my_stack[-1][1]

        