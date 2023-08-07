# n, m = map(int, input().split())

# stack = []
# def f():
#   if len(stack) == m:
#     print(*stack)
#     return

#   for i in range(1, n + 1):
#     if i in stack:
#       continue
#     stack.append(i)
#     f()
#     stack.pop()
    
# f()

#=============================
def dfs(n, lst):
    if n == M:
        ans.append(lst)
        return
    
    for j in range(1, N+1):
        if v[j] == 0:
            v[j] = 1
            dfs(n+1, lst + [j])
            v[j] = 0       

N, M = map(int, input().split())
ans = []
v = [0] * (N+1)

dfs(0, [])
for lst in ans:
    print(*lst)