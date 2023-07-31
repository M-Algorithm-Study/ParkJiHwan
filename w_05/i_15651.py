from itertools import product

n, m = map(int, input().split())
num_list = [i for i in range(1, n+1)]
prod = list(product(num_list, repeat = m))

for x in prod:
    print(*x)