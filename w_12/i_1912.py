import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
dp = [0 for _ in range(n+1)] # [0] * (n + 1)

for i in range(n):
    dp[i+1] = max(dp[i] + lst[i], lst[i])
    
print(max(dp[1:]))


'''
dp 문제, 구간별 최대값을 구하기 위해서는 max(지금까지 전부 더한 값, 지금의 값)을
구해야하는데, 이를 비교하기 위해서는 메모이제이션을 이용해야겠다고 생각이 들었다.

'''