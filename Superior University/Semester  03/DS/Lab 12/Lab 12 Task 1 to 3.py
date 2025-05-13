#Task 01
# : Implementing a Graph Using Adjacency List & Adjacency Matrix 
# Objective: Understand and implement graph representations in Python using both 
# adjacency list and adjacency matrix. 

class Graph:
    def __init__(self, directed=False):
        self.directed = directed
        self.vertices = []  
        self.adj_list = {}  
        self.adj_matrix = []

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices.append(vertex)
            self.adj_list[vertex] = []

           
            size = len(self.vertices)
            for row in self.adj_matrix:
                row.append(0)
            self.adj_matrix.append([0] * size)

    def add_edge(self, src, dest):
        if src not in self.vertices or dest not in self.vertices:
            print("Error: One or both vertices not found.")
            return

        self.adj_list[src].append(dest)
        if not self.directed:
            self.adj_list[dest].append(src)

        
        i = self.vertices.index(src)
        j = self.vertices.index(dest)
        self.adj_matrix[i][j] = 1
        if not self.directed:
            self.adj_matrix[j][i] = 1

    def display_adj_list(self):
        print("Adjacency List:")
        for vertex in self.vertices:
            print(f"{vertex}: {self.adj_list[vertex]}")

    def display_adj_matrix(self):
        print("\nAdjacency Matrix:")
        print("   " + " ".join(self.vertices))
        for i, row in enumerate(self.adj_matrix):
            formatted_row = " ".join(str(val) for val in row)
            print(f"{self.vertices[i]}: {formatted_row}")

 

#Task 02
#  Implementing Breadth-First Search (BFS) & Depth-First Search 
# (DFS) 
# Objective: Learn and apply BFS and DFS traversal techniques on graphs.


from collections import deque

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, src, dest):
        if src not in self.adj_list:
            self.adj_list[src] = []
        if dest not in self.adj_list:
            self.adj_list[dest] = []
        self.adj_list[src].append(dest)
        self.adj_list[dest].append(src) 

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        result = []

        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                for neighbor in self.adj_list.get(vertex, []):
                    if neighbor not in visited:
                        queue.append(neighbor)
        return result

    def dfs_recursive(self, start):
        visited = set()
        result = []

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            result.append(node)
            for neighbor in self.adj_list.get(node, []):
                dfs(neighbor)

        dfs(start)
        return result

    def dfs_stack(self, start):
        visited = set()
        stack = [start]
        result = []

        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                for neighbor in reversed(self.adj_list.get(vertex, [])):
                    if neighbor not in visited:
                        stack.append(neighbor)
        return result
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)

print("BFS:", g.bfs(0))               
print("DFS (recursive):", g.dfs_recursive(0))  
print("DFS (stack):", g.dfs_stack(0))         


#Task 03
# Implementing Dijkstra’s Algorithm for Shortest Path 
# Objective: Learn and implement Dijkstra’s Algorithm for finding the shortest path in a 
# weighted graph. 

import heapq

class Graph:
    def __init__(self):
        self.adj_list = {} 

    def add_edge(self, src, dest, weight):
        if src not in self.adj_list:
            self.adj_list[src] = []
        if dest not in self.adj_list:
            self.adj_list[dest] = []
        self.adj_list[src].append((dest, weight))
        self.adj_list[dest].append((src, weight))  

    def dijkstra(self, start):
        distances = {node: float('inf') for node in self.adj_list}
        distances[start] = 0
        visited = set()
        min_heap = [(0, start)] 

        while min_heap:
            current_dist, current_node = heapq.heappop(min_heap)
            if current_node in visited:
                continue
            visited.add(current_node)

            for neighbor, weight in self.adj_list[current_node]:
                distance = current_dist + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(min_heap, (distance, neighbor))

        return distances
g = Graph()
g.add_edge("A", "B", 4)
g.add_edge("A", "C", 1)
g.add_edge("C", "B", 2)
g.add_edge("B", "D", 1)

print(g.dijkstra("A"))




