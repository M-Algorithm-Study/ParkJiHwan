import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    student_lst = list(map(int, input().split()))
    student_lst = sorted(student_lst[1:])
    
    tmp = student_lst[0]
    largest_gap = 0
    for k in range(1, len(student_lst)):
        if student_lst[k] - tmp > largest_gap:
            largest_gap = student_lst[k] - tmp
        tmp = student_lst[k]
        
    print('Class', i + 1)
    print('Max ', max(student_lst),', ', 'Min ', min(student_lst), ', ', 'Largest gap ', largest_gap, sep='')
    