#Task 01
#  Implementing Activity Selection Algorithm 
# Objective: Learn how Greedy Algorithms optimize decision-making by implementing the 
# Activity Selection Problem to maximize the number of non-overlapping activities. 

def activity_selection(activities):
    activities.sort(key=lambda x: x[1])
    selected_activities = []
    last_end_time = 0
    for start, end in activities:
        if start >= last_end_time:
            selected_activities.append((start, end))
            last_end_time = end 
    return selected_activities
activities = [(1, 3), (2, 5), (3, 9), (6, 8), (8, 11)]
print(activity_selection(activities))

#Task 02
# : Implementing Huffman Coding for Data Compression 
# Objective: Understand Greedy Algorithms in data compression by implementing 
# Huffman Encoding, which minimizes the average code length for characters based on 
# frequency


import heapq
from collections import defaultdict, Counter
class Node:
    def __init__(self, char=None, freq=0):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    def __lt__(self, other):
        return self.freq < other.freq
def build_huffman_tree(freq_map):
    heap = [Node(char, freq) for char, freq in freq_map.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        merged = Node(freq=node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2
        heapq.heappush(heap, merged)

    return heap[0] 

def generate_codes(node, current_code="", code_map={}):
    if node is None:
        return

    if node.char is not None:
        code_map[node.char] = current_code

    generate_codes(node.left, current_code + "0", code_map)
    generate_codes(node.right, current_code + "1", code_map)

    return code_map

def huffman_encoding(input_string):
    if not input_string:
        return "", {}, 0, 0
    freq_map = Counter(input_string)
    root = build_huffman_tree(freq_map)
    code_map = generate_codes(root)
    encoded_string = ''.join(code_map[char] for char in input_string)

    original_length = len(input_string) * 8  
    compressed_length = len(encoded_string)
    return encoded_string, code_map, original_length, compressed_length
input_str = "huffman coding example"
encoded, codes, orig_len, comp_len = huffman_encoding(input_str)

print("Original String:", input_str)
print("Huffman Codes:", codes)
print("Encoded String:", encoded)
print("Original Length (bits):", orig_len)
print("Compressed Length (bits):", comp_len)
print("Compression Ratio:", round(comp_len / orig_len, 2))


#Task 03
# Disjoint Set Union (Union-Find) with path compression
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n + 1)) 
        self.rank = [0] * (n + 1)
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x]) 
        return self.parent[x]
    def union(self, x, y):
        rootX, rootY = self.find(x), self.find(y)
        if rootX == rootY:
            return False  
        if self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        elif self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1
        return True
def kruskal(edges, num_nodes):
    edges.sort(key=lambda x: x[2])
    uf = UnionFind(num_nodes)
    mst = []
    total_weight = 0
    for u, v, weight in edges:
        if uf.union(u, v):
            mst.append((u, v, weight))
            total_weight += weight
    return mst, total_weight
edges = [(1, 2, 4), (2, 3, 1), (1, 3, 3), (3, 4, 2)]
mst, weight = kruskal(edges, 4)
print("MST:", mst)
print("Total Weight:", weight)