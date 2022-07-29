"""
A hash map is an implementation of the Map ADT (associative array). 

Map ADT Operations:
1. insert(key, value): Adds the (key, value) pair to the map.
2. find(key): Returns true if key is in the map, otherwise return false.
3. remove(key): Removes the (key, value) pair associated with key.
4. size(): Returns the number of (key, value) pairs currently sotred in the map.
"""

"""
Hash Map Operations:
1. insert(key, value): Adds the (key, value) pair to the hash map.
2. find(key): Returns true if key is in the hash map, otherwise return false.
3. remove(key): Removes the (key, value) pair associated with key.
4. size(): Returns the number of (key, value) pairs currently sotred in the hash 
map.
5. hash_function(key): Returns a hash value for a given key to use to hash map 
to a valid index.
"""

"""
Hash Map Time-Complexity: 
1. find(x): O(1)
2. insert(x): O(1)
3. remove(x): O(1)
4. resize(): 0(n)
"""

class HashMap():
    """
    Implementation of a hash map data structure ignoring the possibility of 
    collisions. 
    Hash Function: Static hashing using the division method.
    Collision Resolution Strategy: None
    """

    def __init__(self, num_slots=11, load_factor=0.75):
        """
        Creates an empty hash map.
        @param num_slots: Number of slots (ideally a prime number) to initialize
        the hash map with.
        @param load_factor: The maximum accepted ratio of entries to slots 
        acceptable until resizing and rehashing into a larger arrary occurs. 
        """
        self.hash_map = num_slots * [None]
        self.num_entries = 0
        self.num_slots = num_slots
        self.load_factor = load_factor

    def insert(self, key, value):
        """
        Inserts a key into the hash map. If the load factor is too high, it
        resizes the array, rehashes the old keys into the new array, and then
        inserts the key into the hash map. 
        @param key: Value used to hash an index to store this value at.
        @param value: value associated with the given key.
        """
        index = self.hash_function(key)
        if self.hash_map[index] == None:
                self.hash_map[index] = (key, value)
                self.num_entries += 1

        if not self.load_factor_in_range():
            # Often a prime number.
            self.resize(2 * len(self.hash_map) - 1)
            
    def find(self, key, value):
        """
        Searches for a key within the hash map.
        @param key: Key to search for within the hash map.
        @param value: value associated with the given key.
        @return: True if the key is in the hash map, false otherwise.
        """
        index = self.hash_function(key)
        return self.hash_map[index] == (key, value)

    def remove(self, key, value):
        """
        Removes a key from the hash map.
        @param key: The key to remove.
        @param value: value associated with the given key.
        """
        index = self.hash_function(key)
        print(index)
        if self.hash_map[index] != value:
            self.hash_map[index] = None
            self.num_entries -= 1

    def hash_function(self, key):
        """
        Computes a hash value for a given give to use to map to a valid index.
        @param key: The key to hash.
        @return: The hashed value to use as the index of the given key.
        """
        return key % self.num_slots

    def resize(self, new_num_slots):
        """
        Resizes the array. Called once is surpassed.
        @param new_num_slots: Size to resize the array to (ideally a prime 
        number).
        """
        old_hash_map = self.hash_map[:]
        self.hash_map = new_num_slots * [None]
        self.num_slots = new_num_slots
        
        for kvp in old_hash_map:
            if kvp != None:
                index = self.hash_function(kvp[0])
                self.hash_map[index] = (kvp[0], kvp[1])

    def load_factor_in_range(self):
        """
        Checks to see if the load factor is within range.
        @return: True is the load factor is within range, false otherwise.
        """
        return (self.num_entries / len(self.hash_map)) < self.load_factor
    
    def size(self):
        """
        Checks to see the number of entries in the hash map.
        @return: Number of entries within the hash map.
        """
        return self.num_entries

    def print_hash_map(self):
        """Prints the hash map."""
        for index, item in enumerate(self.hash_map):
            print(f"hash_map[{index}] = {item}")

"""
Notes:

Hash Map:
- A collection of (key, value) pairs hashed to indices based on their key.
- To compute an index (for searching, removing, or inserting), a hash map uses
a hash function.
- Collisions occur when two keys are hashed to the same index.
- The capacity of the hash map should be a prime number to avoid unequal 
distributions.
    - This avoids the cases where the mod function never certain indices.

Minimizing Collisions:
1. Maintain a low load factor (# entries/# slots).
    - If the load factor approaches .75 (general rule of thumb), consider 
    resizing the array and rehashing the the elements from the old array into 
    the newly resized array (O(n)).
2. Have a good hash function.

Good Hash Function Characteristics:
1. Minimizes the number of times two different keys are hashed to the same 
index (idealistically to zero).
2. Distributes values evenly.
3. Considers the size of the data structure to hash the key to a valid index.

Hash Function Requirements:
1. It must hash the same key to the same index every time it is called.

Efficient Hash Maps Consider:
1. Amount of data being stored.
2. Number of empty cells.
3. Which hash function(s) to use.
4. Which collision resolution strategy to use.
"""