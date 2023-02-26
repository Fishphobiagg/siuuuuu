# 수 이어가기


'''
N = 첫번째 수
'''

N = int(input())
max_length = []
num = N
for i in range(N, -1, -1): # 두번째 숫자 선택
    num_list = [N, i]
    num = N - i
    while num >=0:
        num_list.append(num)
        num = num_list[len(num_list)-2] - num_list[len(num_list)-1]
    if len(num_list) > len(max_length):
        max_length = num_list
print(len(max_length))
print(*max_length)