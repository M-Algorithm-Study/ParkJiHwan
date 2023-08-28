import sys

input = sys.stdin.readline

n = int(input())
cnt_lst = []
name_lst = []
total = 0

for i in range(n):
    pokemon = input()
    need_candy, have_candy = map(int, input().split())
    
    cnt = 0
    while have_candy >= need_candy:
        have_candy -= (need_candy - 2)
        cnt += 1
        total += 1
        
        cnt_lst.append(cnt)
        name_lst.append(pokemon)


print(total)
print(name_lst[cnt_lst.index(max(cnt_lst))])