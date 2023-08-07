import sys
input = sys.stdin.readline

u, n = map(int, input().split()) # 금액의 상한, 경매에 참여한 횟수

res_lst = []
res_cnt = [0]*u

for _ in range(n):
    s, p = input().split() # 사람 이름, 사람이 제시한 가격    
    res_lst.append([s, p])
    res_cnt[int(p)-1] += 1

min_num = n
for i in range(len(res_cnt)):
    if res_cnt[i] != 0:
        if min_num > res_cnt[i]:
            min_num = res_cnt[i]
            
k = res_cnt.index(min_num)+1

for res in res_lst:
    if int(res[1]) == k:
        print(*res)
        break