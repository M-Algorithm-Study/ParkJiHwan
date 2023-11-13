import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
total_max = 0
tetromino = [
[(1, 0), (2, 0), (3, 0)],
[(0, 1), (0, 2), (0, 3)],
[(1, 0), (1, 1), (0, 1)],
[(0, 1), (1, 1), (2, 1)],
[(0, 1), (-1, 1), (-2, 1)],
[(0, -1), (1, -1), (2, -1)],
[(0, -1), (-1, -1), (-2, -1)],
[(0, 1), (0, 2), (-1, 2)],
[(0, 1), (0, 2), (1, 2)],
[(0, -1), (0, -2), (1, -2)],
[(0, -1), (0, -2), (-1, -2)],
[(1, 0), (1, -1), (2, -1)],
[(1, 0), (1, 1), (2, 1)],
[(0, 1), (1, 1), (1, 2)],
[(0, 1), (-1, 1), (-1, 2)],
[(1, 0), (0, -1), (-1, 0)],
[(0, -1), (-1, 0), (0, 1)],
[(-1, 0), (1, 0), (0, 1)],
[(0, 1), (1, 0), (0, -1)]
]

stack = []
for i in range(n):
    for j in range(m):
        stack.append(i)
        stack.append(j)

while stack:
    x = stack.pop()
    y = stack.pop()
    
    for moving in tetromino:
        total = arr[y][x]
        for dir in moving:
            if 0 <= x + dir[0] < m and 0 <= y + dir[1] < n:
                total += arr[y + dir[1]][x + dir[0]]

        if total_max < total:
            total_max = total
            
print(total_max)