import sys


n, l, r = map(int, input().split())
arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))     

for line in arr:
    for world in line:
        continue