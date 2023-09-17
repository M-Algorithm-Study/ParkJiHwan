import sys
input = sys.stdin.readline

n = int(input())
command = input()

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

x = 0
y = 0
s = 0
visited_x = [0]
visited_y = [0]

for i in command:
    if i == 'F':
        x += dx[s % 4]
        y += dy[s % 4]
        visited_x.append(x)
        visited_y.append(y)
        
    elif i == 'R':
        s += 1
    
    elif i == 'L':
        s += 3
        
graph_x = max(visited_x) - min(visited_x) + 1
graph_y = max(visited_y) - min(visited_y) + 1
graph = [['#'] * graph_x for _ in range(graph_y)]

for num in range(len(visited_x)):
    if graph[visited_y[num] - min(visited_y)][visited_x[num] - min(visited_x)] == '#':
        graph[visited_y[num] - min(visited_y)][visited_x[num] - min(visited_x)] = '.'


for line in graph:
    print(*line, sep='')