N, K = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

for i in range(K):
    if A[i] < B[-i-1]:
        A[i] = B[-i-1]
    else:
        break

print(sum(A))