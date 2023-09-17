import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

graph = [list(map(int, input().split())) for i in range(n)]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2: 
            queue = deque([(i, j)])
            
while queue:
    y, x = queue.popleft()
    
    for dir in range(4):
        if 0 <= y + dy[dir] < n and 0 <= x + dx[dir] < m and graph[y + dy[dir]][x + dx[dir]] == 1:
            graph[y + dy[dir]][x + dx[dir]] += graph[y][x]
            queue.append((y + dy[dir], x + dx[dir]))
            
for a in range(n):
    for b in range(m):
        if graph[a][b] == 1:
            graph[a][b] = -1
            
        elif graph[a][b] != 0:
            graph[a][b] -= 2

for line in graph:      
    print(*line)