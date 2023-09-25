import sys
input = sys.stdin.readline

n = int(input().strip())
m = int(input().strip())
broken = set()

if m > 0:
    broken = set(map(int, input().split()))

# 해당 채널을 고장난 버튼으로 누를 수 있는지 확인하는 함수
def can_press(channel):
    for ch in str(channel):
        if int(ch) in broken:
            return False
    return True

# 1. +/- 버튼만으로 이동할 수 있는 경우의 수
ans = abs(n - 100)

# 2. 0부터 1,000,000까지의 모든 채널을 확인
for channel in range(1000001):
    if can_press(channel):
        # 채널 번호 누르는 횟수 + 해당 채널에서 n까지 +/- 버튼으로 누르는 횟수
        ans = min(ans, len(str(channel)) + abs(channel - n))

print(ans)