from itertools import permutations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num_list = list(map(int, input().split()))

num_list = sorted(num_list)

permu = permutations(num_list, m)
tmp = sorted(list(set(permu)))

for y in tmp:  
    print(*y)


