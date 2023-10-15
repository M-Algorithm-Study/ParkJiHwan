import sys
input = sys.stdin.readline

n = input().strip()
cnt = 0

while len(n) > 1:
    n = list(map(int, list(n))) # list(map(int, list(n)))
    n = str(sum(n))

    cnt += 1

print(cnt)

if int(n) in [3, 6, 9]:
    print('YES')

else:
    print('NO')