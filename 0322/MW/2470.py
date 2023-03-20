# 두 용액

'''
0에 가까운 특성값 만들기
두 포인터를 두고, 더해가는거..?
두 포인터는 결국 왼쪽 구역과 오른쪽 구역을 돌아다니는거
'''

N = int(input())
liquid = list(map(int, input().split()))
liquid.sort()

if min(liquid) > 0:
    print(liquid[0], liquid[1])
    exit()
elif max(liquid) < 0:
    print(liquid[-2], liquid[-1])
    exit()
left = 0
right = N-1
min_val = abs(liquid[0]+liquid[-1])
ans = (0, N-1)
while right-left > 1:
    if abs(liquid[left+1]+liquid[right]) < abs(liquid[left]+liquid[right]):
        left += 1
        ans = (left+1, right)
    elif abs(liquid[left]+liquid[right-1]) <= abs(liquid[left]+liquid[right]):
        right -=1
        ans = (left, right-1)
    else:
        ans = (left, right)
        break
print(liquid[ans[0]], liquid[ans[1]])