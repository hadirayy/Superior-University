#Task 01
#  Implementing Linear Search and Binary Search 
# Objective: Understand and compare Linear Search and Binary Search by implementing 
# them in Python. 

# Linear Search Implementation
def linear_search(arr, target):
    for i, element in enumerate(arr):
        if element == target:
            return i  
    return -1  

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid 
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1 
import time
import random
def measure_time(search_fn, arr, target):
    start = time.time()
    search_fn(arr, target)
    return time.time() - start

def compare_search_algorithms():
    sizes = [1000, 5000, 10000]
    print(f"{'Size':<10}{'Linear Search (s)':<20}{'Binary Search (s)'}")
    for size in sizes:
        arr_linear = [random.randint(1, 100000) for _ in range(size)]
        arr_binary = sorted(arr_linear)
        target = random.choice(arr_linear)  
        t_linear = measure_time(linear_search, arr_linear, target)
        t_binary = measure_time(binary_search, arr_binary, target)
        print(f"{size:<10}{t_linear:<20.6f}{t_binary:.6f}")
compare_search_algorithms()
arr = [10, 23, 45, 70, 11, 15]
print("Linear Search:", linear_search(arr, 45))  

sorted_arr = [10, 15, 23, 45, 70]
print("Binary Search:", binary_search(sorted_arr, 45))  

#Task 02
#  Implementing Interpolation Search and Jump Search 
# Objective: Learn advanced searching techniques like Interpolation Search and Jump 
# Search for improved efficiency. 
import math

def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0

    while prev < n and arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i
    return -1
def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high and target >= arr[low] and target <= arr[high]:
        if arr[high] == arr[low]:
            if arr[low] == target:
                return low
            else:
                return -1
        pos = low + ((high - low) * (target - arr[low]) // (arr[high] - arr[low]))
        if pos >= len(arr):
            return -1
        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    return -1
arr = [1, 3, 5, 7, 9, 11, 13, 15]
print("Jump Search:", jump_search(arr, 7))            
print("Interpolation Search:", interpolation_search(arr, 7))  
import time
import random

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def measure_time(fn, arr, target):
    start = time.time()
    fn(arr, target)
    return time.time() - start

def compare_search_methods():
    sizes = [1000, 5000, 10000]
    print(f"{'Size':<8}{'Binary Search':<18}{'Jump Search':<18}{'Interpolation Search'}")
    
    for size in sizes:
        arr = sorted(random.sample(range(size * 10), size)) 
        target = random.choice(arr)

        t_bin = measure_time(binary_search, arr, target)
        t_jump = measure_time(jump_search, arr, target)
        t_interp = measure_time(interpolation_search, arr, target)

        print(f"{size:<8}{t_bin:<18.6f}{t_jump:<18.6f}{t_interp:.6f}")

compare_search_methods()


#Task 03

def binary_search(arr, left, right, target):
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def exponential_search(arr, target):
    if arr[0] == target:
        return 0

    i = 1
    while i < len(arr) and arr[i] <= target:
        i *= 2

    return binary_search(arr, i // 2, min(i, len(arr) - 1), target)
def fibonacci_search(arr, target):
    n = len(arr)
    fibMMm2 = 0 
    fibMMm1 = 1  
    fibM = fibMMm2 + fibMMm1  

    while fibM < n:
        fibMMm2 = fibMMm1
        fibMMm1 = fibM
        fibM = fibMMm2 + fibMMm1

    offset = -1

    while fibM > 1:
        i = min(offset + fibMMm2, n - 1)

        if arr[i] < target:
            fibM = fibMMm1
            fibMMm1 = fibMMm2
            fibMMm2 = fibM - fibMMm1
            offset = i
        elif arr[i] > target:
            fibM = fibMMm2
            fibMMm1 -= fibMMm2
            fibMMm2 = fibM - fibMMm1
        else:
            return i

    if fibMMm1 and offset + 1 < n and arr[offset + 1] == target:
        return offset + 1

    return -1
arr = [2, 4, 8, 16, 32, 64, 128]
print("Exponential Search:", exponential_search(arr, 32))  
print("Fibonacci Search:", fibonacci_search(arr, 32))      
import time
import random

def measure_time(fn, arr, target):
    start = time.time()
    fn(arr, target)
    return time.time() - start

def compare_searches():
    sizes = [1000, 5000, 10000]
    print(f"{'Size':<10}{'Binary':<12}{'Exponential':<15}{'Fibonacci':<12}")

    for size in sizes:
        arr = sorted(random.sample(range(size * 10), size))
        target = random.choice(arr)

        t_bin = measure_time(lambda a, t: binary_search(a, 0, len(a) - 1, t), arr, target)
        t_exp = measure_time(exponential_search, arr, target)
        t_fib = measure_time(fibonacci_search, arr, target)

        print(f"{size:<10}{t_bin:<12.6f}{t_exp:<15.6f}{t_fib:.6f}")

compare_searches()
