

N,K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

for i in range(K):
    A_min = min(A)
    A_min_index = A.index(A_min)
    B_max = max(B)
    B_max_index = B.index(B_max)
    if B_max > A_min:
        A[A_min_index], B[B_max_index] = B_max, A_min

print(A) 
print(B)
print(sum(A)) 