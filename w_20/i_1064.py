from decimal import *
 
def dist(a, b):
    return ((a[0] - b[0]) * (a[0] - b[0]) + (a[1] - b[1]) * (a[1] - b[1])).sqrt()
 
getcontext().prec = 28 # Decimal 모듈의 정밀도를 28로 설정 이것은 계산의 정확도를 높이기 위함
xa, ya, xb, yb, xc, yc = tuple(map(Decimal, input().split())) 
a, b, c = (xa, ya), (xb, yb), (xc, yc)
la, lb, lc = dist(b, c), dist(a, c), dist(a, b) 
 
if (xb-xa)*(yc-ya) == (yb-ya)*(xc-xa): # 이 조건문은 세 점이 직선 위에 있는지 확인, 만약 그렇다면 -1을 출력
    print(-1)
else:
    len_list = [la, lb, lc]
    print((max(len_list) - min(len_list)) * Decimal(2)) # 가장 긴 변의 길이와 가장 짧은 변의 길이의 차이의 두 배를 계산하고 출력