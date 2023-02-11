import sys
sys.stdin = open("input.txt", "r", encoding='UTF-8')

x = int(input())

d = [0] * (x+1)

for i in range(2, x+1):
    #print(i)
    d[i] = d[i-1] + 1

#26을 하더라도 미리 하나를 빼서 25로 나누는 경우와 26 그대로 2로 나누는 경우를 모두 비교
    if i % 2 == 0:
        #예를들어 i가 10이라면 그 이전에 d[10]에 저장된 값과 d[5]의 값에서 1을 더한(지금 10을 2로 나누면
        #5가 되기 때문) 값 중에서 가장 작은 값을 최소로 둔다. (결과적으로 작은 값을 찾아야하기 때문)
        d[i] = min(d[i], d[i//2] + 1) #
        print(f'2로 나눔 {d[i]}')
        print(f'd[i] {d[i]}')

    if i % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1)

    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)
        print(f'5로 나눔 {d[i]}')
        print(f'd[i] {d[i]}')

print(d[x])
#print(d)

