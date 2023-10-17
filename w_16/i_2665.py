from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

matrix = [input() for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

queue = deque([(0, 0)])
visited = [[0] * n for _ in range(n)] 
print(visited)
while queue:
    y, x = queue.popleft()
    
    for dir in range(4):
        nx = x + dx[dir]
        ny = y + dy[dir]
        
        if 0 <= nx < n and 0 <= ny < n and visited[ny][nx] == 0:
            if matrix[ny][nx] == 0:
                matrix[ny][nx] = 2
                
            elif matrix[ny][nx] == 1 and matrix[ny][nx] < matrix[y][x]:
                matrix[ny][nx] = matrix[y][x] + 1
                

            