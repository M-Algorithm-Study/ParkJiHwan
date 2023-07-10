# 내 풀이 (2008ms)

from collections import deque

n, k = map(int, input().split())
josephus = deque([i for i in range(1, n+1)])
res = []

while josephus:
    for _ in range(k-1):
        josephus.append(josephus.popleft())

    res.append(josephus.popleft())

print('<', end = '')
for j, num in enumerate(res):
    if j != len(res) - 1:
        print(num, end = ', ')
    else:
        print(num, end = '')
print('>')


#----------------------------------------------------------------
# 다른 사람 풀이 (48ms)
# 실제로 순열을 작동시키지 않고 위치를 구한다음 결과값을 뽑아냄

n, k = map(int, input().split())
josephus = list(range(1, n + 1))
res = []
idx = k - 1

while josephus:
    if idx >= len(josephus):
        idx = idx % len(josephus)
    res.append(josephus.pop(idx))
    idx += k - 1

print("<" + ", ".join(map(str, res)) + ">")