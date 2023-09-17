import sys
input = sys.stdin.readline

h, w = map(int, input().split())
block_lst = list(map(int, input().split()))
visited = [[0] * h for _ in range(w)]

for i in range(w):
    for j in range(h):
        if j < block_lst[i]:
            visited[i][j] = 1
        else:
            visited[i][j] = 0

rain = 0
for x in range(h):
    switch = 0
    tmp = 0
    for y in range(w):
        if switch == 0 and visited[y][x] == 1:
            switch += 1
        
        elif switch == 1 and visited[y][x] == 0:
            tmp += 1
        
        elif switch == 1 and visited[y][x] == 1:
            rain += tmp
            tmp = 0

print(rain)