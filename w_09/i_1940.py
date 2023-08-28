import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
num_lst = list(map(int, input().split()))
num_lst = sorted(num_lst)

left = 0
right = len(num_lst) - 1
count = 0

num_lst[left]
num_lst[right]

while left < right:
    sum_num = num_lst[left] + num_lst[right]
    if sum_num < m:
        left  += 1
    
    elif sum_num > m:
        right -= 1
        
    else:
        count += 1
        left += 1
        right -= 1

print(count)   