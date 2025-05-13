# Task 1: Analyzing Time Complexity of Algorithms 
# Objective: Understand and compare the time complexity of different algorithms. 


import random
import time
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        
        merge_sort(L)
        merge_sort(R)
        
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)
data = [random.randint(0, 10000) for _ in range(1000)]
bubble_data = data.copy()
start = time.time()
bubble_sort(bubble_data)
bubble_time = time.time() - start
merge_data = data.copy()
start = time.time()
merge_sort(merge_data)
merge_time = time.time() - start
quick_data = data.copy()
start = time.time()
quick_sorted = quick_sort(quick_data)
quick_time = time.time() - start
algorithms = ['Bubble Sort', 'Merge Sort', 'Quick Sort']
times = [bubble_time, merge_time, quick_time]
print("\nSorting Algorithms Performance (1000 Integers):\n")
max_length = 50 
max_time = max(times)
for algo, t in zip(algorithms, times):
    bar = '#' * int((t / max_time) * max_length)
    print(f"{algo:15}: {bar} {t:.6f} sec")
print("\nTime Complexity Summary:")
print("Bubble Sort: O(n^2) - Compares each pair multiple times, very slow for large lists.")
print("Merge Sort: O(n log n) - Efficient, divides and merges recursively.")
print("Quick Sort: O(n log n) on average - Fastest generally, though worst-case is O(n^2).")

# Task 2: Recursive vs Iterative Approach 
# Objective: Analyze and compare recursion with iteration in solving problems. 

import time
def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)
def fib_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
memo = {}
def fib_memoized(n):
    if n in memo:
        return memo[n]
    if n <= 1:
        memo[n] = n
    else:
        memo[n] = fib_memoized(n - 1) + fib_memoized(n - 2)
    return memo[n]
test_values = [10, 20, 30, 40]

def measure_time(func, n):
    start = time.time()
    result = func(n)
    end = time.time()
    return result, end - start

print(f"{'n':<5}{'Recursive Time':<20}{'Iterative Time':<20}{'Memoized Time':<20}")
print('-' * 65)

for n in test_values:
    try:
        _, t_rec = measure_time(fib_recursive, n)
    except RecursionError:
        t_rec = float('inf')

    _, t_iter = measure_time(fib_iterative, n)
    _, t_memo = measure_time(fib_memoized, n)

    print(f"{n:<5}{t_rec:<20.6f}{t_iter:<20.6f}{t_memo:<20.6f}")

# Task 3: Visualizing Big-O Notation 
# Objective: Develop an interactive Python program to visualize the growth of different time 
# complexities. 
import math
def constant(n):
    return [1 for _ in n]
def logarithmic(n):
    return [math.log2(i) if i > 0 else 0 for i in n]
def linear(n):
    return n
def linearithmic(n):
    return [i * math.log2(i) if i > 0 else 0 for i in n]
def quadratic(n):
    return [i ** 2 for i in n]
def exponential(n):
    return [2 ** i for i in n]
def plot_graph(x_values, y_values, label, max_length=50):
    print(f"\n{label} - Time Complexity Growth:")
    max_y = max(y_values)
    for x, y in zip(x_values, y_values):
        bar = '#' * int((y / max_y) * max_length)
        print(f"{x:<4}: {bar} ({y:.2f})")
x = list(range(1, 101)) 
y_constant = constant(x)
y_log = logarithmic(x)
y_linear = linear(x)
y_nlogn = linearithmic(x)
y_quad = quadratic(x)
y_exp = exponential(range(1, 20)) 
plot_graph(x, y_constant, "O(1) Constant Time")
plot_graph(x, y_log, "O(log n) Logarithmic Time")
plot_graph(x, y_linear, "O(n) Linear Time")
plot_graph(x, y_nlogn, "O(n log n) Linearithmic Time")
plot_graph(x, y_quad, "O(n²) Quadratic Time")
plot_graph(range(1, 21), y_exp, "O(2^n) Exponential Time")
