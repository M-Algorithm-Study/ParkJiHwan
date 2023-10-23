import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
sign = list(map(int, input().split()))

maximum = -1e9
minimum = 1e9

def dfs(depth, total, plus, minus, multi, div): # 깊이, 값, 부호 4개
    global maximum, minimum
    if depth == n:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return

    if plus: # 부호가 존재할 경우 케이스를 적용
        dfs(depth + 1, total + num[depth], plus - 1, minus, multi, div) # 깊이 + 1, 값, 해당 부호 - 1
    if minus:
        dfs(depth + 1, total - num[depth], plus, minus - 1, multi, div)
    if multi:
        dfs(depth + 1, total * num[depth], plus, minus, multi - 1, div)
    if div:
        dfs(depth + 1, int(total / num[depth]), plus, minus, multi, div - 1)

dfs(1, num[0], sign[0], sign[1], sign[2], sign[3])

print(maximum)
print(minimum)
