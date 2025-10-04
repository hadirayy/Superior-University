MAX_X = 3
MAX_Y = 4
GOAL = 2

def get_successors(state):
    x, y = state
    successors = []
    if x < MAX_X:
        successors.append(((MAX_X, y), f"Fill {MAX_X}-gallon jug (X ← {MAX_X})"))
    if y < MAX_Y:
        successors.append(((x, MAX_Y), f"Fill {MAX_Y}-gallon jug (Y ← {MAX_Y})"))
    if x > 0:
        successors.append(((0, y), "Empty X (X ← 0)"))
    if y > 0:
        successors.append(((x, 0), "Empty Y (Y ← 0)"))
    if x > 0:
        total = x + y
        new_y = min(total, MAX_Y)
        new_x = total - new_y
        successors.append(((new_x, new_y), "Pour all X → Y (overflow allowed)"))
    if y > 0:
        total = x + y
        new_x = min(total, MAX_X)
        new_y = total - new_x
        successors.append(((new_x, new_y), "Pour all Y → X (overflow allowed)"))
    if x > 0 and y < MAX_Y:
        transfer = min(x, MAX_Y - y)
        successors.append(((x - transfer, y + transfer), "Pour X → Y until Y full"))
    if y > 0 and x < MAX_X:
        transfer = min(y, MAX_X - x)
        successors.append(((x + transfer, y - transfer), "Pour Y → X until X full"))
    
    return successors

def dfs(state, visited, path):
    x, y = state
    if x == GOAL or y == GOAL:
        return True
    visited.add(state)
    for (next_state, rule) in get_successors(state):
        if next_state in visited:
            continue
        path.append((state, rule, next_state))
        if dfs(next_state, visited, path):
            return True
        path.pop()
    return False

def solve(start=(0, 0)):
    visited = set()
    path = []
    found = dfs(start, visited, path)
    if found:
        print("Solution found! Steps:")
        for (s, rule, ns) in path:
            print(f"At state {s}, apply [{rule}] → get {ns}")
        final = path[-1][2] if path else start
        print(f"Reached final state {final} where one jug has {GOAL} gallons.")
    else:
        print("No solution found.")

if __name__ == "__main__":
    solve((0, 0))
