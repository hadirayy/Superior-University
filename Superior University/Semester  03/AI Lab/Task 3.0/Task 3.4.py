def bfs(graph,start):
    visited=set()
    queue=[]
    visited.add(start)
    queue.append(start)
    while queue:
        current_node=queue.pop(0)
        print(current_node)
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
graph ={
    0:[1,2],
    1:[0,3,4],
    2:[0],
    3:[1],
    4:[1]
}
bfs(graph,0)