import sys
input = sys.stdin.readline

def solution(n, s):
    share = s // n # 몫 구하기
    remain = s % n # 나머지 구하기
    answer = []
    
    if n > s: # n > s 일 경우 0이 존재하게 되므로
        return [-1]
    
    for i in range(n):
        if i < remain:  # (몫 + 1) * 나머지 + 몫 * (n - 나머지) 의 조합일 때, 각 원소의 곱이 가장 크다.
            answer.append(share + 1)
        else:
            answer.append(share)
    
    answer = sorted(answer)
    return answer



# n = int(input())
# s = int(input())
# print(solution(n, s))