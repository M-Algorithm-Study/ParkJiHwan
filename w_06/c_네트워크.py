def solution(n, computers):
    answer = 0
    visited = [0 for _ in range(n)] # 0 부터 n-1까지 방문 여부 기록
        
    for i in range(n):
        if visited[i] == 0: # 방문하기 이전인 경우 방문 체크하고 answer += 1
            visited[i] = 1
            answer += 1
            
        for j in range(n):
            if i == j: # i와 j가 같을 경우 pass
                pass
            elif computers[i][j] == 1: # i는 겉의 리스트(방문 여부), j는 안의 리스트(연결 여부)
                computers[i][j] = 0
                stack = []
                stack.append(j)
                
                while stack:
                    m = stack.pop()
                    if visited[m] == 0: # 방문하기 이전인 경우 방문 체크
                        visited[m] = 1
                    
                    for k in range(n):
                        if m == k:
                            pass
                        elif computers[m][k] == 1:
                            computers[m][k] = 0
                            stack.append(k)
    return answer