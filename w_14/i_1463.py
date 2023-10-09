import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
ans = [[n]]

while 1 not in ans[cnt]:
    ans.append([])
    for k in ans[cnt]:
        if k % 3 == 0:
            ans[cnt + 1].append(k // 3)
            
        if k % 2 == 0:
            ans[cnt + 1].append(k // 2)
            
        ans[cnt + 1].append(k - 1)
        
    cnt += 1

print(cnt)