import sys
input = sys.stdin.readline

n = int(input())
lst = [0] * 3 # r, g, b를 선택했을 때 최솟값을 저장할 lst

for _ in range(n):
    r, g, b = map(int, input().split())
    if lst[0] == 0: # 이전 값이 없으므로 r, g, b 값을 lst 에 하나씩 넣어줌
        lst[0] = r
        lst[1] = g
        lst[2] = b
    else:
        red = min(lst[1] + r, lst[2] + r) # lst[0] 줄에는 이전 상태가 lst[1], lst[2]만 올 수 있음        
        green = min(lst[0] + g, lst[2] + g)
        blue = min(lst[0] + b, lst[1] + b)

        lst[0] = red # 임시로 저장해둔 값을 lst에 옮김
        lst[1] = green
        lst[2] = blue
        
print(min(lst))