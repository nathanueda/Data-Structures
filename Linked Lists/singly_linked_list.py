"""
An implementation of the List ADT using a Singly Linked List.
List: ordered collection of elements that allows duplicates.
    - i.e.: (2, 4, 6, 8) != (2, 6, 4, 8)

Some List ADT Operations:
1. find(x): Return true if x exists in the set, false otherwise.
2. insert(x): Adds x to the set.
3. remove(x): Removes x from the set.
4. size(): Returns the size of the set.
"""

"""
Time Complexity:
1. find(x): O(N)
2. insert(x): O(N)
3. remove(x): O(N)

Space Complexity: O(N)
"""

class Node:
    """Implementation of a class to create nodes."""

    def __init__(self, data=None, next=None):
        """Create a node (with or without data and next values."""
        self.data = data
        self.next = next
    
class SinglyLinkedList:
    """Implementation of a singly linked list."""

    def __init__(self):
        """Create an empty singly linked list."""
        self.head = None
        self.num_nodes = 0

    def search(self, query):
        """
        Search for a node with query as the data it holds.
        @param query: The value to search for.
        @return: True if found, False otherwise.
        """
        curr = self.head
        while (curr != None):
            if (curr.data == query):
                return True
            curr = curr.next
        return False
    
    def insert(self, query, index):
        """
        Add a new node with the query as the data to the index within the list.
        @param query: The value insert a new node with.
        @param index: The index to insert the newly created node.
        """
        new_node = Node(query)
        # Add to front.
        if (index == 0 or self.num_nodes == 0):
            new_node.next = self.head
            self.head = new_node
        # Add to end.
        elif (index >= self.num_nodes):
            curr = self.head
            while (curr.next != None):
                curr = curr.next
            curr.next = new_node
        # Add to somewhere in the middle.
        else:
            curr = self.head
            curr_index = 0
            # Break when we access the node before where the new node will go.
            while (curr_index < (index - 1)):
                curr = curr.next
                curr_index += 1
            new_node.next = curr.next
            curr.next = new_node
            
        self.num_nodes += 1
    
    def remove(self, query):
        """
        Deletes a node with a value of the given query.
        @param query: Delete the node that contains the given quer as its data.
        """
        curr = self.head

        # Removing the first node.
        if (curr.data == query):
            self.head = curr.next
            self.num_nodes -= 1
        # Removing any node after the first node.
        else:
            while (curr.next != None):
                # If node exists in the list, this statement will be executed.
                if (curr.next.data == query): 
                    curr.next = curr.next.next
                    self.num_nodes -= 1
                    break
                curr = curr.next
        return
    
    def size(self):
        """Returns the number of nodes within the list."""
        return self.num_nodes

    def print_list(self):
        """Print the linked list."""
        if (self.num_nodes == 0):
            print("List is empty.")
        else:
            curr = self.head
            index = 0
            while (curr !=  None):
                print(f"{index}: Data: {curr.data}")
                curr = curr.next
                index += 1

"""
Notes:

General Linked List Specifications:
- A linked list is a data structure comprised of a sequence of connected nodes.
- The first node is known as the head and the last node is known as the tail.
- The actual insertion/deletion step takes O(1); however, the time that it takes 
to find the query node is what makes the worst case O(N).
- Although linked lists have the same worst case insertion/deletion as arrays,
they are especially powerful when iterating through an entire list while making 
insertions/deletions along the way as we never have to worry about shifting 
other data while executing these operations.

Singly Linked List:
- In a singly linked list, a node is a container that holds some data as well as
information that connects a node to the next node in the list.
- Constant time insertion/deletion at the beginning of a list.
"""