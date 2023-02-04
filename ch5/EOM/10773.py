# 제로

number_of_int = int(input()) # 입력할 정수의 개수 
num_list = [] # 입력된 숫자를 담을 리스트 생성 

for i in range(number_of_int):
    num = int(input()) # 정수 입력 
    if num : # 정수가 0이 아니면 
        num_list.append(num) # 숫자 리스트에 추가 
    else: # 입력된 정수가 0 이면 
        num_list.pop() # 숫자 리스트에서 하나 제거 

print(sum(num_list)) # 숫자 리스트의 합 출력