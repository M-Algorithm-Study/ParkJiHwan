from collections import deque

n = int(input())
lst = deque(map(int, input().split())) # 줄 서있는 상태
check_lst = [num for num in range(n, 0, -1)] # 5, 4, 3, 2, 1
left_lst = [] # 잠깐 피해있는 공간

while lst:
    if check_lst[-1] == lst[0]:
        lst.popleft()
        check_lst.pop()
    
    elif left_lst:
        if check_lst[-1] == left_lst[-1]:
            left_lst.pop()
            check_lst.pop()
    
        else:
            left_lst.append(lst.popleft())
            
    else:
        left_lst.append(lst.popleft())

while check_lst:
    if check_lst[-1] == left_lst[-1]:
        left_lst.pop()
        check_lst.pop()

    else:
        break
        
if left_lst:
    print('Sad')
else:
    print('Nice')