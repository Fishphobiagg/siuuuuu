#숫자 카드 게임

N, M = map(int,input().split())
max_num = 0
for i in range(N):
    minimum_num = min(list(map(int, input().split())))
    if minimum_num >= max_num:
        max_num = minimum_num
    
print(max_num)