import sys
input = sys.stdin.readline

n, s = map(int, input().split())

num_lst = list(map(int, input().split()))

front = 0
back = 1
res = sum(num_lst[front:back])
ans = []

while back <= n:
    if s <= res:
        ans.append(back - front)
        res -= num_lst[front]
        front += 1
        
    elif back == n:
        break
    
    else:
        res += num_lst[back]
        back += 1

if ans != []:
    print(min(ans))
else:
    print(0)          