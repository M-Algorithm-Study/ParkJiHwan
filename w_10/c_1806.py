import sys
input = sys.stdin.readline

n, s = map(int, input().split())

num_lst = list(map(int, input().split()))

front = 0
back = 1
res_sum = sum(num_lst[front:back])
ans_lst = []

while back <= n: # n을 넘었을 때 종료
    if s <= res_sum:
        ans_lst.append(back - front)
        res_sum -= num_lst[front]
        front += 1
        
    elif back == n: # n일 때 문제가 생기므로 n일 때 종료
        break
    
    else:
        res_sum += num_lst[back]
        back += 1

if ans_lst != []:
    print(min(ans_lst))
else:
    print(0)       