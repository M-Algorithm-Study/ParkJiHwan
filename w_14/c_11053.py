import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split())) # 수열 A

dp = [1] * n

for i in range(1, n):
    for j in range(0, i):
        if arr[j] < arr[i] and dp[j] >= dp[i]: # 앞에 있는 수보다 (자신 포함) 몇 개나 더 큰가? 
            dp[i] = dp[j] + 1                  # and 앞에 있는 dp의 값이 더 크거나 같은 경우 dp[j] + 1
            
print(max(dp)) # [1, 2, 1, 3, 2, 4]

# 0 1

# 0 2
# 1 2

# 0 3
# 1 3
# 2 3

# 0 4
# 1 4
# 2 4
# 3 4

# 0 5
# 1 5
# 2 5
# 3 5
# 4 5
