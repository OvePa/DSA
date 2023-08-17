# Define a class for a hash table with chaining
class HashTableChaining:
    def __init__(self, size):
        self.size = size  # Set the size of the hash table
        self.data = [
            [] for _ in range(size)
        ]  # Create a list of empty lists for chaining

    # Private method to calculate the hash value of a given key
    def _hash(self, key):
        return hash(key) % self.size

    # Method to insert a key-value pair into the hash table
    def insert(self, key, value):
        index = self._hash(key)  # Calculate the index based on the key's hash
        self.data[index].append((key, value))  # Append the key-value pair to the list

    # Method to retrieve a value associated with a given key from the hash table
    def get(self, key):
        index = self._hash(key)  # Calculate the index based on the key's hash
        for stored_key, value in self.data[index]:
            if stored_key == key:
                return value  # Return the value if the key is found
        return None  # Return None if the key is not found

    # Method to remove a key-value pair associated with a given key from the hash table
    def remove(self, key):
        index = self._hash(key)  # Calculate the index based on the key's hash
        # Use list comprehension to filter out the key-value pair with the specified key
        self.data[index] = [
            (stored_key, value)
            for stored_key, value in self.data[index]
            if stored_key != key
        ]


# This class implements a hash table with chaining, where each index in the array holds a list of key-value pairs.
# Chaining is used to handle hash collisions by allowing multiple key-value pairs to be stored at the same index.

# Note: This hash table implementation uses a simple hash function and is for educational purposes.
