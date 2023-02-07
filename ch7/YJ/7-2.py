import sys
sys.stdin = open("input.txt", "r", encoding= 'UTF8')
#set이나 리스트나 상관없는듯
N = int(input())
n_list = list(map(int, input().split()))

M = int(input())
m_list = list(map(int, input().split()))

for i in m_list:
    if i in n_list:
        print('yes', end= ' ')
    else:
        print('no', end= ' ')
