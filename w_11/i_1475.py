num = input()
num_dic = {
    '0': 0, '1': 0, '2': 0, '3': 0, '4': 0,
    '5': 0, '6': 0, '7': 0, '8': 0, '9': 0,
    }

cnt = 0
for i in num:
    if i == '6' or i == '9':
        cnt += 1
        if cnt % 2 == 1:
            num_dic['6'] += 1
        else:
            num_dic['9'] += 1
    
    else:
        num_dic[i] += 1
        
print(max(num_dic.values()))