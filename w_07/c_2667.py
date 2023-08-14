# dfs
import sys
from collections import deque
input = sys.stdin.readline

cnt = 0
n = int(input())
home_lst = [list(map(int, input().rstrip())) for _ in range(n)]
    
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for i in range(n):
    for j in range(n):
        if home_lst[i][j] == 1:
            queue = deque([(j, i)])
            cnt += 1
            home_lst[i][j] += cnt

            while queue:
                x, y = queue.popleft()

                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < n and 0 <= ny < n:
                        if home_lst[ny][nx] == 1:
                            home_lst[ny][nx] += cnt # 다른 단지에 각각 다른 값을 부여
                            queue.append((nx, ny))
                            
print(cnt)
res_lst = []
for num in range(2, cnt + 2):
    res = 0
    for a in range(n):
        for b in range(n):
            if home_lst[a][b] == num:
                res += 1
                
    res_lst.append(res)
    
print(*sorted(res_lst), sep = '\n')

# for row in home_lst:
#     print(" ".join(map(str, row)))
#==================================================================
# dfs
import sys

n = int(input())
square_list = [list(map(int, input().rstrip())) for _ in range(n)]
total = 0
cnt = 0
cnt_list = []

dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

for i in range(n):
    for j in range(n):
        if square_list[i][j] == 1:
            square_list[i][j] = 2
            cnt += 1
            stack = []
            stack.append(j)
            stack.append(i)
            total += 1

            while stack:
                y = stack.pop()
                x = stack.pop()

                for dir in range(4):
                    if 0 <= y + dy[dir] < n and 0 <= x + dx[dir] < n:
                        if square_list[y + dy[dir]][x + dx[dir]] == 1:
                            cnt += 1
                            square_list[y + dy[dir]][x + dx[dir]] = 2 # 단지 별로 체크해서 lst에 저장
                            stack.append(x + dx[dir])
                            stack.append(y + dy[dir])

            cnt_list.append(cnt)
            cnt = 0


print(total)
print(*sorted(cnt_list), sep = '\n')

#================================================================
# bfs

from collections import deque
import sys

n = int(input())
square_list = [list(map(int, input().rstrip())) for _ in range(n)]
total = 0
cnt = 0
cnt_list = []

dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

for i in range(n):
    for j in range(n):
        if square_list[i][j] == 1:
            square_list[i][j] = 2
            cnt += 1
            queue = deque([(j, i)])
            total += 1

            while queue:
                x, y = queue.popleft()

                for dir in range(4):
                    if 0 <= y + dy[dir] < n and 0 <= x + dx[dir] < n:
                        if square_list[y + dy[dir]][x + dx[dir]] == 1:
                            cnt += 1
                            square_list[y + dy[dir]][x + dx[dir]] = 2 # 단지 별로 체크해서 lst에 저장
                            queue.append((x + dx[dir], y + dy[dir]))

            cnt_list.append(cnt)
            cnt = 0


print(total)
print(*sorted(cnt_list), sep = '\n')
