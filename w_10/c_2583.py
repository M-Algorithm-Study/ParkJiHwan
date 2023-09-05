from collections import deque
import sys

input = sys.stdin.readline

m, n, k = map(int, input().split())
visited = [[0] * n for _ in range(m)]
total = []

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
   
    for i in range(y1, y2): # 모눈종이에 그린 직사각형
       for j in range(x1, x2):
           if visited[i][j] == 0: 
                visited[i][j] = 1
               
for a in range(m): 
    for b in range(n):
        if visited[a][b] == 0:
            visited[a][b] = 1   
            queue = deque([(a, b)])

            cnt = 1
            while queue:
                y, x = queue.popleft()
                
                for dir in range(4):
                    new_y = y + dy[dir]
                    new_x = x + dx[dir]
                    
                    if 0 <= new_y < m and 0 <= new_x < n and visited[new_y][new_x] == 0: # 모눈종이 안에 있고, 방문하기 전
                        visited[new_y][new_x] = 1
                        queue.append((new_y, new_x))
                        cnt += 1
                        
            total.append(cnt)

total = sorted(total)
print(len(total))
print(*total)
