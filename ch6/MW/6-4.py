# 두 배열의 원소 교체

N,K = map(int,input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()
max_index = -1
for i in range(K):
    min = A.remove(A[0])
    max = B[max_index]
    max_index -= 1
    A.append(max)
    print(A, B)
print(sum(A))