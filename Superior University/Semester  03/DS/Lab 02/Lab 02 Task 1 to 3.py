#Task #01


#: Implementing Custom Array Operations
#Objective: Develop an understanding of array manipulation techniques.



class DynamicArray:
    def __init__(self, initial_capacity=10):
        self.capacity = initial_capacity
        self.size = 0
        self.data = [None] * self.capacity
    
    def __len__(self):
        return self.size
    
    def __getitem__(self, index):
        
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        return self.data[index]
    
    def __setitem__(self, index, value):
        
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        self.data[index] = value
    
    def __str__(self):
    
        return str(self.data[:self.size])
    
    def _resize(self, new_capacity):
        
        new_data = [None] * new_capacity
        for i in range(self.size):
            new_data[i] = self.data[i]
        self.data = new_data
        self.capacity = new_capacity
    
    def append(self, value):
        if self.size == self.capacity:
            self._resize(2 * self.capacity)  
        self.data[self.size] = value
        self.size += 1
    
    def insert(self, index, value):
    
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        
        if self.size == self.capacity:
            self._resize(2 * self.capacity)
        
        
        for i in range(self.size, index, -1):
            self.data[i] = self.data[i-1]
        
        self.data[index] = value
        self.size += 1
    
    def remove(self, index):

        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        
        value = self.data[index]
        
    
        for i in range(index, self.size - 1):
            self.data[i] = self.data[i+1]
        
        self.size -= 1
        
        
        if self.size < self.capacity // 4 and self.capacity > 10:
            self._resize(self.capacity // 2)
        
        return value
    
    def search(self, value):
        for i in range(self.size):
            if self.data[i] == value:
                return i
        return -1
    
    def get_capacity(self):
    
        return self.capacity

def test_dynamic_array():
    print("Testing Dynamic Array Implementation")
    print("=" * 40)
    
    
    arr = DynamicArray(5)
    print(f"Initial array: {arr}")
    print(f"Size: {len(arr)}, Capacity: {arr.get_capacity()}")
    
    
    print("\nAppending elements:")
    for i in range(1, 6):
        arr.append(i * 10)
    print(f"After appending 5 elements: {arr}")
    print(f"Size: {len(arr)}, Capacity: {arr.get_capacity()}")
    
    
    arr.append(60)
    print("\nAppending one more to trigger resize:")
    print(f"Array: {arr}")
    print(f"Size: {len(arr)}, Capacity: {arr.get_capacity()}")
    
    
    print("\nInserting elements:")
    arr.insert(2, 25)
    print(f"After inserting 25 at index 2: {arr}")
    arr.insert(0, 5)
    print(f"After inserting 5 at index 0: {arr}")
    print(f"Size: {len(arr)}, Capacity: {arr.get_capacity()}")
    
    
    print("\nSearching elements:")
    print(f"Index of 25: {arr.search(25)}")
    print(f"Index of 100: {arr.search(100)}")
    

    print("\nRemoving elements:")
    removed = arr.remove(3)
    print(f"Removed element at index 3: {removed}")
    print(f"Array after removal: {arr}")
    print(f"Size: {len(arr)}, Capacity: {arr.get_capacity()}")
    

    print("\nRemoving elements to trigger shrink:")
    for _ in range(4):
        arr.remove(0)
    print(f"Array after removals: {arr}")
    print(f"Size: {len(arr)}, Capacity: {arr.get_capacity()}")
    
    
    print("\nTesting index access:")
    print(f"Element at index 1: {arr[1]}")
    try:
        print(arr[10])
    except IndexError as e:
        print(f"Error: {e}")
    
    print("\nAll tests completed!")


if __name__ == "__main__":
    test_dynamic_array()



#Task #02
# : Finding the Longest Substring Without Repeating Characters
# Objective: Solve a real-world string manipulation problem efficiently.



def longest_substring_bruteforce(s):
    max_length = 0
    max_substring = ""
    
    for i in range(len(s)):
        seen = set()
        current_sub = ""
        for j in range(i, len(s)):
            if s[j] not in seen:
                seen.add(s[j])
                current_sub += s[j]
                if len(current_sub) > max_length:
                    max_length = len(current_sub)
                    max_substring = current_sub
            else:
                break
                
    return max_substring, max_length
def longest_substring_sliding_window(s):

    char_index = {}
    max_length = 0
    max_substring = ""
    left = 0
    
    for right, char in enumerate(s):
        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1
        
        char_index[char] = right
        
        current_length = right - left + 1
        if current_length > max_length:
            max_length = current_length
            max_substring = s[left:right+1]
    
    return max_substring, max_length
import time

def compare_performance(s):
    print(f"\nTesting string: '{s}'")
    
    
    start = time.time()
    result_bf = longest_substring_bruteforce(s)
    time_bf = time.time() - start
    
    start = time.time()
    result_sw = longest_substring_sliding_window(s)
    time_sw = time.time() - start    
    print(f"Brute Force:   Substring '{result_bf[0]}', Length {result_bf[1]}, Time {time_bf:.6f}s")
    print(f"Sliding Window: Substring '{result_sw[0]}', Length {result_sw[1]}, Time {time_sw:.6f}s")
    return time_bf, time_sw
test_cases = [
    "abcabcbb",  
    "bbbbb",     
    "pwwkew",    
    "",          
    "abcdef",    
    "aab",       
    "dvdf",      
    "abcdeafbdgcbb"  
]
bf_times = []
sw_times = []
for test_str in test_cases:
    bf, sw = compare_performance(test_str)
    bf_times.append(bf)
    sw_times.append(sw)
print("\nPerformance Summary:")
print(f"Average Brute Force Time:   {sum(bf_times)/len(bf_times):.6f}s")
print(f"Average Sliding Window Time: {sum(sw_times)/len(sw_times):.6f}s")
print(f"Sliding Window is {sum(bf_times)/sum(sw_times):.1f}x faster on average")





# Task 3: Two-Dimensional Array – Image Rotation 
# Objective: Apply matrix transformations to manipulate 2D arrays.





def rotate_matrix_90_clockwise(matrix):
    n = len(matrix)
    
    
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    for i in range(n):
        matrix[i] = matrix[i][::-1]
    
    return matrix

def print_matrix(matrix):

    for row in matrix:
        print(row)
    print()


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Original Matrix:")
print_matrix(matrix)

rotated = rotate_matrix_90_clockwise(matrix)

print("Matrix after 90° clockwise rotation:")
print_matrix(rotated)
















