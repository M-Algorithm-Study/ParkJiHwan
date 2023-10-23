from collections import deque

n = int(input())
a, b = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(start, target):
    visited = [False] * (n + 1)
    queue = deque([(start, 0)])
    visited[start] = True

    while queue:
        current, depth = queue.popleft()

        if current == target:
            return depth

        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append((neighbor, depth + 1))
                
    return -1

print(bfs(a, b))
