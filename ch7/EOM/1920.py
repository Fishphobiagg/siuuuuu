def Jin_Lee(num_list, N, i):
    start, end = 0, N-1
    
    while start <= end:
        
        # print(f'start : {start} end : {end}')
        center = (start + end) // 2
        # print(f'center는 {center}')
        if num_list[center] > i :
            end = center - 1
            
        elif num_list[center] < i:
            start = center + 1
            
        else:
            return 1
 
    return 0
    

N = int(input())
num_list = list(map(int,input().split()))
num_list.sort()
M = int(input())
find_me = list(map(int,input().split()))


for i in find_me:
    # print(f' i 는 {i}')
    print(Jin_Lee(num_list, N, i))