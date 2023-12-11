def solution(N, number):
    if N == number:
        return 1

    # 동적 프로그래밍을 위한 집합 배열 초기화
    # 각 집합은 해당 횟수만큼 N을 사용하여 만들 수 있는 숫자들을 포함
    dp = [set() for _ in range(9)]
    for i in range(1, 9):
        dp[i].add(int(str(N) * i)) # 5, 55, 555 같은 예외 숫자 처리

    for i in range(1, 9):
        for j in range(1, i):
            for a in dp[j]: # 개수를 i개로 맞추기 위함
                for b in dp[i - j]: 
                    dp[i].add(a + b)
                    dp[i].add(a - b)
                    dp[i].add(a * b)
                    if b != 0:
                        dp[i].add(a // b)

        # 원하는 숫자를 만들 수 있는지 확인
        if number in dp[i]:
            return i
        
    return -1  # 원하는 숫자를 8회 안에 만들 수 없는 경우

# 예시 입력에 대한 결과 확인
print(solution(5, 12))  # 예제 1