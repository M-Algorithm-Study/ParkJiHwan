def solution(n, computers):
    answer = 0
    visited = [0 for _ in range(n)]
        
    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            answer += 1
            
        for j in range(n):
            if i == j:
                pass
            elif computers[i][j] == 1:
                computers[i][j] = 0
                stack = []
                stack.append(j)
                
                while stack:
                    m = stack.pop()
                    if visited[m] == 0:
                        visited[m] = 1
                    
                    for k in range(n):
                        if m == k:
                            pass
                        elif computers[m][k] == 1:
                            computers[m][k] = 0
                            stack.append(k)
    return answer