for _ in range(int(input())):
    N = int(input())
    li = set(map(int, input().split()))
    M = int(input())
    li_2 = list(map(int, input().split()))
    for n in li_2:
        print(1 if n in li else 0)