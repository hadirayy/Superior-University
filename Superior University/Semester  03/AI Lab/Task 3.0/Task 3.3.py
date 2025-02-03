def bfs_without_queue(graph,start):
    visited =[False]*len(graph)
    visited[start]=True
    node_visit=[start]
    while node_visit:
        current_node = node_visit.pop(0)
        print(current_node)
        for neighbor in graph[current_node]:
            if not visited[neighbor]:
                visited[neighbor]=True
                node_visit.append(neighbor)
graph=[
    [1,2],
    [0,3,4],
    [0],
    [1],
    [1]
]
bfs_without_queue(graph,0)