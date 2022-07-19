"""
Stack ADT Operations:
1. pop(): Remove the top item from the stack.
2. push(item): Add an item to the top of the stack.
3. top(): Return the top of the stack.
4. is_empty(): Return true if and only if the stack is empty.
"""

"""
Time Complexity:
- pop(): O(1)
- push(item): O(1)
- top(): 0(1)
- is_empty(): 0(1)
"""

class Stack:
    """Implementation of the stack ADT using a list."""

    def __init__(self):
        """Create an empty stack."""
        self.stack = []
    
    def is_empty(self):
        """
        Checks to see if the stack is empty.
        @return: True if the stack is empty, false otherwise.
        """
        return len(self.stack) == 0

    def pop(self):
        """
        Removes the top item from the stack.
        @return: The element popped from the stack.
        """
        if self.is_empty():
            raise Exception("Error: Cannot pop an empty stack.")
        else:
            return self.stack.pop()

    def top(self):
        """
        Peeks at the top item of the stack without popping it.
        @return: The element on top of the stack.
        """
        if self.is_empty():
            raise Exception("Error: Stack is empty.")
        else:
            return self.stack[-1]
    
    def push(self, item):
        """
        Adds an item to the top of the stack.
        @param: The item to end to the top of the stack.
        """
        self.stack.append(item)

"""
Notes:
- Uses LIFO (last-in, first-out) ordering.
- Data can only be inserted, deleted, and accessed at the end of a stack.
"""