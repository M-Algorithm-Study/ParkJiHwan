from collections import deque

def bfs():
    queue = deque([(n)])

    while queue:
        x = queue.popleft()
        if x == k: # 수빈이가 동생과 같은 위치에 있을 경우
            print(arr[x])
            break
        
        for nx in (x - 1, x + 1, x * 2): # 순간이동
            if 0 <= nx <= MAX and not arr[nx]: # MAX보다 작거나 같을 경우, arr에 포함되지 않았을 경우
                arr[nx] = arr[x] + 1 # arr[x] 값에 1을 더한 값
                queue.append(nx)

MAX = 10 ** 5
arr = [0] * (MAX + 1)
n, k = map(int, input().split())

bfs()