import sys
input = sys.stdin.readline

n = int(input())
cnt = 0 # 연산 횟수
ans = [[n]]

while 1 not in ans[cnt]: # 1이 존재하면 종료
    ans.append([]) # 빈 리스트를 추가 (ans[cnt + 1])
    for k in ans[cnt]:
        if k % 3 == 0:
            ans[cnt + 1].append(k // 3)
            
        if k % 2 == 0:
            ans[cnt + 1].append(k // 2)
            
        ans[cnt + 1].append(k - 1)
        
    cnt += 1
    
# print(ans) # [[10], [5, 9], [4, 3, 8], [2, 3, 1, 2, 4, 7]]
print(cnt)