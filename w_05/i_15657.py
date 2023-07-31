from itertools import combinations_with_replacement

n, m = map(int, input().split())
num = list(map(int, input().split()))

answer = list(combinations_with_replacement(num, m))
ans = []
for i in answer:
    ans.append(sorted(i))

ans = sorted(ans)

for j in ans:
    print(*j)