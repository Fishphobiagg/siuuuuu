# 수 찾기
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))


# A_set = set(A)
# for num in B:
#     if num in A:
#         print(1)
#     else:
#         print(0)

# 이진탐색
l = 0
r = N-1
A.sort()
def binary_search(left, right, target):
    exist = False
    while left <= right:
        mid = (left+right)//2
        if A[mid] == target:
            exist == True
            break
        elif A[mid] < target:
            right = A[mid]-1
        else:
            left = A[mid]+1
    return exist
for i in B:
    if binary_search(l, r, i):
        print(1)
    else:
        print(0)
