N = int(input())

stu_info = [input().split() for i in range(N)]
sort_info = sorted(stu_info, key = lambda x : x[1])
print(sort_info) # [['이순신', '77'], ['홍길동', '95']]
for index in sort_info:
    print(index[0], end = ' ') # 이순신 홍길동 