import sys
input = sys.stdin.readline

n, m = map(int, input().split())
address = {}
for _ in range(n):
    site, password = input().rstrip().split(' ')
    address[site] = password
    
for _ in range(m):
    site_name = input().rstrip()
    
    print(address[site_name])