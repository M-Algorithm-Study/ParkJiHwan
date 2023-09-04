from collections import deque
import sys

input = sys.stdin.readline

dx = [1, 1, 0, -1, -1, -1, 0, 1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

queue = deque([])
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            arr[i][j] = -1
            queue.append((i, j, 1))
            
while queue:
    y, x, t = queue.popleft()
    
    for dir in range(8):
        new_y = y + dy[dir]
        new_x = x + dx[dir]
        
        if 0 <= new_y < n and 0 <= new_x < m and arr[new_y][new_x] == 0:
            arr[new_y][new_x] = t
            queue.append((new_y, new_x, t + 1))

print(max(num for lst in arr for num in lst))

# from itertools import chain
# print(max(chain.from_iterable(arr))