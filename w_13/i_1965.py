import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
arr = [0] * n

for i in range(len(lst)):
    tmp = []
    for j in range(i):
        if lst[j] < lst[i]:
            tmp.append(arr[j])
    
    if tmp:
        arr[i] += max(tmp) + 1

print(max(arr) + 1)