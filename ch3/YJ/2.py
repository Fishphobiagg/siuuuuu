#2 큰 수의 법칙
N, M, K = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
ans_list = []
ans= 0
print(M)
while len(ans_list) != M:
    for i in range(K): # K번동안 가장 큰 수 넣기
        ans_list.append(num[-1])
        if len(ans_list) == M: #for 반복문이 돌 때마다 검증
            break
    ans_list.append(num[-2]) #k만큼 반복문이 돌면 두 번째로 큰 수 한 번 넣기
    if len(ans_list) == M:
        break