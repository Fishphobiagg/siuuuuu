N = int(input())
liquid = list(map(int, input().split()))
liquid.sort()

min_value = liquid[0]+liquid[-1]
left, right, min_value, ans = 0, N-1, liquid[0]+liquid[-1], (0, N-1)
while left < right:
    a = liquid[left]+liquid[right]
    if abs(a) < abs(min_value):
        min_value = a
        ans = (left, right)
    if not a:
        print(liquid[left], liquid[right])
        exit()
    if a > 0:
        right -= 1
    else:
        left += 1
print(liquid[ans[0]], liquid[ans[1]])