import heapq

class Heap:
    def __init__(self, heap_type="min"):
        self.heap_type = heap_type
        self.data = []

    def insert(self, value):
        if self.heap_type == "min":
            heapq.heappush(self.data, value)
        else:  
            heapq.heappush(self.data, -value)

    def extract_root(self):
        if not self.data:
            return None
        if self.heap_type == "min":
            return heapq.heappop(self.data)
        else:
            return -heapq.heappop(self.data)

    def peek(self):
        if not self.data:
            return None
        return self.data[0] if self.heap_type == "min" else -self.data[0]

    def heapify(self, array):
        if self.heap_type == "min":
            self.data = array[:]
            heapq.heapify(self.data)
        else:
            self.data = [-x for x in array]
            heapq.heapify(self.data)

min_heap = Heap("min")
min_heap.insert(10)
min_heap.insert(5)
min_heap.insert(20)
min_heap.insert(2)
print(min_heap.extract_root())  

max_heap = Heap("max")
max_heap.insert(10)
max_heap.insert(5)
max_heap.insert(20)
max_heap.insert(2)
print(max_heap.extract_root()) 


# Task 02
#  Implementing a Priority Queue Using a Heap 
# Objective: Learn how priority queues work using a heap. 
# Instructions: 

import heapq
class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.counter = 0 
    def enqueue(self, value, priority):
        heapq.heappush(self.heap, (priority, self.counter, value))
        self.counter += 1
    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from an empty priority queue")
        return heapq.heappop(self.heap)[2]
    def peek(self):
        if self.is_empty():
            raise IndexError("peek from an empty priority queue")
        return self.heap[0][2]
    def is_empty(self):
        return len(self.heap) == 0
pq = PriorityQueue()
pq.enqueue("Task A", 3)
pq.enqueue("Task B", 1)
pq.enqueue("Task C", 2)

print(pq.dequeue())
print(pq.peek())     
print(pq.dequeue())  
print(pq.dequeue())  

#Task 03
# Finding the K Smallest and K Largest Elements Using a Heap 
import heapq
def find_k_smallest(arr, k):
    if k <= 0:
        return []
    return heapq.nsmallest(k, arr)
def find_k_largest(arr, k):
    if k <= 0:
        return []
    return heapq.nlargest(k, arr)
arr = [10, 4, 3, 20, 15, 7]
print("K Smallest:", find_k_smallest(arr, 3))  
print("K Largest:", find_k_largest(arr, 2)) 