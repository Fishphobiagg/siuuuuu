
# N_M_k = list(map(int,input().split())) # [5, 8, 3]    
n,m,k = map(int, input().split())

num_list = list(map(int,input().split())) # [2, 4, 5, 4, 6] 

num_list.sort(reverse=True)
#print(num_list)

# m_try = 0 # 기존에 받아놨던 m을 하나씩 뺴는것도 가능 
# k_try = 0 
# total = 0

# while m_try < N_M_k[1]:


#     for j in range(N_M_k[2]):
#         m_try += 1
#         total += num_list[0]

#     m_try += 1
#     #print(m_try)
#     total += num_list[1]
#     #print(total)

# print(total)

## 다른 방법 2

## ( 1번째로 큰수 * k + 2번째로 큰수 ) * (m // (k+1)) + (1번쨰로 큰수 * (m % (k+1))

## 다른 방법 2의 풀어진 버전 

## (1번째로 큰수) * (k * (m // (k+1) + m % (k+1)) + 2번째로 큰수 * (m // (k+1))

count1 = (k * (m // (k+1))) + (m % (k+1))  
count2 = (m // (k+1))

result = count1 * num_list[0] + count2 * num_list[1]

print(result)