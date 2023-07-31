import sys
input = sys.stdin.readline

def dfs(n, cnt, tst):
    if n == C:
        if len(tst) == L and cnt >= 1 and L - cnt >= 2:
            ans.append(tst)
        return

    dfs(n+1, cnt + tbl[ord(alphabet[n])], tst + alphabet[n])
    dfs(n+1, cnt, tst)
    
L, C = map(int, input().split())
alphabet = sorted(list(input().split()))

# Lookup table(모음인 경우 1, 그 외 0이 저장되어 있는...)
tbl = [0]*128
for ch in "aeiou":
    tbl[ord(ch)] = 1
    
ans = []
dfs(0, 0, "")
for st in ans:
    print(st)