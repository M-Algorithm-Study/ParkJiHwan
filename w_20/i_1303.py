from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

soldier = [input().rstrip() for _ in range(m)]
visited = [[0] * n for _ in range(m)]
ans = [0, 0]
q = deque()
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def sol(x, y, color):
    q.append((y, x))
    tmp = 1
    while q:
        y, x = q.popleft()
        
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            
            if 0 <= nx < n and 0 <= ny < m and visited[ny][nx] == 0 and soldier[ny][nx] == color:
                visited[ny][nx] = 1
                tmp += 1
                q.append((ny, nx))

    if color == 'W':
        ans[0] += tmp ** 2
    else:
        ans[1] += tmp ** 2
        
for i in range(m):
    for j in range(n):
        if visited[i][j] == 0:
            visited[i][j] = 1
            if soldier[i][j] == 'W':
                sol(j, i, 'W')
            else:
                sol(j, i, 'B')

print(*ans)