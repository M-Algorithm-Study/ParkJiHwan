from itertools import permutations

n, m = map(int, input().split())
num_list = list(map(int, input().split()))
permu = set(permutations(num_list, m))
permu = sorted(permu)
for x in range(len(permu)):
    print(*permu[x])