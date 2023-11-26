import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
q = deque(enumerate(map(int, input().split()))) # deque로 받아서 순서와 함께 적기 
ans = []

while q:
    idx, paper = q.popleft()
    ans.append(idx + 1)

    if paper > 0:
        q.rotate(-(paper - 1))
    elif paper < 0:
        q.rotate(-paper)
    
print(' '.join(map(str, ans))) # 하나씩 꺼내서 공백을 두고 연결