import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
ans = [n]

while 1 not in ans:
    for k in ans:
        if k % 3 == 0:
            ans.append(k / 3)
            
        elif k % 2 == 0:
            ans.append(k / 2)
            
        else:
            ans.append(k - 1)
        
        cnt += 1

print(cnt)