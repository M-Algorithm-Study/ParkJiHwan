from collections import deque
import sys
input = sys.stdin.readline

m, n = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(m)]
cnt = 0

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

queue = deque([(0, 0)])

while queue:
    y, x = queue.popleft()
    
    for dir in range(4):
        ny = y + dy[dir]
        nx = x + dx[dir]
        
        if 0 <= ny < m and 0 <= nx < n:
            if ny == m - 1 and nx == n - 1:
                cnt += 1
            elif matrix[y][x] > matrix[ny][nx]:
                queue.append((ny, nx))
                
print(cnt)