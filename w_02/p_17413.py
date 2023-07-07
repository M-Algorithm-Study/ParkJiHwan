from collections import deque
import sys

input = sys.stdin.readline

words = deque(input().rstrip().split(' '))
cnt = 0
ans = []
tmp = deque([])

for word in words:
    for w in word:
        if w == '<':
            cnt += 1
            if tmp:   
                for T in tmp:             
                    ans.append(T)
                tmp.clear()
        
        if cnt % 2 == 1:
            ans.append(w)
        else:
            tmp.appendleft(w)
        
        if w == '>':
            cnt += 1
        
    if tmp:   
        for T in tmp:             
            ans.append(T)
        tmp.clear()
    ans.append(' ')

print(''.join(ans))
