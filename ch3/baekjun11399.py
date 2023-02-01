people = int(input()) # 사람의 수를 입력받아 정수로 저장
people_list = []
people_list.extend(map(int, input().split())) # Pi를 입력받아 리스트에 int 형식으로 저장하고 그 리스트를 빈 리스트에 저장
people_list.sort() # 오름차순 정렬
ans = 0 
for idx in range(len(people_list)) : # 각 인덱스에 대해 실행 -> 리스트의 0번째 인덱스 값부터 해당 인덱스까지의 합들의 총합을 구한다.
    ans += sum(people_list[:idx+1])
print(ans)
