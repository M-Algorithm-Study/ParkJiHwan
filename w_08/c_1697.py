from collections import deque

def bfs():
    queue = deque([(n)])

    while queue:
        x = queue.popleft()
        if x == k:
            print(arr[x])
            break
        
        for nx in (x - 1, x + 1, x * 2):
            if 0 <= nx <= MAX and not arr[nx]:
                arr[nx] = arr[x] + 1
                queue.append(nx)

MAX = 10 ** 5
arr = [0] * (MAX + 1)
n, k = map(int, input().split())

bfs()