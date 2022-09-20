"""
An implenetation of the Graph ADT using an adjacency list.

Some Graph ADT Operations:
- The basic operations provided by a graph data structure G usually include:
1. is_adjacent(G, x, y): Returns true if there is an edge from the vertex x to 
the vertex y.
2. neighbors(G, x): Returns a list of all vertices y such that there is an edge 
from the vertex x to the vertex y.
3. add_vertex(G, x): Adds the vertex x, if it is not there already.
4. remove_vertex(G, x): Removes the vertex x, if it exists.
5. add_edge(G, x, y, z): Adds the edge z from the vertex x to the vertex y, if there is not one already.
6. remove_edge(G, x, y): Removes the edge from the vertex x to the vertex y, if one exists.
7. get_vertex_value(G, x): Returns the value associated with the vertex x.
8. set_vertex_value(G, x, v): Sets the value associated with the vertex x to v.

Structures that associate values to the edges usually also provide:
9. get_edge_value(G, x, y): returns the value associated with the edge (x, y).
10. set_edge_value(G, x, y, v): sets the value associated with the edge (x, y) to v.
"""

"""
Space Complexity: O(|V| + |E|)
    - We must allocate one slot for each of our |V| vertices, and we place each 
    of our |E| edges in their corresponding slots.
"""

class Vertex:
    """Implementation of a class to create vertices."""

    def __init__(self, data=None):
        """Create a vertex."""
        self.data = data
        self.adj_vertices = []

class UnweightedUndirectedAdjacenyList():
    """Implementation of an adjancey list."""

    def __init__(self):
        """Create an empty adjaceny list."""
        self.vertices = []
    
    def size(self):
        return len(self.vertices)
    
    def is_adjacent(self, vertex1, vertex2):
        """
        Returns true if there is an edge from the vertex1 to the vertex2.
        @param vertex1: Vertex to check if adjacent to vertex2.
        @param vertex2: Vertex being checked for adjacency to vertex1.
        """

        if vertex2 in vertex1.adj_vertices:
            return True

    def neighbors(self, vertex_value):
        """
        Returns a list of all adjacent vertices for a given vertex.
        @param vertex_value: Vertex to check adjacent vertices for.
        """

        for vertex in self.vertices:
            if vertex.data == vertex_value:
                return vertex.adj_vertices

    def add_vertex(self, vertex_value):
        """
        Add a vertex to the graph, if a vertex with the same value doesn't 
        already exist.
        @param vertex_value: The value of the vertex to add to the graph.
        """
        
        vertex_exists = False

        for vertex in self.vertices:
            if vertex.data == vertex_value:
                vertex_exists = True

        if not vertex_exists:
            new_vertex = Vertex()
            new_vertex.data = vertex_value
            self.vertices.append(new_vertex)

    def remove_vertex(self, vertex_value):
        """
        Removes a vertex to the graph, if a vertex with the same value exists.
        @param vertex_value: The value of the vertex to remove from the graph.
        """

        for vertex in self.vertices:
            if vertex.data == vertex_value:
                # Deleting vertex from being in any node's adj_vertices list.
                for adj_vertex in self.vertices:
                    if vertex_value in adj_vertex.adj_vertices:
                        adj_vertex.adj_vertices.remove(vertex_value)
                self.vertices.remove(vertex)
    
    def add_edge(self, vertex1_value, vertex2_value):
        """
        Adds edge from the vertex1 to the vertex2, if there is not one already.
        @param vertex1: One of the vertices to add the edge between.
        @param vetex2: The other vertex to add the edge between.
        """
        vertex1_exists = False
        vertex2_exists = False
        edge_exists = False
        vertex1 = None
        vertex2 = None

        # Ensuring both vertices exists in the graph and no edge already exists.
        for vertex in self.vertices:
            # If vertex1 exists.
            if vertex.data == vertex1_value:
                vertex1 = vertex
                vertex1_exists = True
                # Checking if an edge from vertex1 to vertex2 exists.
                for adj_vertex in vertex.adj_vertices:
                    if adj_vertex == vertex2_value:
                        edge_exists = True
            elif vertex.data == vertex2_value:
                vertex2 = vertex
                vertex2_exists = True
                for adj_vertex in vertex.adj_vertices:
                    if adj_vertex == vertex1_value:
                        edge_exists = True
        if not vertex1_exists or not vertex2_exists or edge_exists:
            return
        
        # Adding edge.
        for vertex in self.vertices:
            if vertex.data == vertex1_value:
                vertex.adj_vertices.append(vertex2_value)
            elif vertex.data == vertex2_value:
                vertex.adj_vertices.append(vertex1_value)
        
    def remove_edge(self, vertex1_value, vertex2_value):
        """
        Removes edge from the vertex1 to the vertex2, if one exists.
        @param vertex1: One of the vertices to remove the edge between.
        @param vetex2: The other vertex to remove the edge between.
        """
        # Removing edge.
        for vertex in self.vertices:
            if vertex.data == vertex1_value:
                vertex.adj_vertices.remove(vertex2_value)
            elif vertex.data == vertex2_value:
                vertex.adj_vertices.remove(vertex1_value)

"""
Notes:

- A graph consists of vertices and edges.

General Graph Terminology:
- Edges: Connections between vertices.
- Spare graphs: Those for which |E| is much less than |V|^2.
- Dense graphs: Those for which |E| is close to |V|^2.
- Undirected graph: A graph in which each edge has no particular direction.
- Directed graph: A graph in which each edge has a direction associated with it.
- Weighted graph: A graph in which each edge has a weight associated with it.
- Unweighted graph: A graph in which each edge has no weight associated with it.
- Adjaceny lists: every vertex stores a list of adjacent vertices. THe most
common way to represent a graph. Are a compact way to represent sparse graphs.
- Adjacency matrix: A two-dimensional matrix, in which the rows represent source 
vertices and columns represent destination vertices. Data on edges and vertices 
must be stored externally. Only the cost for one edge can be stored between each 
pair of vertices.
"""