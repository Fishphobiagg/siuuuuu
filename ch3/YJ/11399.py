#ATM
N = int(input())
time_list = list(map(int, input().split())) #기다리는 시간을 리스트로 받음
time_list.sort() #기다리는 시간을 정렬
#무조건 오름차순으로 정렬하는 것이 최소시간
ans = 0 #답을 받을 변수

for i in range(N): 
    ans += (time_list[i] * (N-i)) #앞에 있을 수록 더 많은 사람에게 영향
print(ans)