import sys
input = sys.stdin.readline

n = int(input())

tmp = list(map(int,input().split()))
dp_1 = tmp
dp_2 = tmp

for _ in range(n - 1):
    a, b, c = map(int, input().split())
    dp_1 = [a + max(dp_1[0], dp_1[1]), b + max(dp_1), c + max(dp_1[1], dp_1[2])]   #  max(dp_1[0], dp_1[1], dp_1[2])을 max(dp_1)로 줄일 수 있음
    dp_2 = [a + min(dp_2[0], dp_2[1]), b + min(dp_2), c + min(dp_2[1], dp_2[2])]

print(max(dp_1), min(dp_2))

# DP에서 말하는 슬라이딩 윈도우 기법이란, 메모이제이션을 할 때 더 이상 
# 사용하지 않는 값을 저장하지 않고 배열을 계속하여 갱신해주는 것

#================================================================================================================================

# 처음 풀이
 
# # import sys
# input = sys.stdin.readline

# n = int(input())

# a1, b1, c1 = map(int, input().split())

# a_min = a1
# a_max = a1

# b_min = b1
# b_max = b1

# c_min = c1
# c_max = c1

# res = [[a1, b1, c1], [a1, b1, c1]]

# for _ in range(n - 1):
#     a, b, c = map(int, input().split())
#     res[0][0] = max(a_max + a, b_max + a)
#     res[1][0] = min(a_min + a, b_min + a)
#     res[0][1] = max(a_max + b, b_max + b, c_max + b)
#     res[1][1] = min(a_min + b, b_min + b, c_min + b)
#     res[0][2] = max(b_max + c, c_max + c)
#     res[1][2] = min(b_min + c, c_min + c)

#     a_max = res[0][0]
#     a_min = res[1][0]
#     b_max = res[0][1]
#     b_min = res[1][1]
#     c_max = res[0][2]
#     c_min = res[1][2]

# print(max(res[0]), min(res[1]))