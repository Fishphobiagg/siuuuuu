num = int(input())
d = [0] * 1000  # 메모이제이션 초기화
# 탑다운 방식
def top_down(x):
    if x == 1:
        return 0
    if d[x] != 0:  # x의 값을 계산한 적이 있을 경우, 호출
        return d[x]
    d[x] = d[x-1] + 1  # x 의 값을 계산한 적이 없을 경우, 최솟값 작성
    if x % 2 == 0:
        d[x] = min(d[x], top_down(x//2)+1)
    if x % 3 == 0:
        d[x] = min(d[x], top_down(x//3)+1)        
    if x % 5 == 0:
        d[x] = min(d[x], top_down(x//5)+1)        
    return d[x]

print(top_down(num))