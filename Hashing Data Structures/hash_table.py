"""
A hash table is an implementation of the Set ADT.
1. find(x): Return true if x exists in the set, false otherwise.
2. insert(x): Adds x to the set.
3. remove(x): Removes x from the set.
"""

"""
Hash Table Operations:
1. insert(key): Inserts a key into the hash table.
2. find(key): Searches for a key within the hash table.
3. remove(key): Removes a key from the hash table.
4. hash_function(key): Returns a hash value for a given key to use to map to a
valid index.
"""

"""
Hash Table Time-Complexity: 
1. find(x): O(1)
2. insert(x): O(1)
3. remove(x): O(1)
4. resize(): 0(n)
"""

class HashTable():
    """
    Implementation of a hash table data structure ignoring the possibility of 
    collisions. 
    Hash Function: Static hashing using the division method.
    Collision Resolution Strategy: None
    """

    def __init__(self, num_slots=11, load_factor=0.75):
        """
        Creates an empty hash table.
        @param num_slots: Number of slots (ideally a prime number) to initialize
        the hash table with.
        @param load_factor: The maximum accepted ratio of entries to slots 
        acceptable until resizing and rehashing into a larger arrary occurs. 
        """
        self.hash_table = num_slots * [None]
        self.num_entries = 0
        self.num_slots = num_slots
        self.load_factor = load_factor

    def insert(self, key):
        """
        Inserts a key into the hash table. If the load factor is too high, it
        resizes the array, rehashes the old keys into the new array, and then
        inserts the key into the hash table. 
        @param key: Value used to hash an index to store this value at.
        """
        index = self.hash_function(key)
        if self.hash_table[index] == None:
                self.hash_table[index] = key
                self.num_entries += 1

        if not self.load_factor_in_range():
            # Often a prime number.
            self.resize(2 * len(self.hash_table) - 1)

    def find(self, key):
        """
        Searches for a key within the hash table.
        @param key: Key to search for within the hash table.
        @return: True if the key is in the hash table, false otherwise.
        """
        index = self.hash_function(key)
        return self.hash_table[index] == key


    def remove(self, key):
        """
        Removes a key from the hash table.
        @key: The key to remove.
        """
        index = self.hash_function(key)
        
        if self.hash_table[index] == key:
            self.hash_table[index] = None
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
        old_hash_table = self.hash_table[:]
        self.hash_table = new_num_slots * [None]
        self.num_slots = new_num_slots

        for key in old_hash_table:
            if key != None:
                index = self.hash_function(key)
                self.hash_table[index] = key
    
    def load_factor_in_range(self):
        """
        Checks to see if the load factor is within range.
        @return: True is the load factor is within range, false otherwise.
        """
        return (self.num_entries / len(self.hash_table)) < self.load_factor
    
    def print_hash_table(self):
        """Prints the hash table."""
        for index, item in enumerate(self.hash_table):
            print(f"hash_table[{index}] = {item}")

"""
Notes:

Hash Table:
- A collection of keys hashed to indices.
- To compute an index (for searching, removing, or inserting), a hash table uses
a hash function.
- Collisions occur when two keys are hashed to the same index.
- The capacity of the hash table should be a prime number to avoid unequal 
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

Efficient Hash Tables Consider:
1. Amount of data being stored.
2. Number of empty cells.
3. Which hash function(s) to use.
4. Which collision resolution strategy to use.
"""