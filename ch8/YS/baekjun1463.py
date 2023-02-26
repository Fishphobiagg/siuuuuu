num = int(input())
d = [0] * 1000001  # dp테이블 초기화
# 바텀업 방식
for x in range(2, num + 1 ):  # 1은 작업필요가 없고 num 초과할 필요도 없다
    d[x] = d[x-1] + 1  # 일단 1을 더하는 것부터 시작
    if x % 2 == 0:  # 2로 나누어지면
        d[x] = min(d[x], d[x//2] + 1)  # 더 작다면 갱신
    if x % 3 == 0:  # 3으로 나누어지면
        d[x] = min(d[x], d[x//3] + 1)  # 더 작다면 갱신      
print(d[num])
