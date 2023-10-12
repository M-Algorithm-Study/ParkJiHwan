import sys
input = sys.stdin.readline

n = int(input())
wine = [int(input()) for i in range(n)]

dp = [0] * n

dp[0] = wine[0]

if n > 1:
    dp[1] = wine[0] + wine[1]

if n > 2:
    dp[2] = max(wine[2] + wine[1], wine[2] + wine[0], dp[1]) # xoo, oxo, oox

for i in range(3, n): # oox, xoo, oxo
    dp[i] = max(dp[i - 1], dp[i - 3] + wine[i - 1] + wine[i], dp[i - 2] + wine[i])

print(dp[n - 1])