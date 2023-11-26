from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    tmp = []
    ans = []
    rdx = [1, 0, -1, 0, 1, 1, -1, -1]
    rdy = [0, -1, 0, 1, 1, -1, -1, 1]
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]
    visited = [[1] * 52 for _ in range(52)]

    for i in range(len(rectangle)):
        for j in range(rectangle[i][0], rectangle[i][2] + 1):
            for k in range(rectangle[i][1], rectangle[i][3] + 1):
                tmp.append((j, k))

    start = [0, 0]

    while start:
        ox = start.pop()
        oy = start.pop()

        for dir in range(8):
            if 0 <= ox + rdx[dir] < 52 and 0 <= oy + rdy[dir] < 52 and visited[ox + rdx[dir]][oy + rdy[dir]] == 1:
                if (ox + rdx[dir], oy + rdy[dir]) in tmp:
                    visited[ox + rdx[dir]][oy + rdy[dir]] = 0
                    ans.append((ox + rdx[dir], oy + rdy[dir]))
                else:
                    visited[ox + rdx[dir]][oy + rdy[dir]] = 2
                    start.append(oy + rdy[dir])
                    start.append(ox + rdx[dir])

    queue = deque([(characterX, characterY)])

    while queue:
        x, y = queue.popleft()
        for dir in range(4):
            if (x + dx[dir], y + dy[dir]) == (itemX, itemY) and visited[x + dx[dir]][y + dy[dir]] == 0:
                visited[x + dx[dir]][y + dy[dir]] += visited[x][y] + 1

            elif (x + dx[dir], y + dy[dir]) in ans and visited[x + dx[dir]][y + dy[dir]] == 0:
                visited[x + dx[dir]][y + dy[dir]] += visited[x][y] + 1
                queue.append((x + dx[dir], y + dy[dir]))

    return visited[itemX][itemY]


# rectangle = [[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]]
# characterX = 1
# characterY = 3
# itemX = 7
# itemY = 8
# result = 17

rectangle = [[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]]
characterX = 9
characterY = 7
itemX = 6
itemY = 1
result = 11


print(solution(rectangle, characterX, characterY, itemX, itemY))
