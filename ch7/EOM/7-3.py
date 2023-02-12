N , M = map(int,input().split())
dduck_list = list(map(int,input().split()))

# 이진 탐색으로 H 구하기 
def func(dducks, N, M):
    dduck_list.sort()
    start, end = 0, dducks[-1] # H 값은 최소한 가장 긴 떡 길이보다 작아야함 그래서 end = 가장 긴 떡 길이 
    center = (start + end) // 2
    sum_dduck = 0

    while start <= end:
        
        # 잘린 떡의 총 합 구하기 
        for dduck in dduck_list:
            if dduck > center:
                sum_dduck += dduck - center
        
        # print(sum_dduck)
        
        if sum_dduck > M: # 잘린 떡이 얻어야하는 떡 총 길이보다 크다면 H를 키워야함 
            start = center + 1
            center = (start + end) // 2
            sum_dduck = 0
            print(f'start : {start} end : {end} center : {center}')

        elif sum_dduck < M: # 잘린 떡이 얻어야 하는 떡 총 길이보다 작다면 H를 줄여야함 
            end = center - 1
            center = (start + end) // 2
            sum_dduck = 0
            print(f'start : {start} end : {end} center : {center}')
        else: # 잘린 떡 길이랑 얻어야하는 떡 길이랑 같다면 
            return center # 그 H 값 출력 

    return center # 최선을 다한 H 값 출력
        
print(func(dduck_list, N, M))
    
    
    