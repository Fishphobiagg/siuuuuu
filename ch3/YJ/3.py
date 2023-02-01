#3 숫자카드게임
n, m = map(int,input().split())
ans = []
for i in range(n): #열의 수 만큼 반복
    cards = list(map(int, input().split()))
    ans.append(min(cards))
print(max(ans))