# 위에서 아래로

N = int(input())
num_list = []


def quick_sort(num):
    if len(num) <= 1:
        return num
    pivot = num[0]
    tail = num[1:]
    left = [n for n in tail if n <= pivot]
    right = [n for n in tail if n > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)


for i in range(N):
    num_list.append(int(input()))

a = quick_sort(num_list)
a = a[::-1]
print(a)
