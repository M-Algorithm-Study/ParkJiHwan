import sys
input = sys.stdin.readline

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
    
arr = [[0] * n for _ in range(n + 1)]

k = 0
for lst in matrix:
    k += 1
    for i in range(len(lst)):
        if i == 0:
            arr[k][i] = arr[k - 1][i] + lst[i]
        elif i == len(lst) - 1:
            arr[k][i] = arr[k - 1][i - 1] + lst[i]
        else:
            arr[k][i] += max(arr[k - 1][i - 1] + lst[i], arr[k - 1][i] + lst[i])

print(max(arr[-1]))