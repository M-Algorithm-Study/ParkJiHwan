from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
cnt = 0

command = [[(1, 1), (1, 0)], [(1, 1), (0, 1)], [(1, 1), (1, 0), (0, 1)]] # command[0]: 가로, command[1]: 세로,  command[2]: 대각선
dp = [[[0, 0, 0] for _ in range(n)] for _ in range(n)] # [위치y][위치x][command[0], command[1], command[2]]
dp[0][1][0] = 1 # (0, 1) 의 좌표에 command[0](가로) 방식으로 도착
sum_x_y = 1

while sum_x_y <= 2*(n - 1): # 원하는 지점 (n - 1, n - 1)이 나올 때 까지 순환
    a = sum_x_y
    b = 0
    tmp = deque([])
    
    for i in range(sum_x_y + 1):
        if a < n and b < n:
            tmp.append((a, b))
        a -= 1
        b += 1     
    
    while tmp:
        x, y = tmp.popleft()
        for k in range(3):
            if dp[y][x][k]: # * (x, y)에 command[k]의 값이 있다면
                for j in command[k]:
                    if j == (1, 0):
                        if x + j[0] < n and y + j[1] < n and arr[y + j[1]][x + j[0]] == 0:
                            dp[y + j[1]][x + j[0]][0] += dp[y][x][k]

                    elif j == (0, 1):
                        if x + j[0] < n and y + j[1] < n and arr[y + j[1]][x + j[0]] == 0:
                            dp[y + j[1]][x + j[0]][1] += dp[y][x][k]
                            
                    else:
                        if x + j[0] < n and y + j[1] < n and arr[y + 1][x] + arr[y][x + 1] + arr[y + 1][x + 1] == 0:
                            dp[y + j[1]][x + j[0]][2] += dp[y][x][k]
            
    sum_x_y += 1
                
print(sum(dp[-1][-1]))

# 1. 어떠한 방식으로 해당 위치까지 왔는지 저장
# 2. 해당 위치의 좌표가 (a, b)라고 할 때, a + b 값이 같은 것끼리 먼저 연산 ex) (3, 1), (2, 2), (3, 1)

# [
# [[0, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0]], 
# [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 1], [1, 0, 1], [2, 0, 1]], 
# [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 1, 0], [0, 1, 1], [1, 1, 2]], 
# [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 1, 0], [0, 2, 1], [1, 3, 2]], 
# [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 1, 0], [0, 3, 1], [1, 5, 3]], 
# [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 1, 0], [0, 4, 1], [1, 8, 4]]
# ]




# =================================================================================================

# 다른 풀이 (시간 초과, dp 사용 안함)

# from collections import deque
# import sys
# input = sys.stdin.readline

# n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]
# cnt = 0

# command = [[(1, 1), (1, 0), (0, 1)], [(1, 1), (1, 0)], [(1, 1),(n, n), (0, 1)]]

# queue = deque([(1, 0, 1)])

# while queue:
#     x, y, cmd = queue.popleft()
    
#     if x == n - 1 and y == n - 1:
#         cnt += 1
#     else:
#         for index, i in enumerate(command[cmd]):
#             if index == 0:
#                 if x + i[0] < n and y + i[1] < n and arr[y + 1][x] + arr[y][x + 1] + arr[y + 1][x + 1] == 0:
#                     queue.append((x + i[0], y + i[1], index))
                        
#             elif x + i[0] < n and y + i[1] < n and arr[y + i[1]][x + i[0]] == 0:
#                     queue.append((x + i[0], y + i[1], index))
        
# print(cnt)             
