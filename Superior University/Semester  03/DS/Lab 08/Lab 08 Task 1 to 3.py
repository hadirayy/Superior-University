#Task 01
#  Implementing a Graph Using Adjacency List & Adjacency Matrix 
# Objective: Learn how to represent graphs using adjacency lists and adjacency matrices in 
# Python. 
class Graph:
    def __init__(self, num_vertices, directed=False):
        self.num_vertices = num_vertices
        self.directed = directed
        self.adj_list = {i: [] for i in range(num_vertices)}
        self.adj_matrix = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]

    def add_edge(self, v1, v2):
        self.adj_list[v1].append(v2)
        self.adj_matrix[v1][v2] = 1
        if not self.directed:
            self.adj_list[v2].append(v1)
            self.adj_matrix[v2][v1] = 1

    def remove_edge(self, v1, v2):
        if v2 in self.adj_list[v1]:
            self.adj_list[v1].remove(v2)
        self.adj_matrix[v1][v2] = 0

        if not self.directed:
            if v1 in self.adj_list[v2]:
                self.adj_list[v2].remove(v1)
            self.adj_matrix[v2][v1] = 0

    def display(self):
        print("Adjacency List:")
        for key in self.adj_list:
            print(f"{key}: {self.adj_list[key]}")

        print("\nAdjacency Matrix:")
        for row in self.adj_matrix:
            print(row)
g = Graph(5, directed=False)

g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)

g.display()


#Task 02
# : Implementing Breadth-First Search (BFS) and Depth-First Search 
# (DFS) 
# Objective: Understand and implement graph traversal using BFS and DFS.

from collections import deque

class Graph:
    def __init__(self, num_vertices, directed=False):
        self.num_vertices = num_vertices
        self.directed = directed
        self.adj_list = self.adj_list = {}
        for i in range(num_vertices):
          self.adj_list[i] = []

    def add_edge(self, v1, v2):
        self.adj_list[v1].append(v2)
        if not self.directed:
            self.adj_list[v2].append(v1)

    def bfs(self, start):
        visited = [False] * self.num_vertices
        queue = deque([start])
        visited[start] = True
        traversal = []

        while queue:
            vertex = queue.popleft()
            traversal.append(vertex)

            for neighbor in self.adj_list[vertex]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

        return traversal

    def dfs(self, start):
        visited = [False] * self.num_vertices
        traversal = []

        def dfs_recursive(v):
            visited[v] = True
            traversal.append(v)
            for neighbor in self.adj_list[v]:
                if not visited[neighbor]:
                    dfs_recursive(neighbor)

        dfs_recursive(start)
        return traversal

    def display(self):
        print("Adjacency List:")
        for vertex in self.adj_list:
            print(f"{vertex}: {self.adj_list[vertex]}")
g = Graph(6)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 5)

print("BFS:", g.bfs(0))  
print("DFS:", g.dfs(0)) 
#Task 03
# : Implementing Dijkstra’s Algorithm for Shortest Path 
# Objective: Learn Dijkstra’s Algorithm for finding the shortest path in a weighted graph.
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
    'A': {'B': 4, 'C': 1},
    'B': {'A': 4, 'C': 2, 'D': 5},
    'C': {'A': 1, 'B': 2, 'D': 8},
    'D': {'B': 5, 'C': 8}
}

print(dijkstra(graph, 'A'))