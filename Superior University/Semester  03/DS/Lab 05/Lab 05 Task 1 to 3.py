#Task 1: Implementing a Custom Hash Table with Collision Handling
import time
import random
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTableChaining:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * self.size

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        if not self.table[index]:
            self.table[index] = Node(key, value)
        else:
            current = self.table[index]
            while current.next:
                if current.key == key:
                    current.value = value
                    return
                current = current.next
            if current.key == key:
                current.value = value
            else:
                current.next = Node(key, value)

    def get(self, key):
        index = self._hash(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def delete(self, key):
        index = self._hash(key)
        current = self.table[index]
        prev = None
        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.table[index] = current.next
                return
            prev = current
            current = current.next

    def display(self):
        for i, bucket in enumerate(self.table):
            print(f"Bucket {i}: ", end="")
            current = bucket
            while current:
                print(f"({current.key}, {current.value}) -> ", end="")
                current = current.next
            print("None")

class HashTableLinearProbing:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * self.size

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        original_index = index
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = (key, value)  
                return
            index = (index + 1) % self.size
            if index == original_index:
                raise Exception("Hash table is full")
        self.table[index] = (key, value)

    def get(self, key):
        index = self._hash(key)
        original_index = index
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.size
            if index == original_index:
                break
        return None

    def delete(self, key):
        index = self._hash(key)
        original_index = index
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = None
                return
            index = (index + 1) % self.size
            if index == original_index:
                break

    def display(self):
        for i, entry in enumerate(self.table):
            print(f"Bucket {i}: {entry}")
num_items = 1000
keys = [random.randint(1, 10000) for _ in range(num_items)]
values = [random.randint(1, 10000) for _ in range(num_items)]
chaining_table = HashTableChaining(size=2000)
start_time = time.time()
for i in range(num_items):
    chaining_table.insert(keys[i], values[i])
chaining_insert_time = time.time() - start_time
start_time = time.time()
for key in keys:
    chaining_table.get(key)
chaining_search_time = time.time() - start_time
linear_table = HashTableLinearProbing(size=2000)
start_time = time.time()
for i in range(num_items):
    linear_table.insert(keys[i], values[i])
linear_insert_time = time.time() - start_time
start_time = time.time()
for key in keys:
    linear_table.get(key)
linear_search_time = time.time() - start_time
print(f"Chaining Insert Time: {chaining_insert_time:.5f} sec")
print(f"Chaining Search Time: {chaining_search_time:.5f} sec")
print(f"Linear Probing Insert Time: {linear_insert_time:.5f} sec")
print(f"Linear Probing Search Time: {linear_search_time:.5f} sec")

#Task 2: Checking if Two Strings Are Anagrams Using Hashing

def are_anagrams(str1, str2):
    if len(str1) != len(str2):
        return False
    char_count = {}
    for char in str1:
        char_count[char] = char_count.get(char, 0) + 1
    for char in str2:
        if char not in char_count:
            return False
        char_count[char] -= 1
        if char_count[char] < 0:
            return False
    return True
print(are_anagrams("listen", "silent")) 
print(are_anagrams("hello", "world"))    
print(are_anagrams("anagram", "nagaram")) 
print(are_anagrams("rat", "car"))  

#Task 03:Implementing a Simple Caching Mechanism Using Hash Maps



from collections import OrderedDict
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()  
    def get(self, key):
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        return None  
    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        elif len(self.cache) >= self.capacity:
            self.cache.popitem(last=False)
        self.cache[key] = value  
    def display(self):
        print("Cache state:", dict(self.cache))
cache = LRUCache(5)
cache.put(1, "A")
cache.put(2, "B")
cache.put(3, "C")
cache.put(4, "D")
cache.put(5, "E")
cache.display()
cache.get(2)  
cache.put(6, "F") 
cache.display()



