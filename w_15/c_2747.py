n = int(input())
dp = [1] * n

if n <= 2: # n == 1 or 2 일 때, 둘다 1의 값을 가짐
    print(1)
    
else:
    for i in range(2, n): # dp[i] = dp[i-1] + dp[i-2]를 연산하며 dp에 저장
        dp[i] = dp[i-1] + dp[i-2]
        
    print(dp[-1])
    
# 다른 풀이

# n = int(input())
# a, b, c = 1, 1, 0

# for i in range(n):
#     tmp_a, tmp_b, tmp_c = a + b, a, b
#     a, b, c = tmp_a, tmp_b, tmp_c
    
# print(c)