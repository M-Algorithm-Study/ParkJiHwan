import sys

input = sys.stdin.readline

n = int(input())
data_lst = []

for _ in range(n):
    country, num, score = map(int, input().split())
    data_lst.append([country, num, score])

data_lst = sorted(data_lst, key=lambda x: x[2], reverse=True)

print(data_lst[0][0], data_lst[0][1])
print(data_lst[1][0], data_lst[1][1])

i = 2
while True:
    if data_lst[0][0] == data_lst[i][0]:
        i += 1
    
    else:
        print(data_lst[i][0], data_lst[i][1])
        break   