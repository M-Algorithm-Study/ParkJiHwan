import sys
import heapq
input = sys.stdin.readline

def solution(n, works):
    heap = []
    if n > sum(works): # 작업량보다 시간이 더 많다면
        return 0
        
    for i in works:
        heapq.heappush(heap, - i) # works의 숫자에 -를 입힌 상태로 힙에 저장
                                  # heap = [-4, -3, -3]
    for _ in range(n):
        heapq.heappush(heap, heapq.heappop(heap) + 1)   # 최소힙 구한 후 1을 더함
                                                        # 음수 처리했으므로 최대힙에서 1을 뺀 것과 같다. 
    answer = 0
    for j in heap:
        answer += j ** 2    # 어차피 제곱할 것이므로 부호변환 안해도 됨
    
    return answer

# works = [5, 7, 8]
# n = 6
# print(solution(n, works))