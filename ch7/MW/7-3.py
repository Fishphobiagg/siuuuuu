# 떡볶이 떡 만들기

N, M = map(int, input().split())
ricecake = list(map(int, input().split()))
ricecake.sort()
# 높이의 최대값 -> 떡을 최소한으로 잘라야함
# 가격을 최적화하는 방향으로 계속해서 갱신 (극한) -> 최종 길이 or 중간에 최적값 찾으면 그게 최대값
# mid가 절단기의 높이
l = 0
r = ricecake[-1]
def cut_cake(left, right, target):
    while left <= right:
        mid = (left + right) // 2
        ricecake_sum = [i - mid for i in ricecake if i > mid]
        if sum(ricecake_sum) < target:
            right = mid-1
        elif sum(ricecake_sum) > target:
            left = mid + 1
        elif sum(ricecake_sum) == target:
            return mid

print(cut_cake(l,r,M))