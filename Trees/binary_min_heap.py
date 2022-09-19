"""
An implementation of the Binary Min Heap ADT using a list.

Priority Queue ADT Operations:
1. insert(value): Add an element to the priority queue.
2. peek(): Look at the highest priority element in the priority queue.
3. pop(): Remove the highest priority element from the priority queue.
"""

"""
Worst Case Time Complexity:
1. insert(value): O(logN)
2. peek(): O(1)
3. pop(): O(logN)

Space Complexity: O(logN)
"""
        
class BinaryMinHeap:
    """Implementation of a binary min heap using an array."""

    def __init__(self):
        """Create an empty binary min heap."""
        self.heap = []
    
    def size(self):
        """Returns the size of the heap."""
        return len(self.heap)
    
    def get_root(self):
        """
        Return the root node (node with the highest priority).
        @return: the root node.
        """
        return self.heap[0]

    def get_value_at_index(self, index):
        """
        Returns the value at a given index.
        @param index: The index to return the value for.
        """
        return self.heap[index]
    
    def get_last_node(self):
        """
        Return the bottom right node in the heap (node with lowest priority).
        @return: the last node.
        """
        return self.heap[-1]
    
    def get_left_child_index(self, parent_index):
        """
        Return the index of the left child for a given parent node.
        @param parent_index: index of the parent node we want to find the left 
        child index for.
        @return: the index of the left child.
        """
        return (parent_index * 2) + 1

    def get_right_child_index(self, parent_index):
        """
        Return the index of the right child for a given parent node.
        @param parent_index: index of the parent node we want to find the right 
        child index for.
        @return: the index of the right child.
        """
        return (parent_index * 2) + 2
    
    def get_parent_index(self, child_index):
        """
        Return the index of the parent for a given child node.
        @param child_index: index of the child node we want to find the parent
        index for.
        @return: the index of the parent node.
        """
        return (child_index - 1) // 2

    def insert(self, value):
        """
        Insert a node with the given value into the heap at its proper location.
        @param value: the value to give the newly created node. 
        """
        self.heap.append(value)
        new_node_index = len(self.heap) - 1

        parent_index = self.get_parent_index(new_node_index)
        # While new node has a parent and a higher priority than its parent...
        while (new_node_index > 0 and 
        self.heap[new_node_index] < self.heap[parent_index]):
            # ...swap the new node with the parent node.
            self.heap[parent_index], self.heap[new_node_index] = \
            self.heap[new_node_index], self.heap[parent_index]

            # Update indices.
            new_node_index = parent_index
            parent_index = self.get_parent_index(new_node_index)
        
        # Once loops compeletes execution, the new node is in its proper place.
    
    def pop(self):
        """
        Remove the node with the highest priority (the root) from the heap.
        """

        # Remove last element from heap and make it the new root.
        self.heap[0] = self.heap.pop()

        # Index to represent to new root we need to move into proper index.
        trickle_node_index = 0

        # While trickle node is not upholding the heap property.
        while self.has_higher_priority_child(trickle_node_index):
            higher_pri_child_index = \
                self.get_higher_priority_child_index(trickle_node_index)

            # Swap trickle node with its larger child
            self.heap[trickle_node_index], self.heap[higher_pri_child_index] = \
            self.heap[higher_pri_child_index], self.heap[trickle_node_index]

            # Update index of trickle node.
            trickle_node_index = higher_pri_child_index
    
    def has_higher_priority_child(self, index):
        """
        Helper function for pop. Checks whether the node at given index has a 
        left and/or right child and if either of those children are less than 
        (have a higher priority than) the node at index.
        @param index: the index of the node to check.
        """

        left_child_index = self.get_left_child_index(index)
        right_child_index = self.get_right_child_index(index)

        left_child_valid = True
        right_child_valid = True

        # No left child.
        if left_child_index > self.size() - 1:
            left_child_valid = False
        
        # No right child.
        if right_child_index > self.size() - 1:
            right_child_valid = False

        # Has a left child and that child is < current node or has a right child
        # and that child is < current node.
        return ((left_child_valid and self.heap[left_child_index] < \
        self.heap[index]) or \
        (right_child_valid and self.heap[right_child_index] < \
        self.heap[index]))
    
    def get_higher_priority_child_index(self, index):
        """
        Helper function for pop. Calculates the index of the child node that has
        a higher priority than its current parent node at the given index. When 
        used, it is already known that a higher priority child exists.
        @param index: The index of the node to calculate its higher priority 
        child node for.
        """

        left_child_index = self.get_left_child_index(index)
        right_child_index = self.get_right_child_index(index)

        # If no right child, higher priority child must be left child.
        if right_child_index > self.size() - 1:
            return left_child_index
        elif left_child_index > self.size() - 1:
            return right_child_index

        
        # If right child has higher priority than left child.
        if self.heap[right_child_index] < self.heap[left_child_index]:
            return right_child_index
        else:
            return left_child_index

"""
Notes:

Binary Heap:
- A binary heap is a tree based data structure that satisfies three properties:
    1. Heap Property: The value of each node must have a higher priority than
    each of its descendant nodes.
    2. Shape Property: The tree is a complete tree. In other words, all levels 
    of the tree, except possibly the bottom level, are fully filled. If the
    bottom level is not fully filled, then the nodes that are on the bottom 
    level are filled from left to right.
    3. Binary Tree Property (only a requirement for binary heaps): All nodes in 
    the tree must have either 0, 1, or 2 children.

Priority:
- The priority of a node is determined by what type of heap is being used.
- A min-heap is a heap where every node is smaller than (or equal to) all of its
children (if it has any). Therefore, the smaller the value, the higher the 
priority.
- A max-heap is a heap where every node is greater than (or equal to) all of its
children (if it has any). Therefore, the larger the value, the higher the 
priority.

Implementing a Heap as an Array:
- It is common to implement a heap as an array because it will make finding the
last node (important for heap operations) more efficient and all of the data 
will be localized in memory (making it faster in practice). We are treating the
heap as an ADT and implementing it using an array.
- Using this implementation, the root is stored in index 0, the next node (in a 
level order traversal) is stored at index 1, then at index 2, and so on until we
reach the last node which will always be the final element of the array.
- To find the left child of any node use: (index * 2) + 1.
- To find the right child of any node use: (index * 2) + 2.
- To find the parent of a node use: (index - 1) / 2.
"""