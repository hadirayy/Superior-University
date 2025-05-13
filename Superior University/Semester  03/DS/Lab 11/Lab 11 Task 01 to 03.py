#Task 01
# 1: Implementing a Simple Hash Table with Collision Handling 
# Objective: Understand hashing and implement a hash table using Python with collision 
# handling techniques.

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTableChaining:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        idx = self._hash(key)
        head = self.table[idx]
        curr = head
        while curr:
            if curr.key == key:
                curr.value = value
                return
            curr = curr.next
        new_node = Node(key, value)
        new_node.next = head
        self.table[idx] = new_node

    def get(self, key):
        idx = self._hash(key)
        curr = self.table[idx]
        while curr:
            if curr.key == key:
                return curr.value
            curr = curr.next
        return None

    def delete(self, key):
        idx = self._hash(key)
        curr = self.table[idx]
        prev = None
        while curr:
            if curr.key == key:
                if prev:
                    prev.next = curr.next
                else:
                    self.table[idx] = curr.next
                return
            prev = curr
            curr = curr.next
class HashTableLinearProbing:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        idx = self._hash(key)
        original_idx = idx
        while self.table[idx] is not None:
            if self.table[idx][0] == key:
                self.table[idx] = (key, value)
                return
            idx = (idx + 1) % self.size
            if idx == original_idx:
                raise Exception("Hash table is full")
        self.table[idx] = (key, value)

    def get(self, key):
        idx = self._hash(key)
        original_idx = idx
        while self.table[idx] is not None:
            if self.table[idx][0] == key:
                return self.table[idx][1]
            idx = (idx + 1) % self.size
            if idx == original_idx:
                break
        return None

    def delete(self, key):
        idx = self._hash(key)
        original_idx = idx
        while self.table[idx] is not None:
            if self.table[idx][0] == key:
                self.table[idx] = None
                return
            idx = (idx + 1) % self.size
            if idx == original_idx:
                break
ht = HashTableChaining(10)


ht.insert("name", "Alice")
ht.insert("age", 25)
print(ht.get("name"))  
ht.delete("age")
print(ht.get("age"))   
#Task 02
# : Implementing a Custom Hash Function and Analyzing Collisions 
# Objective: Design a custom hash function and analyze its effectiveness in minimizing 
# collisions.

import random
import string
def custom_hash(key, size):
    return sum(ord(c) for c in str(key)) % size
def builtin_hash(key, size):
    return hash(key) % size
def generate_keys(n, key_length=6):
    keys = set()
    while len(keys) < n:
        keys.add(''.join(random.choices(string.ascii_lowercase, k=key_length)))
    return list(keys)
def count_collisions(keys, hash_func, size):
    table = [0] * size
    for key in keys:
        idx = hash_func(key, size)
        table[idx] += 1
    collisions = sum(1 for count in table if count > 1)
    return collisions, table
def print_histogram(table, title):
    print(f"\n{title}")
    for i, count in enumerate(table):
        bar = '#' * count
        print(f"Index {i:2}: {bar} ({count})")
def test_hash_functions():
    table_size = 20
    num_keys = 200
    keys = generate_keys(num_keys)
    custom_collisions, custom_table = count_collisions(keys, custom_hash, table_size)
    print(f"Custom Hash Collisions: {custom_collisions}")
    print_histogram(custom_table, "Custom Hash Table Distribution")
    builtin_collisions, builtin_table = count_collisions(keys, builtin_hash, table_size)
    print(f"\nBuilt-in Hash Collisions: {builtin_collisions}")
    print_histogram(builtin_table, "Built-in Hash Table Distribution")
test_hash_functions()

#Task 03

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}  
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
    def _remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
    def _add_to_front(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add_to_front(node)
            return node.value
        return -1

    def put(self, key, value):
        if key in self.cache:
            self._remove(self.cache[key])
        elif len(self.cache) >= self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]

        new_node = Node(key, value)
        self._add_to_front(new_node)
        self.cache[key] = new_node
cache = LRUCache(2)
cache.put(1, "A")
cache.put(2, "B")
print(cache.get(1))  
cache.put(3, "C")    
print(cache.get(2))  
print(cache.get(3))

