import sys
input = sys.stdin.readline

a_words = input().rstrip()
b_words = input().rstrip()

a_split = [i for i in a_words]
b_split = [j for j in b_words]
cnt = 0

while a_split and b_split:
    a = a_split.pop()
    for b in range(len(b_split)):
        if a == b_split[b]:
            del b_split[b]
            cnt += 2
            break

print(len(a_words) + len(b_words) - cnt)

#============================================================================

a, b = input(), input()
for c in a:
    if c in b:
        a = a.replace(c, "", 1)
        b = b.replace(c, "", 1)
print(len(a) + len(b))
