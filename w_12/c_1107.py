import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

err_num_lst = map(int, input().split())
num_lst = []

for i in range(10):
    if i not in err_num_lst:
        num_lst.append(i)
        
# 아직 못 풀음(풀고 있는 중)