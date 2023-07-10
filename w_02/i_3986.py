from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
cnt = 0

for i in range(n):
    words = deque(input().rstrip())
    tmp_list = deque([])
    while words:
        t = words.popleft()
        if tmp_list:
            if tmp_list[0][0] == t: # A == A, B == B
                tmp_list.popleft()
            else:
                tmp_list.appendleft(t)
        else:
            tmp_list.appendleft(t)

            
    if tmp_list:
        pass
    else:
        cnt += 1
                
print(cnt)