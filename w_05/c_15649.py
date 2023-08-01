from itertools import permutations

n, m = map(int, input().split())
num_list = [i for i in range(1, n+1)]
permu = list(permutations(num_list, m))

for x in range(len(permu)):
    print(*permu[x])
    
# permutations(순열): (nPr) n! / (n-r)!
# combinations(조합): (nCr) n! / r! * (n-r)!
# product(카다시안 곱): n ^ r
# combinations_with_replacement(중복 조합): (nHr) (n+r-1)Cr

# 예제 입력 2 
# 4 2
# 예제 출력 2 
# 1 2
# 1 3
# 1 4
# 2 1
# 2 3
# 2 4
# 3 1
# 3 2
# 3 4
# 4 1
# 4 2
# 4 3