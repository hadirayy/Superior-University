# Task 1: Implementing Depth-First Search (DFS) and Breadth-First Search 
# (BFS) 
# Objective: Understand graph traversal algorithms by implementing DFS and BFS on a 
# given graph.


def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = []
    visited.append(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)
    return visited
def dfs_iterative(graph, start):
    visited = []
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(reversed(graph[node]))

    return visited
from collections import deque

def bfs(graph, start):
    visited = []
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])

    return visited                       
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
print("DFS (Recursive):", dfs_recursive(graph, 'A'))  
print("DFS (Iterative):", dfs_iterative(graph, 'A'))   
print("BFS:", bfs(graph, 'A')) 


# Task 2: Finding the Shortest Path Using Dijkstra’s Algorithm 
# Objective: Learn graph-based shortest path algorithms by implementing Dijkstra’s 
# Algorithm for weighted graphs. 

 


import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    return distances
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

print(dijkstra(graph, 'A'))

# Task 3: Detecting Cycles in a Graph (Directed & Undirected) 
# Objective: Understand cycle detection in graphs by implementing cycle detection for 
# directed and undirected graphs using DFS. 
def detect_cycle_undirected(graph):
    parent = {}

    def find(node):
        if parent[node] != node:
            parent[node] = find(parent[node]) 
        return parent[node]

    def union(u, v):
        root_u, root_v = find(u), find(v)
        if root_u == root_v:
            return False 
        parent[root_u] = root_v
        return True

 
    for node in graph:
        parent[node] = node

    visited_edges = set()
    for u in graph:
        for v in graph[u]:
            if (v, u) in visited_edges:
                continue  
            visited_edges.add((u, v))
            if not union(u, v):
                return True 

    return False 
def detect_cycle_directed(graph):
    visited = set()
    rec_stack = set()

    def dfs(node):
        visited.add(node)
        rec_stack.add(node)

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
            elif neighbor in rec_stack:
                return True  

        rec_stack.remove(node)
        return False

    for node in graph:
        if node not in visited:
            if dfs(node):
                return True

    return False
graph_undirected = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}
print(detect_cycle_undirected(graph_undirected)) 

graph_directed = {
    'A': ['B'],
    'B': ['C'],
    'C': ['A']
}
print(detect_cycle_directed(graph_directed))  

