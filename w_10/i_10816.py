import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
card_list = list(map(int, input().split()))

M = int(input())
check_list = list(map(int, input().split()))

card_dict = Counter(card_list)

for j in range(M):
    if check_list[j] in card_dict:
        print(card_dict[check_list[j]], end=' ')
    else:
        print(0, end=' ')