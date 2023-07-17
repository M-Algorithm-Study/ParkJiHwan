n, m = map(int, input().split())
j = int(input())
total = 0

s = 1
e = m
for i in range(j):
    apple = int(input())
    if s <= apple <= e:
        continue
    elif apple < s:
        total += s - apple
        s = apple
        e = s + m - 1
    else:
        total += apple - e
        s = s + apple - e
        e = apple
        
print(total)