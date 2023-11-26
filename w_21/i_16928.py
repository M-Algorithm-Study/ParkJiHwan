import heapq
import sys
input = sys.stdin.readline

x, y = map(int, input().split())
ladder = {}
snake = {}

for _ in range(x+y):
    a, b = map(int, input().split())
    
    if a < b:
        ladder[a] = b
    else:
        snake[a] = b

complete = 0
visited = [0 for _ in range(101)]

heap = []
heapq.heapify(heap)
heapq.heappush(heap, [0, 1])

while complete == 0:
    cnt, location = heapq.heappop(heap)
    
    if location >= 94:
        complete = 1
        print(cnt + 1)

    else:
        for i in range(1, 7):
            if location + i in ladder and visited[location + i] == 0:
                visited[location + i] = 1
                heapq.heappush(heap, [cnt + 1, ladder[location + i]])

            elif location + i in snake and visited[location + i] == 0:
                visited[location + i] = 1
                heapq.heappush(heap, [cnt + 1, snake[location + i]])
        
        switch = 0
        for j in range(6, 0, -1):
            if location + j not in snake and location + j not in ladder and switch == 0 and visited[location + j] == 0:
                visited[location + j] = 1
                switch = 1     
                heapq.heappush(heap, [cnt + 1, location + j])