from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
queue = deque([1, 2])

if n < 2:
    print(n)
    
else:
    for _ in range(n - 2):
        queue.append((queue[-1] + queue.popleft()) % 15746)
                
    print(queue[-1])
    

'''
dp 문제, 타일이 깔리는 숫자가 1, 1, 2, 3, 5, 8 ... 인 것을 보고
피보나치 수열임을 눈치챔

처음 풀 때에는 메모리 초과가 나왔는데, 값을 저장한 다음 마지막에
나머지를 구했다. 값을 저장하기 전에 먼저 나누고 나머지를 더하는게 
메모리 측면에서 훨씬 절약할 수 있다는 점을 깨달았다.

가장 최근 두 수의 합을 구하는 것이므로 두 수 중에 작은 수는 
popleft()로 빼서 메모리를 절약했다.
''' 