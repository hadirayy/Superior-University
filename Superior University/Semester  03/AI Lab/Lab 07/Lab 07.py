import os 
os.system('cls')
graph = {
    'A': {'B': 2, 'C': 4},
    'B': {'C': 1, 'D': 5},
    'C': {'D': 3},
    'D': {}
}

h = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 0  
}
def A_staric(start, goal):
    list = [start] 
    g = {start: 0}  
    parent= {start: None}

    while list:
        current = min(list, key=lambda node: g[node] + h[node])
        if current == goal:
            return path(parent, goal)

        list.remove(current)

        for neighbor in graph[current]:
            new_g = g[current] + graph[current][neighbor]

            if neighbor not in g or new_g < g[neighbor]:
                g[neighbor] = new_g
                parent[neighbor] = current
                if neighbor not in list:
                    list.append(neighbor)

def path(parent, node):
    path = []
    while node:
        path.append(node)
        node = parent[node]
    return path[::-1]

path = A_staric('A', 'D')
if path:
    print("Path found:", " -> ".join(path))
else:
    print("No path found.")
