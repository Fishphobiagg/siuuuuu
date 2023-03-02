# 랜선 자르기

K, N = map(int, input().split())
stick = [int(input()) for i in range(K)]
result = []
def binary(left, right):
    st = 0
    if left > right:
        return
    for i in stick:
        st += i // ((left+right)//2)
    if st >= N: # 덜 쪼개야하는 경우, 더 큰 값 찾기위해 가능한 값 찾아도 계속 진행
        result.append((left+right)//2)
        binary((left+right)//2+1, right)
    elif st < N: # 더 쪼개야 하는 경우
        binary(left, (left+right)//2-1)
binary(1, max(stick))
print(max(result))