import sys
input = sys.stdin.readline
        
n, k = map(int, input().split())

thing = [[0, 0]]
dp = [[0] * (k + 1) for _ in range(n + 1)] # dp에 물건을 하나 넣었을 때, 각 무게마다(1, 2, 3 ,4...) 가치의 최댓값을 구하는 식으로 저장할 것임

for _ in range(n):
    thing.append(list(map(int, input().split())))

for i in range(1, n + 1):
    for j in range(1, k + 1): # 가방의 무게를 j로 제한하면,( k = 7 이라면 j는 1 ~ 7)
        w = thing[i][0]
        v = thing[i][1]

        if j < w: # 제한된 무게 j < 물건의 무게 일 때: 이전 값을 그대로 가져옴
            dp[i][j] = dp[i-1][j]
        else: # 물건의 무게 =< 제한된 무게 j: max(이전 값을 그대로 가져옴, 이전 j - w의 값에 v를 더한 값을 가져옴)
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v) 
                        
print(dp[n][k])

# 가방에 물건을 넣을 때, 물건을 하나 넣을 때마다 무게 하나하나(1일 때부터 k 일 때까지)를 
# 기록해둔 다음 이전 값이랑 비교해서 큰 값을 넣어주면 되는 것이었다.