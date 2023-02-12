# 2부터 시작해서 x 까지 올라감 -> 바텀업 

x = int(input())

d= [0] * 30001 # 결과 저장 / d[i-1]의 값을 소환해서 계산량 줄임 

for i in range(2,x+1):
    print(i)

    d[i] = d[i-1] + 1
    print(f'1. {d[i]}')
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
        print(f'2. {d[i]}')

    if i % 3 == 0:
        d[i] = min(d[i], d[i //3] + 1)
        print(f'3. {d[i]}')

    if i % 5 == 0 :
        d[i] = min(d[i], d[i//5] + 1)
        print(f'5. {d[i]}')

print(d[:x+1])
print(d[x])