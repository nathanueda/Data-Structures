"""
An implementation of the List ADT using a Doubly Linked List.
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

    def __init__(self, data=None, prev=None, next=None):
        """Create a node."""
        self.data = data
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    """Implementation of a doubly linked list."""

    def __init__(self):
        """Create an empty singly linked list."""
        self.head = None
        self.tail = None
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
        # List is empty.
        if (self.num_nodes == 0):
            self.head = new_node
            self.tail = new_node
            self.head.prev = None
            self.tail.next = None
        else:
            # Add to front.
            if (index == 0):
                new_node.next = self.head
                new_node.prev = None
                self.head.prev = new_node
                self.head = new_node
            # Add to end.
            elif (index >= self.num_nodes):
                new_node.prev = self.tail
                new_node.next = None
                self.tail.next = new_node
                self.tail = new_node
            # Add to somewhere in the middle.
            else:
                curr = self.head
                curr_index = 0
            # Break when we access the node before where the new node will go.
                while (curr_index < (index - 1)):
                    curr = curr.next
                    curr_index += 1
                new_node.next = curr.next
                new_node.prev = curr
                curr.next = new_node
                curr.next.next.prev = new_node
            
        self.num_nodes += 1

    def remove(self, query):
        """
        Deletes a node with a value of the given query.
        @param query: Delete the node that contains the given quer as its data.
        """

        # Removing the first node.
        if (self.head.data == query):
            self.head = self.head.next
            self.head.prev = None
            self.num_nodes -= 1
        # Removing the last node
        elif (self.tail.data == query):
            self.tail = self.tail.prev
            self.tail.next = None
            self.num_nodes -= 1
        # Removing any node in between the first and last nodes.
        else:
            curr = self.head
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

    def print_list_backwards(self):
        """Print the linked list in reverse order."""
        if (self.num_nodes == 0):
            print("List is empty.")
        else:
            curr = self.tail
            index = self.num_nodes - 1
            while (curr != None):
                print(f"{index}: Data: {curr.data}")
                curr = curr.prev
                index -= 1

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

Doubly Linked List:
- In a doubly linked list, a node is a container that holds some data as well as
information that connects a node to the next node and previous node in the list.
- Constant time insertion/deletion at the beginning and end of a list.
"""