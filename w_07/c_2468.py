# dfs
import sys
input = sys.stdin.readline

N = int(input())
area = [list(map(int, input().split())) for _ in range(N)]
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
cnt_lst = []

max_num = max(max(line) for line in area) # 최대 높이를 구함, 최대 높이 - 1까지 계산하기 위함

for num in range(max_num):
    cnt = 0 # 안전 영역의 개수
    visited = [[0]*N for _ in range(N)] # 방문 리스트
    
    for a in range(N):
        for b in range(N):
            if area[a][b] > num:
                visited[a][b] = 1 # 안전한 영역일 경우 1로 표시
                
    for i in range(N):
        for j in range(N):
            if  visited[i][j] == 1: # 안전한 영역일 경우 stack에 넣고 0으로 변경(확인했다는 표시)
                visited[i][j] = 0                
                stack = []
                stack.append(j)
                stack.append(i)
                cnt += 1
            
                while stack:
                    y = stack.pop()
                    x = stack.pop()
                     
                    for k in range(4):
                        ny = y + dy[k]
                        nx = x + dx[k]
                        if 0 <= nx < N and 0 <= ny < N:
                            if visited[ny][nx] == 1:
                                visited[ny][nx] = 0
                                stack.append(nx)
                                stack.append(ny)

    cnt_lst.append(cnt)

print(max(cnt_lst))


#=================================================================================================================
# bfs
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
area = [list(map(int, input().split())) for _ in range(N)]
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
cnt_lst = []

max_num = max(max(line) for line in area)

for num in range(max_num):
    cnt = 0
    visited = [[0] * N for _ in range(N)]

    for a in range(N):
        for b in range(N):
            if area[a][b] > num:
                visited[a][b] = 1

    for i in range(N):
        for j in range(N):
            if visited[i][j] == 1:
                visited[i][j] = 0
                queue = deque([(j, i)])
                cnt += 1

                while queue:
                    x, y = queue.popleft()

                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < N and 0 <= ny < N:
                            if visited[ny][nx] == 1:
                                visited[ny][nx] = 0
                                queue.append((nx, ny))
    cnt_lst.append(cnt)

print(max(cnt_lst))

