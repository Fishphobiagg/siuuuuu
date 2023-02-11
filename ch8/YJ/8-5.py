import sys
sys.stdin = open("input.txt", "r", encoding='UTF-8')

#인풋 받고 화폐 가치는 리스트로 정리
n, m = map(int, input().split())
money_list = []
for _ in range(n):
    money_list.append(int(input()))
#print(money_list)

d = [99999] * (m+1)
d[0] = 0
#확인할 돈(m)만큼 반복문을 돌린다.
for j in money_list:
    for i in range(money_list[0], m+1):
        if (i - j != 99999): #남은 돈이 화폐로 거슬러질 수 있는가
            d[i] = min([d[i], d[i-j]+1])


#답을 내보자
if d[m] == 99999:
    print(-1)
else:
    print(d[m])