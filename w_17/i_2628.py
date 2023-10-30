import sys
input = sys.stdin.readline

a, b = map(int, input().split())
n = int(input())
lst_x = [0, a]
lst_y = [0, b]

for _ in range(n):
    command, num = map(int, input().split())

    if command == 0:
        lst_y.append(num) # 가로로 자르는 점선: y를 자름
    else:
        lst_x.append(num)

lst_x = sorted(lst_x)
lst_y = sorted(lst_y)

max_x = 0
max_y = 0

for i in range(len(lst_x) - 1):
    max_x = max(max_x, lst_x[i+1] - lst_x[i])

for i in range(len(lst_y) - 1):
    max_y = max(max_y, lst_y[i+1] - lst_y[i])

print(max_x*max_y)