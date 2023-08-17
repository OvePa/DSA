# Define a class for a hash table with open addressing
class HashTableOpenAddressing:
    def __init__(self, size):
        self.size = size  # Set the size of the hash table
        self.keys = [None] * size  # Create an array to store keys
        self.values = [None] * size  # Create an array to store values

    # Private method to calculate the hash value of a given key
    def _hash(self, key):
        return hash(key) % self.size

    # Method to insert a key-value pair into the hash table using open addressing
    def insert(self, key, value):
        index = self._hash(key)  # Calculate the index based on the key's hash
        while self.keys[index]:  # Continue probing until an empty slot is found
            index = (index + 1) % self.size
        self.keys[index] = key  # Insert the key at the calculated index
        self.values[index] = value  # Insert the value at the same index

    # Method to retrieve a value associated with a given key from the hash table
    def get(self, key):
        index = self._hash(key)  # Calculate the index based on the key's hash
        while self.keys[index]:
            if self.keys[index] == key:
                return self.values[index]  # Return the value if the key is found
            index = (index + 1) % self.size
        return None  # Return None if the key is not found

    # Method to remove a key-value pair associated with a given key from the hash table
    def remove(self, key):
        index = self._hash(key)  # Calculate the index based on the key's hash
        while self.keys[index]:
            if self.keys[index] == key:
                self.keys[index] = None  # Remove the key from the keys array
                self.values[
                    index
                ] = None  # Remove the corresponding value from the values array
                return
            index = (index + 1) % self.size  # Continue probing to find the key


# This class implements a hash table with open addressing as a collision resolution strategy.
# In open addressing, when a collision occurs, the next available slot is used to store the collided item.

# Note: This hash table implementation uses a simple hash function and linear probing.
