#Task 01
#  Implementing and Analyzing Sorting Algorithms 
# Objective: Understand and implement different sorting algorithms and analyze their time 
# complexity. 


import time
import random
def bubble_sort(arr):
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
def selection_sort(arr):
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
def insertion_sort(arr):
    arr = arr.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
def measure_time(sort_fn, arr):
    start = time.time()
    sort_fn(arr)
    end = time.time()
    return end - start

def compare_algorithms():
    sizes = [100, 200, 400]
    print(f"{'Size':<10}{'Bubble Sort':<20}{'Selection Sort':<20}{'Insertion Sort'}")

    for size in sizes:
        arr = [random.randint(0, 1000) for _ in range(size)]

        t1 = measure_time(bubble_sort, arr)
        t2 = measure_time(selection_sort, arr)
        t3 = measure_time(insertion_sort, arr)

        print(f"{size:<10}{t1:<20.6f}{t2:<20.6f}{t3:.6f}")

compare_algorithms()

#Task 02
# : Implementing Quick Sort and Merge Sort with Performance 
# Comparison 
# Objective: Learn Quick Sort and Merge Sort and compare their efficiency.
import time
import random
def quick_sort(arr):
    arr = arr.copy()
    def _quick_sort(arr, low, high):
        if low < high:
            pivot_index = partition(arr, low, high)
            _quick_sort(arr, low, pivot_index - 1)
            _quick_sort(arr, pivot_index + 1, high)
    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
    _quick_sort(arr, 0, len(arr) - 1)
    return arr
def merge_sort(arr):
    arr = arr.copy()
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)
def merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged
def measure_time(sort_fn, arr):
    start = time.time()
    sort_fn(arr)
    return time.time() - start

def compare_quick_merge():
    sizes = [1000, 5000, 10000]
    print(f"{'Size':<10}{'Quick Sort (s)':<20}{'Merge Sort (s)'}")

    for size in sizes:
        arr = [random.randint(0, 100000) for _ in range(size)]
        t_quick = measure_time(quick_sort, arr)
        t_merge = measure_time(merge_sort, arr)
        print(f"{size:<10}{t_quick:<20.6f}{t_merge:.6f}")

compare_quick_merge()
arr = [38,27,43,3,9,82,10]
print("Quick Sort:", quick_sort(arr))  
print("Merge Sort:", merge_sort(arr)) 
#Task 03
# : Implementing Heap Sort and Counting Sort for Large Datasets 
# Objective: Learn and apply Heap Sort and Counting Sort for sorting large datasets 
# efficiently.
# Heap Sort using Max-Heap
def heap_sort(arr):
    arr = arr.copy()
    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        
        if left < n and arr[left] > arr[largest]:
            largest = left
        
        if right < n and arr[right] > arr[largest]:
            largest = right
        
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr
def counting_sort(arr):
    arr = arr.copy()
    max_val = max(arr)
    min_val = min(arr)
    range_of_elements = max_val - min_val + 1
    count = [0] * range_of_elements
    output = [0] * len(arr)

    for num in arr:
        count[num - min_val] += 1
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    for num in reversed(arr):
        output[count[num - min_val] - 1] = num
        count[num - min_val] -= 1
    
    return output
import time
import random
def measure_time(sort_fn, arr):
    start = time.time()
    sort_fn(arr)
    return time.time() - start

def compare_heap_counting():
    sizes = [1000, 5000, 10000]
    print(f"{'Size':<10}{'Heap Sort (s)':<20}{'Counting Sort (s)'}")

    for size in sizes:
        arr = [random.randint(0, 1000) for _ in range(size)]
        t_heap = measure_time(heap_sort, arr)
        t_counting = measure_time(counting_sort, arr)
        print(f"{size:<10}{t_heap:<20.6f}{t_counting:.6f}")

compare_heap_counting()
arr = [4, 10, 3, 5, 1]
print("Heap Sort:", heap_sort(arr))  
arr2 = [1, 4, 1, 2, 7, 5, 2]
print("Counting Sort:", counting_sort(arr2)) 

