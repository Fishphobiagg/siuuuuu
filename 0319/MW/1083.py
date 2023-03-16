# 소트
'''
S = 교환 횟수
버블소트 내림차순
'''
N = int(input())
arr = list(map(int, input().split()))
chance = int(input())
end = N-1
while chance and end >= 1:
    for i in range(end):
        if chance:
            chance-=1
            if arr[i] < arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        else:
            print(*arr)
            exit()
    end-=1
