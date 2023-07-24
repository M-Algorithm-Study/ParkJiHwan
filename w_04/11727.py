import sys
input = sys.stdin.readline

tiling = [1, 3]
n = int(input())
while(len(tiling) < n):
    tiling.append((tiling[-1] + tiling[-2] * 2) % 10007)

print(tiling[n - 1])