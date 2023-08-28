import sys

input = sys.stdin.readline

dx = [1, -1]

n = int(input())
stone_lst = list(map(int, input().split()))
s = int(input())
visited = [0] * n
frog = []
visited[s-1] = 1

frog.append(s-1)

while frog:
    x = frog.pop()
    
    for dir in dx:
        if 0 <= x + stone_lst[x] * dir < n:
            if visited[x + stone_lst[x] * dir] == 0:
                visited[x + stone_lst[x] * dir] = 1
                frog.append(x + stone_lst[x] * dir)

print(sum(visited))       
        