# 시작점에서 도착점까지의 가장 저렴한 가격을 계산하되, k개의 경유지 이내에
# 도착하는 가격을 리턴하라. 경로가 존재하지 않을 경우 -1을 리턴한다.

# n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 
# src = 0, dst = 3, k = 1

from collections import defaultdict
import heapq

def findCheapestPrice(n, flights, src, dst, K):
    graph = defaultdict(list)
    # 그래프 인접 리스트 구성
    for u, v, w in flights:
        graph[u].append((v, w))
    
    # 큐 변수: [(가격, 정점, 남은 가능 경유지 수)]
    Q = [(0, src, K)]
    
    # 우선순위 큐 최솟값 기준으로 도착점까지 최소 비용 판별
    while Q:
        price, node, k = heapq.heappop(Q)
        if node == dst:
            return price
        if k >= 0:
            for v, w in graph[node]: # v는 도착지, w는 소요시간
                alt = price + w
                heapq.heappush(Q, (alt, v, k - 1))
                
    return -1
    
print(findCheapestPrice(n = 4, flights = [[0,1,1],[0,2,5],[1,2,1],[2,3,1]], src = 0, dst = 3, K = 1))