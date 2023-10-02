import sys
input = sys.stdin.readline

n = int(input())

arr = [0] + [1] * 9 

for _ in range(n - 1):
    ans = [0] * 10
    for i in range(10):
        if arr[i] > 0:
            if i < 9:
                ans[i + 1] += arr[i]
                
            if i >= 1:
                ans[i - 1] += arr[i]

    arr = [0] * 10
    arr = ans

print(sum(arr) % 1000000000)