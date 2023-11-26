import sys
input = sys.stdin.readline

number = 100000
a = [False, False] + [True] * (number - 1) # 0과 1은 제외
primes = [] # 에라토스테네스의 체

for i in range(2, number+1):
  if a[i]:
    primes.append(i)
    for j in range(2 * i, number+1, i):
        a[j] = False

n = int(input().rstrip())
for _ in range(n):
    N = int(input())
    visited = [0] * (number + 1)

    while N > 1:
        for i in primes:
            if N % i == 0:
                N = N // i
                visited[i] += 1
                break
            
    for j in range(len(primes)):
        if visited[primes[j]]:
            print(primes[j], visited[primes[j]])