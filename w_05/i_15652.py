from itertools import combinations_with_replacement

n, m = map(int, input().split())
num_list = [i for i in range(1, n+1)]
combi = list(combinations_with_replacement(num_list, m))

for x in combi:
    print(*x)
    
# 예제 입력 2 
# 4 2
# 예제 출력 2 
# 1 1
# 1 2
# 1 3
# 1 4
# 2 2
# 2 3
# 2 4
# 3 3
# 3 4
# 4 4