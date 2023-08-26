class HashEntry:
    def __init__(self, key, data):
        # key of the entry
        self.key = key
        # data to be stored
        self.value = data
        # reference to new entry
        self.nxt = None

    def __str__(self):
        return str(entry.key) + ", " + entry.value


class HashTable:
    # Constructor
    def __init__(self):
        # Size of the HashTable
        self.slots = 10
        # Current entries in the table
        # Used while resizing the table when half of the table gets filled
        self.size = 0
        # List of HashEntry objects (by default all None)
        self.bucket = [None] * self.slots

    # Helper Functions

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.get_size() == 0


# Hash Function
def get_index(self, key):
    # hash is a built-in function in Python
    hash_code = hash(key)
    index = hash_code % self.slots
    return index


if __name__ == "__main__":
    entry = HashEntry(3, "Educative")
    print(entry)
    ht = HashTable()
    print(ht.is_empty())
