import sys
sys.stdin = open("input.txt", "r", encoding= 'UTF8')

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort() #오름차순

start = 0
end = max(arr)

ans = 0
while (start <= end):
    tteok = 0 #잘린 떡 합
    cut = (start + end) // 2 #떡볶이 자르는 선(시작은 중간)
    for x in arr:
        if x > cut: #떡이 선보다 크면 잘라서 합산
            tteok += (x-cut)
    if tteok < m:   #더 잘라봐야하는 경우 (오른쪽)
        end = cut - 1
    else:#최대한 덜 자르는 경우를 찾아봄 (왼쪽)
        ans = cut
        start = cut + 1
print(ans)




