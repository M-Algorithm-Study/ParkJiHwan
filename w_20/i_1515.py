import sys
input = sys.stdin.readline

num_list = input()
n = 1
j = 0

while j != len(num_list) - 1:
    n = str(n)
    for i in range(len(n)):
        if num_list[j] == n[i]:
            j += 1
            if j == len(num_list) - 1:
                break

    n = int(n)    
    n += 1

print(n - 1)