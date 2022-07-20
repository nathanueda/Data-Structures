"""
Queue ADT Operations:
1. enqueue(item): Add an item to the end of the queue.
2. dequeue(): Remove the first item in the queue.
3. front(): Return the front item in the queue.
4. is_empty(): Return true if and only if the queue is empty. 
"""

"""
Time Complexity:
- enqueue(item): O(1)
- dequeue(): 0(1)
- front(): 0(1)
- is_empty(): 0(1) 
"""

class Queue:
    """Implementation of the queue ADT using a list."""

    def __init__(self):
        """Create an empty queue."""
        self.queue = []

    def is_empty(self):
        """
        Checks to see if the queue is empty.
        @return: True if the queue is empty, false otherwise.
        """
        return len(self.queue) == 0
    
    def dequeue(self):
        """
        Removes the front item from the queue.
        @return: The element dequeued from the queue.
        """
        if self.is_empty():
            raise Exception("Error: Cannot dequeue from an empty queue.")
        else:
            return self.queue.pop(0)
    
    def front(self):
        """
        Peeks at the front item in the queue without removing it.
        @return: The element at the front of the queue. 
        """
        if self.is_empty():
            raise Exception("Error: Queue is empty.")
        else:
            return self.queue[0]
    
    def enqueue(self, item):
        """
        Adds an item to the end of the queue.
        @param: The item to add to the end of the queue.
        """
        self.queue.append(item)

"""
Notes:
- Uses FIFO (first in, first out) ordering.
- Simple arrays with the restrictions that data can only be inserted at the end, 
deleted from the front, and accessed from the front of the queue.
"""