n, k = map(int, input().split())

left = 0
right = n // 2 # (row, col)을 자른 횟수가 (2, 8)인 것과 (8, 2)인 것은 같기 때문
isPossible = False

while left <= right:
    row = (left + right) // 2
    col = n - row
    pieces = (row + 1) * (col + 1) # (row + 1) * (col + 1) 조각
    if k == pieces:
        print('YES')
        isPossible = True
        break
    if k > pieces:
        left = row + 1
    else:
        right = row - 1

if not isPossible:
    print('NO')