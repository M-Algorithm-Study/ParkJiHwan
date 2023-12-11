ans = []
for i in range(1, 150):
    for j in range(1, 151):
        if i < j:
            ans.append([i**2 + j**2, i, j])

ans = sorted(ans)

while True:
    h, w = map(int, input().split())

    if h == 0 and w == 0:
        break
    
    for k in range(len(ans)):
        if h ** 2 + w ** 2 in ans[k] and h in ans[k] and w in ans[k]:
            print(ans[k + 1][1], ans[k + 1][2])