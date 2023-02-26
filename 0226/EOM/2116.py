# 주사위 쌓기 

'''
https://www.acmicpc.net/problem/2116

서로 붙어있는 두 개의 주사위에서 붙어있는 면들의 숫자가 같아야함 

이 규칙을 통해 만들어진 사각기둥 한면의 최대값 출력 

A(0) 의 맞은편 : F(5)
B(1) : D(3)
C(2) : E(4) 

바닥주사위의 바닥이 어디냐에 따라 전체 주사위의 바닥-위가 정해짐
 
'''

def func(n):
    '''
    param
    n : 시작 인덱스 
    '''
    global max_sum
    max_sum_now = 0

    for i in range(N): # 주사위 번호 
        # 현재 주사위 옆면의 최댓값 더하기 
        up_index = rev[n] # 윗면 인덱스 
        # 옆면의 최댓값구하기 
        max_now = 0 # 초기값 
        for index in range(6):
            if not index in (n, up_index): # 옆면이면 
                if dices[i][index] > max_now: # 현재 최댓값보다 현재 옆면이 크면 
                    max_now = dices[i][index] # 현재 옆면을 최댓값으로 
        # 옆면의 최댓값을 더해주기 
        max_sum_now += max_now
        # print(max_sum_now)
        if i != N-1: # 마지막 주사위가 아니면 
            up = dices[i][rev[n]] # 주사위 윗면 번호  
            n = dices[i+1].index(up) # 다음 주사위 아랫면 인덱스  
    
    if max_sum_now > max_sum: # 현재 최댓값이 최댓값보다 크면 
        max_sum = max_sum_now

# 주사위의 개수
N = int(input())
# 주사위의 종류가 주사위 번호 순서대로 입력 
dices = [list(map(int,input().split())) for _ in range(N)]
# print(dices)
# 맞은편 정보 리스트 (인덱스가 면의 번호 A~F == 0~5)
rev = [5,3,4,1,2,0]
max_sum = 0
for start in range(6):
    func(start)
print(max_sum)



        

        
        





