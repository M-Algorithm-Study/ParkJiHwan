import sys
input = sys.stdin.readline

def dfs(n, cnt, tst):
    # print(tst)
    if n == C:
        if len(tst) == L and cnt >= 1 and L - cnt >= 2: # 정해진 길이, 최소 1개의 모음, 최소 2개의 자음
            ans.append(tst)
        return

    dfs(n+1, cnt + tbl[ord(alphabet[n])], tst + alphabet[n]) # 포함하는 경우
    dfs(n+1, cnt, tst) # 포함하지 않는 경우
    
L, C = map(int, input().split())
alphabet = sorted(input().split())

# Lookup table(모음인 경우 1, 그 외 0이 저장되어 있는...)
tbl = [0]*128
for ch in "aeiou":
    tbl[ord(ch)] = 1
# print(tbl)

ans = []
dfs(0, 0, "")
for st in ans:
    print(st)


# print(tst)
# a
# ac
# aci
# acis
# acist
# acistw
# acist
# acis
# acisw
# acis
# aci
# acit
# acitw
# acit
# aci
# aciw
# aci
# ac
# acs
# acst
# acstw
# acst
# acs
# acsw
# acs
# ac
# act
# actw
# act
# ac
# acw
# ac
# a
# ai
# ais
# aist
# aistw
# aist
# ais
# aisw
# ais
# ai
# ait
# aitw
# ait
# ai
# aiw
# ai
# a
# as
# ast
# astw
# ast
# as
# asw
# as
# a
# at
# atw
# at
# a
# aw
# a

# c
# ci
# cis
# cist
# cistw
# cist
# cis
# cisw
# cis
# ci
# cit
# citw
# cit
# ci
# ciw
# ci
# c
# cs
# cst
# cstw
# cst
# cs
# csw
# cs
# c
# ct
# ctw
# ct
# c
# cw
# c

# i
# is
# ist
# istw
# ist
# is
# isw
# is
# i
# it
# itw
# it
# i
# iw
# i

# s
# st
# stw
# st
# s
# sw
# s

# t
# tw
# t

# w


# print(tbl)  
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
# 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
# 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 
# 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]