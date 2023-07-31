n = int(input())
stair_list = [int(input()) for _ in range(n)]
dp=[0]*(n)
if len(stair_list) <= 2: # 2개 이하
    print(sum(stair_list))
else: # 3개 이상
    dp[0] = stair_list[0]
    dp[1] = stair_list[0] + stair_list[1]
    for i in range(2,n):
        dp[i] = max(dp[i-3] + stair_list[i-1] + stair_list[i], dp[i-2] + stair_list[i])
    print(dp[-1])