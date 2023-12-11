from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    
    answer = 0 
    graph = [[-1] * 102 for i in range(102)]
    
    for r in rectangle:
        x1, y1, x2, y2 = map(lambda x: x*2, r) # 해결이 안되는 경우가 있어서 각 요소에 *2를 해줌
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                if x1 < i < x2 and y1 < j < y2: # 직사 각형 내부 일 때 0으로 표시
                    graph[i][j] = 0 
                elif graph[i][j] != 0: # 내부가 아니고 테두리면 1로 표시
                    graph[i][j] = 1
    

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    q = deque()
    q.append([characterX * 2, characterY * 2]) # 시작점(초기위치) 넣기
    visited = [[1] * 102 for i in range(102)] # 방문하지 않은 곳은 1로 표시
    visited[characterX * 2][characterY * 2] = 0 # 시작 지점은 0
    
    while q:
        x, y = q.popleft()
        if x == itemX*2 and y == itemY*2: # 아이템 있는 위치라면 break
            answer = visited[x][y] // 2
            break
            
        else:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
            
                if graph[nx][ny] == 1 and visited[nx][ny] == 1:
                    q.append([nx, ny])
                    visited[nx][ny] = visited[x][y] + 1 # 거리 누적

    return answer