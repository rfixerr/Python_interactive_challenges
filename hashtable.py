'''Implement a hash table with set, get, and remove methods.
    Constraints

    For simplicity, are the keys integers only? Yes
    For collision resolution, can we use chaining? Yes
    Do we have to worry about load factors? No

    Test Cases

    get on an empty hash table index
    set on an empty hash table index
    set on a non empty hash table index
    set on a key that already exists
    remove on a key with an entry
    remove on a key without an entry'''



class Item(object):

    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable(object):

    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]


    def hash_function(self, key):
        return key % self.size


    def set(self, key, value):
        hash_index = self.hash_function(key)
        for item in self.table[hash_index]:
            if item.key == key:
                item.value = value
                return
        self.table[hash_index].append(Item(key, value))


    def get(self, key):
        hash_index = self.hash_function(key)
        for item in self.table[hash_index]:
            if item.key == key:
                return item.value
        return None


    def remove(self, key):
        hash_index = self.hash_function(key)
        for i, item in enumerate(self.table[hash_index]):
            if item.key == key:
                del self.table[hash_index][i]