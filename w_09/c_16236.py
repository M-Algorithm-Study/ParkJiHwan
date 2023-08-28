from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
sea = [list(map(int, input().split())) for _ in range(n)]
level = [2, 0]
time = 0
top_left = []
before_time = 0

dx = [0, 1, -1, 0]
dy = [-1, 0, 0, 1]

while True:
    tmp = 0
    for i in range(n):
        for j in range(n):
            if sea[i][j] >= 20:
                sea[i][j] -= 20
                
            if sea[i][j] < level[0] and sea[i][j] != 0:
                tmp += 1
            
            elif sea[i][j] == 9:
                sea[i][j] = 0
                queue = deque([(i, j, time)])
    
    if tmp == 0:
        break
    

    while queue:
        y, x, time = queue.popleft()
        
        if top_left and before_time != time:
            before_time = time
            top_left = sorted(top_left)
            sea[top_left[0][0]][top_left[0][1]] = 9
            level[1] += 1
            top_left.clear()
            
            if level[0] == level[1]:
                level[0] += 1
                level[1] = 0
    
            queue.clear()
            break
        
        for dir in range(4):
            new_x = x + dx[dir]
            new_y = y + dy[dir]
            
            if 0 <= new_x < n and 0 <= new_y < n:
                if sea[new_y][new_x] < level[0] and sea[new_y][new_x] != 0:
                    top_left.append([new_y, new_x])
                    
                elif sea[new_y][new_x] <= level[0]:
                    sea[new_y][new_x] += 20
                    queue.append((new_y, new_x, time + 1))
        
        before_time = time
      
print(time)