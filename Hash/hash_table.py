# Define a class for a simple hash table
class HashTable:
    def __init__(self, size):
        self.size = size  # Set the size of the hash table
        self.data = [None] * size  # Create an array to hold hash table data

    # Private method to calculate the hash value of a given key
    def _hash(self, key):
        hash_value = 0
        for char in key:
            hash_value = (hash_value + ord(char)) % self.size
        return hash_value

    # Method to insert a key-value pair into the hash table
    def insert(self, key, value):
        index = self._hash(key)  # Calculate the index based on the key's hash
        if not self.data[index]:
            self.data[index] = []  # Initialize an empty list if the index is empty
        self.data[index].append((key, value))  # Append the key-value pair to the list

    # Method to retrieve a value associated with a given key from the hash table
    def get(self, key):
        index = self._hash(key)  # Calculate the index based on the key's hash
        if self.data[index]:
            for stored_key, value in self.data[index]:
                if stored_key == key:
                    return value  # Return the value if the key is found
        return None  # Return None if the key is not found

    # Method to remove a key-value pair associated with a given key from the hash table
    def remove(self, key):
        index = self._hash(key)  # Calculate the index based on the key's hash
        if self.data[index]:
            for i, (stored_key, _) in enumerate(self.data[index]):
                if stored_key == key:
                    del self.data[index][i]  # Remove the key-value pair from the list
                    return


# This class implements a simple hash table with basic hash function, insert, get, and remove methods.
# It uses an array to store data, and each index in the array holds a list of key-value pairs.

# Note: This hash table implementation is simplified and may not handle collisions efficiently.


if __name__ == "__main__":
    hash_table = HashTable(10)

    hash_table.insert("apple", 5)
    hash_table.insert("banana", 10)
    hash_table.insert("cherry", 15)

    print(hash_table.get("banana"))  # Output: 10
    print(hash_table.get("orange"))  # Output: None

    hash_table.remove("banana")
    print(hash_table.get("banana"))  # Output: None
