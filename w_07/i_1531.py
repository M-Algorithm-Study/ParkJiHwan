import sys
input = sys.stdin.readline

n, m = map(int, input().split())

num_lst = [[0]*101 for _ in range(101)]
res = 0

for _ in range(n):
    x, y, a, b = map(int, input().split())
    
    for dy in range(y, b+1):
        for dx in range(x, a+1):
            num_lst[dy][dx] += 1
            
for c in range(101):
    for r in range(101):
        if num_lst[c][r] > m:
            res += 1

print(res)