import sys
from collections import deque
input = sys.stdin.readline

m, n, h = map(int, input().split())
box_list = []

for _ in range(h):
    box = []
    for _ in range(n):
        box.append(list(map(int, input().split())))     
    box_list.append(box)
    

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
dz = [-1, 1]

q = deque()
for z in range(h):
    for y in range(n):
        for x in range(m):
            if box_list[z][y][x] == 1:
                q.append((x, y, z))
    
while q:
    x, y, z = q.popleft()    

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < m and 0 <= ny < n:
            if box_list[z][ny][nx] == 0:
                q.append((nx, ny, z))
                box_list[z][ny][nx] = box_list[z][y][x] + 1
                
    for i in range(2):
        nz = z + dz[i]
        
        if 0 <= nz < h:
            if box_list[nz][y][x] == 0:
                q.append((x, y, nz))
                box_list[nz][y][x] = box_list[z][y][x] + 1

max_t = 0
err = 0
for b in box_list:
    for l in b:
        for t in l:
            if t > max_t:
                max_t = t
                
            elif t == 0:
                err += 1
                break

if err == 0:        
    print(max_t - 1)
else:
    print(-1)
    
    
    
#================================================================

import sys
from collections import deque
input = sys.stdin.readline

m, n, h = map(int, input().split())
box_list = []

for _ in range(h):
    box = []
    for _ in range(n):
        box.append(list(map(int, input().split())))
    box_list.append(box)


dx = [1, 0, -1, 0, 0, 0]
dy = [0, -1, 0, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

q = deque()
for z in range(h):
    for y in range(n):
        for x in range(m):
            if box_list[z][y][x] == 1:
                q.append((x, y, z))

while q:
    x, y, z = q.popleft()

    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]

        if 0 <= nx < m and 0 <= ny < n and 0 <= nz < h:
            if box_list[nz][ny][nx] == 0:
                q.append((nx, ny, nz))
                box_list[nz][ny][nx] = box_list[z][y][x] + 1
                
max_t = 0
err = 0
for b in box_list:
    for l in b:
        for t in l:
            if t > max_t:
                max_t = t
                
            elif t == 0:
                err += 1
                break

if err == 0:        
    print(max_t - 1)
else:
    print(-1)