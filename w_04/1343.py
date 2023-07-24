import sys
input = sys.stdin.readline

word_list = list(input().rstrip().split('.'))
ans = []
err = 0

for word in word_list:
    if len(word) % 4 == 0:
        ans.append(len(word)*'A')
    elif len(word) % 4 == 2:
        ans.append((len(word) - 2)*'A' + 'BB')
    else:
        err += 1
        break

if err == 0:
    for line in range(len(ans)):
        if ans[line] == '':
            ans[line] = '.'

    for i in range(len(ans)-1):
        if ans[i] == '.':
            print(ans[i], end='')
        else:
            print(ans[i], end='.')
    
    if ans[len(ans)-1] != '.':
        print(ans[len(ans)-1])
      
else:
    print(-1)