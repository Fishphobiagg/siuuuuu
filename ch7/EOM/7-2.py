# 이진탐색 

def func(arr, part, N):
        
        start, end = 0, N - 1
        center = (start + end) // 2
        while start <= end:
            if arr[center] > part:
                end = center - 1
                center = (start + end) // 2
                # print(end, center)
            elif arr[center] < part:
                start = center + 1
                center = (start + end) // 2
                # print(end, center)
            elif arr[center] == part:
                return 'yes'
                
        return 'no'


N = int(input())
arr = list(map(int,input().split()))
arr.sort()
# print(arr)
M = int(input())
parts = list(map(int,input().split()))

for part in parts: # 파트별로 하나 씩 이진 탐색 
    print(func(arr, part, N))

