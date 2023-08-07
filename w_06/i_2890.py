r, c = map(int, input().split())

s = list(input() for _ in range(r))
res = []
order = []

for i in range(r):
    cnt = 0
    for j in s[i]:
        if j == 'S' or j == '.' or j == 'F':
            cnt += 1
        else:
            order.append(j)
            break
    
    if cnt <= c - 4:
        res.append(cnt)

ans = [0]*9
for rank in range(1, 10):
    max_num = -1
    for p in range(len(res)):
        if res[p] > max_num:
            max_num = res[p]

    if max_num >= 0:
        for k in range(9):
            if res[k] == max_num:
                res[k] = -1
                ans[k] = rank

for i in range(1, 10):
    print(ans[order.index(str(i))])