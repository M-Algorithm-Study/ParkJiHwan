import sys

T = int(sys.stdin.readline())

stack = []
for i in range(T):
    n = int(sys.stdin.readline())
    if n == 0:
        stack.pop()
    else:
        stack.append(n)

print(sum(stack))