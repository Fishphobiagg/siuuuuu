import sys
sys.stdin = open("input.txt", "r", encoding='UTF-8')

n = int(input())
k  = list(map(int, input().split()))
d = [0] * (n)
#첫 칸이 d[0] 인덱스 0부터 시작 생각
d[0] = k[0]
d[1] = max(k[0], k[1])


for i in range(2, n):
    #d[i-3]의 값은 d[i-1]에 포함
    d[i] = max(d[i-1], d[i-2]+k[i])

print(d[n-1])
