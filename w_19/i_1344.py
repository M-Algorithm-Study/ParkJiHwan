prime = [2, 3, 5, 7, 11, 13, 17, 19]

a_per = int(input())
b_per = int(input()) 

lst = [0] * 19
for i in range(19):
    tmp = 1  
    for j in range(18, 18 - i, -1):
        tmp *= j
        tmp //= 19 - j

    lst[i] = tmp

dp_a = [[] for _ in range(19)]
dp_b = [[] for _ in range(19)]
for k in range(19):
    dp_a[k] = (a_per/100) ** k * ((100 - a_per)/100) ** (18 - k)
    dp_b[k] = (b_per/100) ** k * ((100 - b_per)/100) ** (18 - k)
    
total_a = 0
total_b = 0
for l in range(19):
    if l not in prime:
        total_a += dp_a[l] * lst[l]
        total_b += dp_b[l] * lst[l]

print(1 - (total_a * total_b))