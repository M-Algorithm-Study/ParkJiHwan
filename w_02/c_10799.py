import sys
input = sys.stdin.readline

stick = list(input())
p = ')'
cnt = 0
total = 0

for i in stick:    
    if i == '(':
        cnt += 1
        
    elif i == ')':
        cnt -= 1
        
    if p == '(' and i == ')':
        total += cnt
    
    elif p == ')' and i == ')':
        total += 1
                
    p = i
     
print(total)

