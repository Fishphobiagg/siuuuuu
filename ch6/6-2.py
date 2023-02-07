#위에서 아래로
# import sys
# sys.stdin = open("input.txt", "r")
#정렬 내장함수 이용
n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
    arr.sort(reverse = True)
    #앞에 *을 넣으면 리스트의 내용을 대괄호 없이 출력
print(*arr)

