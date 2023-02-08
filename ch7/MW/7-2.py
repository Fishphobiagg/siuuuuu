# 부품 찾기

N = int(input())
parts = list(map(int, input().split()))
M = int(input())
client_parts = list(map(int, input().split()))

parts.sort()

l = 0
r = N-1

def binary_search(left, right, target):
    if left > right:
        return 'no'
    mid = (left+right)//2
    if parts[mid] == target:
        return 'yes'
    elif parts[mid] > target:
        binary_search(mid+1, right, target)
    else:
        binary_search(left, mid-1, target)

for i in client_parts:
    print(binary_search(l, r, i), end=' ')