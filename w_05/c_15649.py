from itertools import permutations

n, m = map(int, input().split())
num_list = [i for i in range(1, n+1)]
permu = list(permutations(num_list, m))

for x in range(len(permu)):
    print(*permu[x])
    
# permutations(순열): (nPr) n! / (n-r)!
# combinations(조합): (nCr) n! / r! * (n-r)!https://www.acmicpc.net/problem/15650