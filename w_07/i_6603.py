from itertools import combinations
import sys
input = sys.stdin.readline

while True:
    num_lst = list(map(int, input().split()))
    if num_lst[0] == 0:
        break
    
    combi = list(combinations(num_lst[1:], 6))
    for line in combi:
        for num in line:
            print(num, end=' ')
        
        print()
    
    print(' ')