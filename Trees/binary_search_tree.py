"""
An implementation of the Tree ADT using a Binary Search Tree.

Some Tree ADT Operations:
1. search(x): Return the node containing x is found, None otherwise.
2. insert(x): Adds x to the set.
3. remove(x): Removes x from the set.
4. size(): Returns the size of the set.
"""

"""
Worst Case Time Complexity:
1. search(x): O(N)
2. insert(x): O(N)
3. remove(x): O(N)

Average Time Complexity:
1. search(x): O(logN)
2. insert(x): O(logN)
3. remove(x): O(logN)

Space Complexity: O(N)
"""""

class Node:
    """Implementation of a class to create nodes."""

    def __init__(self, data=None, parent=None, left=None, right=None):
        """Create a node."""
        self.data = data
        self.parent = parent
        self.left = left
        self.right = right
    
    
class BinarySearchTree:
    """Implementation of a binary search tree."""

    def __init__(self):
        """Create an empty binary search tree."""
        self.root = None
        self.num_nodes = 0
    
    def search(self, query):
        """
        Search for a node with query as the data it holds.
        @param query: The value to search for.
        @return: The node if found, None otherwise.
        """

        if self.size() == 0:
            return None

        curr = self.root
        while curr.data != query:
            if query < curr.data:
                curr = curr.left
            elif query > curr.data:
                curr = curr.right
            if curr == None:
                return None
        return curr
    
    def insert(self, query):
        """
        Add a new node with the query as the data to the binary search tree.
        @param query: The value insert a new node with.
        """
        new_node = Node(query)
        curr = self.root
        if self.size() == 0:
            self.root = new_node
            self.num_nodes += 1
        else:
            # Condition met if the query is already in the tree.
            while query != curr.data:
                if query < curr.data:
                    if curr.left == None:
                        curr.left = new_node
                        new_node.parent = curr
                        self.num_nodes += 1
                    else:
                        curr = curr.left
                elif query > curr.data:
                    if curr.right == None:
                        curr.right = new_node
                        new_node.parent = curr
                        self.num_nodes += 1
                    else:
                        curr = curr.right
        return

    def remove(self, query):
        """
        Deletes a node with a value of the given query.
        @param query: Delete the node that contains the given query as its data.
        """
        curr = self.root
        while query != curr.data:
            if query < curr.data:
                curr = curr.left
            elif query > curr.data:
                curr = curr.right
            # Condition met if query is not in the tree.
            if curr == None:
                return
        # Found node to delete.

        # Case 1: Node has no children. 
        # Delete the node.
        if curr.left == None and curr.right == None:
            if self.size() == 1:
                self.root = None
            elif curr.parent.data < curr.data:
                curr.parent.right = None
            elif curr.parent.data > curr.data:
                curr.parent.left = None
        # Case 2: Node has one child. 
        elif curr.left == None or curr.right == None: 
            if curr.left != None:
                child_node = curr.left
            else:
                child_node = curr.right
            
            # Connect curr's parent to curr's child.
            if curr.parent.data < curr.data:
                curr.parent.right = child_node
            elif curr.parent.data > curr.data:
                curr.parent.left = child_node    
            child_node.parent = curr.parent
        # Case 3: Node has 2 children. 
        # Replace curr with successor. 
        # Remove original successor.
        else:
            successor = self.find_successor(curr)
            # Connecting successor's child to successor's parent.
            # If successor is its parent's left child.
            if successor.data < successor.parent.data:
                successor.parent.left = successor.right
            else:
                successor.parent.right = successor.right
            curr.data = successor.data
        
        self.num_nodes -= 1
    
    def find_successor(self, node):
        """
        Find the successor of a given node (the node that is larger than a node 
        by the smallest margin).
        @param node: The node to find the succeessor of.
        @return: The successor of node.
        """
        # Case 1: node has a right child. Find smallest node in right subtree.
        if node.right != None:
            # Traverse right once...
            curr = node.right
            # ...then left all the way.
            while curr.left != None:
                curr = curr.left
            return curr
        # Case 2: node doesn't have a right child.
        else:
            curr = node
            while curr.parent != None:
                # Once node is the left child of its parent, return the parent.
                if curr.data < curr.parent.data:
                    return curr.parent
                else:
                    # Continuously traverse up the tree.
                    curr = curr.parent
        # No successor exists.
        return None

    def size(self):
        """
        Returns the number of nodes within the tree.
        @return: number of nodes in the tree.
        """
        return self.num_nodes
    
    def height(self, root):
        """
        Determines the height of the tree. Height is defined as the longest 
        path (in number of edges) from the node to a leaf.
        @param root: The root of the tree.
        @return: The height of the tree.
        """
        if root == None:
            return -1
        else:
            left_subtree_height = self.height(root.left)
            right_subtree_height = self.height(root.right)
            return max(left_subtree_height, right_subtree_height) + 1
    
    def depth(self, root, query):
        """
        Determines the depth of a node. Depth is defined as the number of edges
        from the node to the root.
        @param root: The root of the tree.
        @param query: The data of the node to find the depth of.
        @return: The depth of a node.
        """
        dist = 0
        if root == None and self.num_nodes == 0:
            return 0
        elif root == None:
            return -1
        elif root.data == query:
            return dist
        
        dist = self.depth(root.left, query)
        if dist >= 0:
            return dist + 1
        dist = self.depth(root.right, query)
        if dist >= 0:
            return dist + 1
        return dist
    
    def print_tree_diagram(self, root, space):
        """
        Prints the tree as a diagram.
        @param root: The root of the tree:
        @param space: The number of spaces between each node. Initial value 
        should be zero.
        """
        height = self.height(self.root)

        if root is None:
            return
 
        # Increasing distance between levels.
        space += height
    
        self.print_tree_diagram(root.right, space)
        print()
    
        for i in range(height, space):
            print(' ', end='')

        print(root.data)
        self.print_tree_diagram(root.left, space)
    
    def get_root(self):
        """Returns the root of the tree."""
        return self.root

    def preorder_traversal(self, node):
        """
        Prints the tree. Visits the current node before its child nodes.
        @param node: The node to begin the traversal from.
        """
        if (node != None):
            print(node.data, end=" ")
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)
        return

    def inorder_traversal(self, node):
        """
        Prints the tree. Visits the left node, then the current node, then right
        node.
        @param node: The node to begin the traversal from.
        """
        if (node != None):
            self.inorder_traversal(node.left)
            print(node.data, end=" ")
            self.inorder_traversal(node.right)
        return
    
    def postorder_traversal(self, node):
        """
        Prints the tree. Visits the left node, then the right node, then the
        current node.
        @param node: The node to begin the traversal from.
        """
        if (node != None):
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            print(node.data, end=" ")
        return
    
    def levelorder_traversal(self, node):
        """
        Prints the tree from top to bottom, level by level, left to right.
        Utilizes a modified version of breadth first search.
        @param node: The node to begin the traversal from.
        """
        queue = [node]
        
        while queue:
            curr = queue.pop(0)
            if curr:
                print(curr.data, end=" ")
                if curr:
                    queue.append((curr.left))
                    queue.append((curr.right))

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

Binary Tree:
- A binary tree is a tree in which each node has 0, 1, or 2 children.
- A perfect binary tree is a binary tree where every internal node has exactly 2
children and all leaf nodes are on the same level.
- A complete binary tree is a binary tree in which every level of the tree is 
fully filled, except for perhaps the last level (which must be filled left to
right).
- Binary trees are unordered and allows for duplicate values as opposed to a 
binary search tree.

Binary Search Tree:
- A data structure that maintains order yet also has relatively fast search, 
insertion, and deletion.
- A binary search tree does not allow duplicates.
- A binary search tree is a binary tree in which every nnode fits a specific
ordering property:
    - all left descendants of a node can only contain values that are less than 
    the node itself.
    - all right descendants of a node can only contain values that are greater 
    than the node itself.

Tree Traversals: 
- Pre-order: VLR
- In-order: LVR
- Post-order: LRV
- Level-order: Top to bottom, level by level, left to right
"""