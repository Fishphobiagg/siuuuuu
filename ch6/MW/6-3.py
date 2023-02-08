# 성적이 낮은 학생 출력하기

N = int(input())
student_dict = {}
for i in range(N):
    name, score = map(str, input().split())
    student_dict[name] = int(score)

student_dict = sorted(student_dict.items(), key=lambda x:x[1])
for i in student_dict:
    print(i[0], end=' ')