import sys
input = sys.stdin.readline

n, m = map(int, input().split())
words_dic = {}
for i in range(n):
    word = input().rstrip()
    
    if len(word) >= m:
        if word in words_dic:
            words_dic[word] += 1
            
        else:
            words_dic[word] = 1

sorted_words_dic = dict(sorted(words_dic.items(), key=lambda item: (-item[1], -len(item[0]), item[0])))
# -item[1]: 자주 나오는 단어, -len(item[0]): 길이가 길수록 앞,  item[0]: 알파벳 사전 순
for key in sorted_words_dic.keys():
    print(key)

'''
예제
6 1
a
cc
bb
ddd
ee
ee
'''

# -item[1] 조건 만족 시: {'ee': 2, 'a': 1, 'bb': 1, 'cc': 1, 'ddd': 1}
# -len(item[0]) 조건 만족 시: {'ee': 2, 'ddd': 1, 'cc': 1, 'bb': 1, 'a': 1}
# item[0] 조건 만족 시: {'ee': 2, 'ddd': 1, 'bb': 1, 'cc': 1, 'a': 1}

