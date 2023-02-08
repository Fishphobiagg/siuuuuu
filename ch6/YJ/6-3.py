#성적이 낮은 순서로 학생 출력하기
import sys
sys.stdin = open("input.txt", "r", encoding= 'UTF8')

dic = {}
n = int(input())
for _ in range(n):
    a, b = input().split()
    dic[a] = b
#람다로 딕셔너리의 값으로 정렬
dic = sorted(dic.keys(), key = lambda x: x[1], reverse= True)
print(*dic)
