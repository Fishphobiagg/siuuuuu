# 나무 자르기

N, M = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort()

start, end = 0, trees[-1] # 최소값 처리
result = 0
if N == 1:
    print(trees[0]-M)
    exit()
while start < end:
    mid = (start+end)//2
    total = 0
    for i in trees:
        if i <= mid:
            continue
        total += i-mid
    if total < M: # 너무 짧게 자른 경우 절단기 높이 낮추기
        end = mid
    else:
        start = mid+1
        result = mid
print(result)