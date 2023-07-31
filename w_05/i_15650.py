from itertools import combinations

n, m = map(int, input().split())
num_list = [i for i in range(1, n+1)]
combi = list(combinations(num_list, m))

for x in range(len(combi)):
    print(*combi[x])