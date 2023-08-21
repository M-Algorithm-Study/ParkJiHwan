import sys

m, n, k = map(int, sys.stdin.readline().split())
visited = [[1]*n for _ in range(m)]
dx = [1, 0, -1 ,0, 0]
dy = [0, 1, 0, -1, 0]
cnt = 0
total_area = []

for _ in range(k):
    rec_list = list(map(int, sys.stdin.readline().split()))

    for i in range(rec_list[1], rec_list[3]):
        for j in range(rec_list[0], rec_list[2]):
            visited[i][j] = 0

for r in range(m):
    for c in range(n):
        if visited[r][c] == 1:
            stack = []
            stack.append(r)
            stack.append(c)
            cnt += 1
            area = 0

            while stack:
                x = stack.pop()
                y = stack.pop()

                for dir in range(5):
                    if 0 <= x + dx[dir] < n and 0 <= y + dy[dir] < m:
                        if visited[y + dy[dir]][x + dx[dir]] == 1:
                            area += 1
                            visited[y + dy[dir]][x + dx[dir]] = 2
                            stack.append(y + dy[dir])
                            stack.append(x + dx[dir])

            total_area.append(area)

print(cnt)
print(*sorted(total_area))