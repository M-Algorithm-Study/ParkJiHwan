# import sys
# input = sys.stdin.readline

# t = int(input())

# for _ in range(t):
#     n = int(input())
#     sticker = [list(map(int, input().split())) for _ in range(2)]
#     dp = [[0, 0, 0] for _ in range(n+1)]

#     for i in range(n):
#         dp[i+1][0] = max(dp[i][1] + sticker[0][i], dp[i][2] + sticker[0][i])
#         dp[i+1][1] = max(dp[i][0] + sticker[1][i], dp[i][2] + sticker[1][i])
#         dp[i+1][2] = max(dp[i])

#     print(max(dp[-1]))
    
#================================================================
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    dp = [list(map(int,input().split())) for _ in range(2)] # dp에 스티커값을 직접 입력받음
    
    if n > 1 : # n == 1 일 경우 dp에는 인덱스 0밖에 존재하지 않으므로 오류가 난다.
        dp[0][1] += dp[1][0]
        dp[1][1] += dp[0][0]
            
    for i in range(2, n): # dp[0][i-1]의 값과 dp[1][i-1]의 값을 서로 비교
        dp[0][i] += max(dp[1][i-1], dp[1][i-2])
        dp[1][i] += max(dp[0][i-1], dp[0][i-2])

    print(max(dp[0][n-1], dp[1][n-1]))
    

# 이전 풀이보다 메모리(dp에 직접 값을 받는 방식) 및 시간(dp에 저장하는 값을 3개에서 2개로 줄임) 절약
