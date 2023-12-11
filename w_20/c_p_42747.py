# 각 논문의 인용 횟수가 담긴 배열
citations = [7, 8, 9]

def solution(citations):
    # 인용 횟수를 내림차순으로 정렬
    # 이렇게 하면 각 논문이 얻은 인용 횟수를 쉽게 비교할 수 있음
    citations.sort(reverse=True)

    # H-Index를 저장할 변수
    answer = 0

    # 정렬된 인용 횟수에 대해 반복
    # 'i'는 인덱스 (0부터 시작), 'c'는 인용 횟수
    for i, c in enumerate(citations):
        # 현재 위치 (인덱스 + 1)가 인용 횟수 이하인지 확인
        # H-Index는 최대 'i + 1'개의 논문이 각각 'i + 1'회 이상 인용된 것
        if i < c:
            # H-Index를 현재 위치 (인덱스 + 1)로 업데이트
            # 인덱스는 0부터 시작하므로 1을 더함
            answer = i + 1
    
    # 계산된 H-Index 반환
    return answer

# 입력된 인용 횟수로 함수를 호출하고 결과 출력
print(solution(citations))


#================================================================


# citations = [ 1, 2, 3, 3, 3, 4, 5]

# 7편 중 3번 이상 인용된 논문 5편
# 나머지 논문이 3번 이하

# citations = [3, 0, 6, 1, 5]

# def solution_2(citations):
#     answer = 0
#     citations = sorted(citations)
#     n = len(citations)
#     prev_h = citations[0]
#     s_num = 0
#     tmp = 0
    
#     for i, h in enumerate(citations):
#         if prev_h < h:
#             s_num += tmp
#             tmp = 1
#             prev_h = h

#         else:    
#             tmp += 1

#         if h <= n - s_num:
#             answer = h
            
#     return answer

# print(solution_2(citations))