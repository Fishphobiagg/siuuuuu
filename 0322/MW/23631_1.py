# 진좌반뛰
import sys
'''
값이 커질 경우 소수점에서 오류가 나는거같음

'''
input = sys.stdin.readline

for _ in range(int(input())):
    N, K = map(int,input().split())
    start, end = 0, 5000
    result = 0
    # mid가 총 뛴 횟수
    while start < end:
        mid = (start+end)//2
        if ((K+mid*K)/2)*mid < N:
            start = mid+1
        elif ((K+mid*K)/2)*mid >= N:
            end = mid
            result = mid
        if start >= end:
            result = start
    left = (((2*K+(result//2-1)*2*K)+2*K)/2)*(result//2)
    right = (((K+((result // 2 + result % 2)-1)*2*K)+K)/2)*(result // 2 + result % 2)
    total = right - left
    if result%2: # 오른쪽으로 뛰고 끝
        if ((result+result*K)/2)*result == N-1: # 딱 맞아 떨어질때 방향전환
            print(int(total), 'L')
            continue
        print(int(total-(left+right-(N-1))), 'R')
    else: # 왼쪽으로 뛰고 끝
        if ((result + result * K) / 2) * result == N - 1:
            print(int(total), 'R')
            continue
        print(int(total+(left+right-(N-1))), 'L')