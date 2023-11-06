import sys
input = sys.stdin.readline

def round2(num): # 사사오입
    return int(num) + (1 if num - int(num) >= 0.5 else 0)

n = int(input())
cut = n * 0.15
cut_line = round2(cut)

lst = [int(input()) for _ in range(n)]
lst = sorted(lst)

if n == 0:
    print(0)
else:
    print(round2(sum(lst[cut_line:n - cut_line])/(n - 2 * cut_line)))
    