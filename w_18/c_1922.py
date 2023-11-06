import heapq
import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
adj = [[] for _ in range(n)]

for i in range(m):
    start, end, time = map(int, input().split())
    adj[start - 1].append((time, end - 1)) # 시간, 끝나는 점을 adj[시작점]에 넣음
    adj[end - 1].append((time, start - 1))
visited = [0] * n
Q = []

for time, node in adj[0]:
    heapq.heappush(Q, (time, node))
visited[0] = 1
cnt = 0
ans = 0

while Q:
    time, node = heapq.heappop(Q)
    if visited[node]:
        continue
    visited[node] = 1
    ans += time
    cnt += 1
    if cnt == n - 1:
        break
    for time, nxt in adj[node]:
        if visited[nxt] == 0:
            heapq.heappush(Q, (time, nxt))
                
print(ans)