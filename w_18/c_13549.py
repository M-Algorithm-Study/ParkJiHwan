# from collections import deque

# n, k = map(int, input().split())

# if n >= k: # 수빈이가 동생 앞에 있을 떄
#     print(n - k)

# else:
#     MAX = 100001
#     q = deque()
#     q.append(n)
#     dp = [-1 for _ in range(MAX)]
#     dp[n] = 0

#     while q:
#         x = q.popleft()
#         if x == k:
#             print(dp[x])
#             break
        
#         if 0 <= x - 1 < MAX and dp[x - 1] == -1:
#             dp[x - 1] = dp[x] + 1
#             q.append(x - 1)
            
#         if x * 2 < MAX and dp[x * 2] == -1:
#             dp[x * 2] = dp[x]            
#             q.appendleft(x * 2)
            
#         if x + 1 < MAX and dp[x + 1] == -1:
#             dp[x + 1] = dp[x] + 1
#             q.append(x + 1)


#================================================================
import heapq

n, k = map(int, input().split())

if n >= k: # 수빈이가 동생 앞에 있을 떄
    print(n - k)

else:
    MAX = 100001
    check_list = [0 for _ in range(MAX)]
    Q = [(0, n)]    # 큐 변수: [(소요 시간, 정점)]
        
    while Q:     # 우선순위 큐 최솟값 기준으로 정점까지 최단 경로 삽입
        time, x = heapq.heappop(Q)
        if x == k:
            print(time)
            break
        
        if 0 <= x - 1 < MAX and check_list[x - 1] == 0:
            check_list[x - 1] = 1
            heapq.heappush(Q, (time + 1, x - 1))

        if x * 2 < MAX and check_list[x * 2] == 0:
            check_list[x * 2] = 1            
            heapq.heappush(Q, (time, x * 2))
            
        if x + 1 < MAX and check_list[x + 1] == 0:
            check_list[x + 1] = 1
            heapq.heappush(Q, (time + 1, x + 1))