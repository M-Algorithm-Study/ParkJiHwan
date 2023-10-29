import heapq

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

arr = sorted(arr, key = lambda x: x[1]) # 강의 시작 시간 기준으로 정렬

min_heap = []
cnt = 0

print(arr)
for i in arr:
    while min_heap and min_heap[0] <= i[1]: # min_heap(강의 종료 시간)보다 i의 강의 시작 시간이 더 나중일 경우
        heapq.heappop(min_heap)
    heapq.heappush(min_heap, i[2])
    cnt = max(cnt, len(min_heap))

    print(min_heap)
print(cnt)