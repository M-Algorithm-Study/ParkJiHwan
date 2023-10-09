import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = [1] * n

for i in range(1, n):
    for j in range(0, i):
        if arr[j] < arr[i] and dp[j] >= dp[i]: # 앞에 있는 수보다 몇개나 더 큰가? 
            dp[i] = dp[j] + 1                  # and 앞에 있는 dp의 값이 더 크거나 같은 경우 dp[j] + 1

print(max(dp))
