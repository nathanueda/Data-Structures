"""
An implementation of a Trie.

Trie Operations:
1. search(x): Return the node containing x is found, None otherwise.
2. insert(x): Adds x to the set.
3. remove(x): Removes x from the set.
4. size(): Returns the size of the set.
"""

"""
Time Complexity (Worst/Average/Best):
- k is the length of the longest key in the trie.
- n is the number of elements in the trie.
1. search(x): O(k)
2. insert(x): O(k)
3. remove(x): O(k)

Space Complexity: O(|Σ|^(k+1))
- If each word was length k, the 1st level of the trie would have 1 node, the
2nd level would have |Σ| nodes, the third would have |Σ|^2 and so on. Therefore,
for lenght k words, we would get the above space complexity.
"""""

class Node:
    """Implementation of a class to create nodes."""

    def __init__(self):
        """Create a node."""
        # Keys are letters, value are Nodes.
        self.children = {}
        self.is_word = False

class Trie:
    """Implmentation of a trie."""

    def __init__(self):
        """Create an empty trie."""
        self.root = Node()
        self.num_words = 0
        self.words = []

    def search(self, word):
        """
        Search for a node with word as the data it holds.
        @param word: The word to search for.
        @return: The node if found, None otherwise.
        """
        if self.size() == 1:
            return None
        else:
            curr = self.root
            for char in word:
                # char is found among curr's children (curr has an outgoing edge
                # labeled by char).
                if curr.children.get(char):
                    # Follow the edge.
                    curr = curr.children[char]
                else:
                    return None

            if curr.is_word:
                return curr
            else:
                return None

    def insert(self, word):
        """
        Add a new node with the word as the data to the trie.
        @param word: The value insert a new node with.
        """
        curr = self.root
        for char in word:
            # char is found among curr's children (curr has an outgoing edge
            # labeled by char).
            if curr.children.get(char):
                # Follow the edge.
                curr = curr.children[char]
            else:
                new_node = Node()
                # Create an outgoing edge from curr labeled by char.    
                curr.children[char] = new_node
                # Traverse to it.
                curr = new_node
        
        # If word was not already inserted, this condition is met.
        if curr.is_word == False:
            curr.is_word = True
            self.num_words += 1
            self.words.append(word)

    def remove(self, word):
        """
        Deletes a node with a value of the given word.
        @param word: Delete the node that contains the given word as its data.
        """
        curr = self.root
        for char in word:
            # char is found among curr's children (curr has an outgoing edge
            # labeled by char).
            if curr.children.get(char):
                # Follow the edge.
                curr = curr.children[char]
            # Word did not previously exist in the trie.
            else:
                return
        
        # If word was not already inserted, this condition is met.
        if curr.is_word == True:
            curr.is_word = False
            self.num_words -= 1
            self.words.remove(word)
    
    def auto_complete(self, prefix):
        """
        Prints all the words that start with a given prefix.
        @param prefix: The prefix to search for words that start with it.
        """
        curr = self.root
        for char in prefix:
            # char is found among curr's children (curr has an outgoing edge
            # labeled by char).
            if curr.children.get(char):
                # Follow the edge.
                curr = curr.children[char]
            else:
                # Prefix doesn't exist in the trie.
                return None

        # If reached, prefix exists in trie.
        end_of_prefix = curr
        # Printing all the words that start with prefix.
        self.preorder_traversal(end_of_prefix, prefix)

    def size(self):
        """
        Returns the number of words within the trie.
        @return: number of words in the trie.
        """
        return self.num_words

    def preorder_traversal(self, node, word=""):
        """
        Prints the tree in ascending alphabetical order. Visits the current node 
        before its child nodes.
        @param node: The node to begin the traversal from (root). 
        @param word: The word to print. Initially empty to append to (unless 
        using for auto complete).
        """
        if node.is_word:
            print(word)
        
        for char, curr in sorted(node.children.items()):
            self.preorder_traversal(curr, word + char)

    def postorder_traversal(self, node, word=""):
        """
        Prints the tree in descending alphabetical order. Visits the left node, 
        then the right node, then the current node.
        @param node: The node to begin the traversal from (root). 
        @param word: The word to print. Initially empty to append to (unless 
        using for auto complete).
        """  
        # Visiting each child in descending order.
        for char, curr in sorted(node.children.items(), reverse=True):
            self.postorder_traversal(curr, word + char)

        if node.is_word:
            print(word)

    def level_order_traversal(self, node):
        """
        Prints the trie from top to bottom, level by level, left to right.
        Utilizes a modified version of breadth first search.
        Prints the words from shortest length to longest.
        @param node: The node to begin the traversal from.
        """
        queue = [(node, "")]
        words_printed = 0   
        words = []
        
        while queue:
            curr, str = queue.pop(0)
        
            if curr.is_word:

                # This if else enables the ability to print same length words in
                # alphabetical order.
                # List is empty or word is the same length as other entries.
                if len(words) == 0 or len(words[0]) == len(str):
                    words.append(str)
                # New word is longer than previous words.
                else:
                    for word in sorted(words):
                        words_printed += 1
                        print(word)
                    words.clear()
                    words.append(str)
            
            if words_printed == self.num_words:
                break

            # Adding each child to the queue.
            for char, child in curr.children.items():
                queue.append((child, str + char))
        
        if len(words):
            for word in sorted(words):
                words_printed += 1
                print(word)

    def print_list(self):
        """
        Prints the words in the order of insertion.
        """
        for word in self.words:
            print(word)
            
"""
Notes:

General Tree Terminology:
- Root node: the top most node of a tree that does not have a parent node.
- Child node: a node directly below a node A is the child of node A.
- Parent node: a node directly above a node A is the parent of node A.
- Ancestors: all nodes that it stems from.
- Descendants: all nodes that stem from a node.
- Sibling: a node that shares the same parent.
- Leaf nodes: a node that has no children nodes. 
- Internal nodes: nodes that have children nodes.
- Height of a node: the longest path (in number of edges) from the node to a 
leaf. A leaf will have a height of 0.
- Depth of a node: the number of edges from the node to the root. A root node 
will have a depth of 0.

Tree:
- A tree is a collection of nodes and edges. 
- Each tree (typically) has a root node.
- Trees have 2 properties:
    1. No undirected cycles.
        - A cycle is a path that starts at a given vertex and ends at the same
        vertex.
    2. Must be connected.
        - There must be a path from any arbitrary vertex to every other vertex.

Trie:
- A trie (sometimes called a prefix tree) is a type of tree that is ideal for 
text-based features such as autocomplete.
- Each node can have at most |Σ| children, where |Σ| represents the size of the
alphabet.
- Edges are labeled by a single character in Σ.
- Words are represented by paths down the tree.
- A newly created trie contains 1 node with no edges.
- Order of insertion does not affect the trie structure (unlike in a ternary 
search tree).
- The height of the tree is the length of the longest word.
- Effective when dense (there are many words using the allocated pointers), 
ineffective if sparse (this is when ternary search trees are more effective).
"""