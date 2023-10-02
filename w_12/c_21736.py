from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

matrix = [list(input().strip()) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 'I': # 도연이의 위치를 파악
            queue = deque([(i, j)])

cnt = 0 # 만날 수 있는 사람의 수          
while queue:
    y, x = queue.popleft()
    
    for dir in range(4):
        if 0 <= y + dy[dir] < n and 0 <= x + dx[dir] < m:
            if matrix[y + dy[dir]][x + dx[dir]] == 'P': # 탐색되는 위치에 사람이 있다면
                matrix[y + dy[dir]][x + dx[dir]] = 'X' # 탐색되는 위치를 벽으로 바꾸고
                cnt += 1 # 사람 수를 1명 더한다.
                queue.append((y + dy[dir], x + dx[dir])) # 해당 위치에서 다시 탐색
            
            elif matrix[y + dy[dir]][x + dx[dir]] == 'O': # 탐색되는 위치가 빈 공간이라면
                matrix[y + dy[dir]][x + dx[dir]] = 'X' # 탐색되는 위치를 벽으로 바꾸고
                queue.append((y + dy[dir], x + dx[dir])) # 해당 위치에서 다시 탐색

if cnt == 0:
    print('TT')
else:
    print(cnt)
