﻿    """
    Leetcode: 20. Valid Parentheses
    Easy - String, Stack
    Link: https://leetcode.com/problems/valid-parentheses/
    
    Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
    
    An input string is valid if:
        1. Open brackets must be closed by the same type of brackets.
        2. Open brackets must be closed in the correct order.
        
    Note that an empty string is also considered valid.
    
    Time Complexity: O(n): n is the length of the string
    Space Complexity: O(n) for the stack
    """
#First approach

def isValid(s: str) -> bool:
    stack = []
    bracket_map = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in bracket_map:  # This character is a closing bracket
            if stack:  # Check if the stack is not empty
                top_element = stack.pop()
            else:
                top_element = '#'
            if bracket_map[char] != top_element:
                return False
        else:  # This character is an opening bracket
            stack.append(char)
    return not stack  # Check if the stack is empty at the end



#second Approach

def isValidStr(my_string):
    if not my_string:
        return True
    my_stack =[]
    opening_brackets = ['{', '(', '[']
    bracket_pairs=[('{','}'), ('(',')'), ('[',']')]

    for char in my_string:
        if char in opening_brackets:
            my_stack.append(char)
        else:
            if not my_stack:
                return False
            top_bracket=my_stack.pop()
            if (top_bracket, char) not in bracket_pairs:
                return False

    return not my_stack