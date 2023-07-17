import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []

for i in range(n):
    arr.append(list(map(int, input().strip())))
    
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def bfs(x, y):
    
    q = deque()
    q.append((x, y))
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 1:
                    q.append((nx, ny))
                    arr[nx][ny] = arr[x][y] + 1
                    
    return arr[n-1][m-1]

print(bfs(0, 0))