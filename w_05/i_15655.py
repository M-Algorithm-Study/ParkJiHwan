from itertools import combinations

n, m = map(int, input().split())
num_list = list(map(int, input().split()))
combi = list(combinations(num_list, m))
combi = sorted(combi)
arr = []

for x in range(len(combi)):
    arr.append(sorted(combi[x]))

arr = sorted(arr)

for y in range(len(arr)):
    print(*arr[y])