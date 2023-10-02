import sys
input = sys.stdin.readline

S = list(input().rstrip())
T = list(input().rstrip())

switch = False
while T: # T에서 뺀 결과가 S가 되는지
    if T[-1] == 'A': # A일 경우에는 그냥 빼고
        T.pop()
        
    elif T[-1] == 'B': # B일 경우에는 빼고 뒤집음
        T.pop()
        T.reverse()
        
    if S == T: # 같아질 경우
        switch = True # True로 표시한 후 break
        break
    
if switch:
    print(1)
else:
    print(0)