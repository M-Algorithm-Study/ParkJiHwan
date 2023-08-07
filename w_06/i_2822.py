# score_lst = [int(input()) for _ in range(8)]
# tmp = [ _ for _ in score_lst]
# res = [ _ for _ in score_lst]
# total = sorted(tmp)

# rank_lst = [0]*8
# for rank in range(1, 9):
#     max_score = -1
#     for score in score_lst:
#         if score > max_score:
#             max_score = score

#     for k in range(8):
#         if score_lst[k] == max_score:
#             score_lst[k] = -1
#             rank_lst[k] = rank
            
# score_lst = res
# print(sum(total[3:]))
# print(res)
# print(rank_lst)
# for i in total[::-1]:
#     print(score_lst.index(i) + 1)

#============================================

score = []
for i in range(8):
    score.append(int(input()))
temp = []
answer = 0

for i in range(5):
    answer += max(score)
    temp.append(score.index(max(score)) + 1)
    score[score.index(max(score))] = -1
temp.sort()

print(answer)
print(*temp)