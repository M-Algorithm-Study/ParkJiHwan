# import sys
# from collections import deque
# input = sys.stdin.readline

# n, m = map(int, input().split())
# cheese = [list(map(int, input().split())) for _ in range(n)]
# cnt = 0
# res = 0

# dx = [1, 0, -1, 0]
# dy = [0, -1, 0, 1]

# while True:
#     cnt_before = cnt
#     cnt = cnt + 2

#     for i in range(n):
#         for j in range(m):
#             if i == 0 or i == n - 1 or j == 0 or j == m - 1: # 겉쪽 공기와 안쪽 공기를 구분
#                 if cheese[i][j] == 0 or cheese[i][j] == cnt_before:
#                     cheese[i][j] = cnt
#                     queue = deque([(j, i)])
                    
#                 while queue:
#                     x, y = queue.popleft()

#                     for t in range(4):
#                         ny = y + dy[t]
#                         nx = x + dx[t]

#                         if 0 <= ny < n and 0 <= nx < m:
#                             if cheese[ny][nx] == 0 or cheese[ny][nx] == cnt_before:
#                                 cheese[ny][nx] = cnt
#                                 queue.append((nx, ny))


#     for q in range(n): # 공기에 연결된 내부 공간
#         for w in range(m):
#             if cheese[q][w] == cnt:
#                 queue_3 = deque([(w, q)])
                
#             while queue_3:
#                 x, y = queue_3.popleft()
                            
#                 for dir in range(4):
#                     ny = y + dy[dir]
#                     nx = x + dx[dir]

#                     if 0 <= ny < n and 0 <= nx < m:
#                         if cheese[ny][nx] == 0:
#                             cheese[ny][nx] = cnt
#                             queue_3.append((nx, ny))                


#     work = 0
#     for a in range(n):
#         for b in range(m):
#             if cheese[a][b] == 1: # 치즈가 존재할 때
#                 queue_2 = deque([(b, a)])
#                 work += 1
                
#                 while queue_2:
#                     x, y = queue_2.popleft()
#                     cheese_cnt = 0
                    
#                     for t in range(4):
#                         ny = y + dy[t]
#                         nx = x + dx[t]

#                         if 0 <= ny < n and 0 <= nx < m:
#                             if cheese[ny][nx] == cnt:
#                                 cheese_cnt += 1
                                
#                             if cheese_cnt == 2:
#                                 cheese[y][x] = cnt + 2
    
#     if work == 0: # 사라지는 치즈가 없을 경우
#         break
    
#     res += 1

# print(res)

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
res = 0

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

work = 0    
while True:
    visited = [[0]* n for _ in range(m)]

    queue = deque([(0, 0)])
        
    while queue:
        x, y = queue.popleft()
        cheese_cnt = 0
        
        for t in range(4):
            ny = y + dy[t]
            nx = x + dx[t]

            if cheese[ny][nx] == 1:
                visited[ny][nx] += 1
            
            if 0 <= ny < n and 0 <= nx < m:
                if cheese[ny][nx] == 1:
                    visited[ny][nx] += 1
                    
                if visited[ny][nx] > 1:
                    cheese[y][x] = 2
                    work += 1

    if work == 0: # 사라지는 치즈가 없을 경우
        break

res += 1

print(res)