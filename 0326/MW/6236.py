# 용돈 관리
import sys
input = sys.stdin.readline

N, M = map(int, input().split())


dragon_mountain = [int(input()) for _ in range(N)]
start, end = max(dragon_mountain), sum(dragon_mountain)+1
result = 0

while start < end:
    mid = (start+end)//2

    cnt = 1
    money = mid
    for i in dragon_mountain:
        if money - i < 0:
            money = mid-i
            cnt += 1
        else:
            money -= i
    if cnt <= M: # 돈을 적게 인출한 경우 ->
        result = mid
        end = mid
    else:
        start = mid + 1
print(result)