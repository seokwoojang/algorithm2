import sys
input = sys.stdin.readline

#최대한 많은 부서에게 물품을 지원
#전체 부서 수는 100개 이하
#부서 당 쵀대 금은 100000 이하
#전체 예산은 10000000 이하


#-------------------------------------------------------------

# maxinum = -1e9

# def maxBudgetDept(d, budget, cnt):
#     global maxinum
#     if budget - d[0] == 0:
#         cnt += 1
#         maxinum = max(maxinum, cnt)
#         return
    
#     if budget - d[0] < 0:
#         maxinum = max(maxinum, cnt)
#         return

#     for i in range(len(d)):
#         maxBudgetDept(d[:i] + d[i+1:], budget - d[i], cnt + 1)
    
# print(maxBudgetDept([2,3,5,7],10, 0)) #오름차순으로 정렬해야함

#-------------------------------------------------------------

# #스택
# cnt = 0
# def maxBudgetDept(d, budget):
#     global cnt
#     if budget - d[-1] == 0:
#         cnt += 1
#         print(cnt)
#         return
    
#     if budget - d[-1] < 0:
#         print(cnt)
#         return 
    
#     budget = budget - d.pop()
#     cnt += 1
#     maxBudgetDept(d, budget)

# maxBudgetDept([7,5,3,2],10) #내림차순 정렬로 들어가야됨


#-------------------------------------------------------------
# #단순히 배열
# def maxBudgetDept(d, budget):
#     cnt = 0

#     for i in range(len(d)):
#         if budget - d[0] == 0:
#             cnt += 1
#             print(cnt)
#             return
    
#         if budget - d[0] < 0:
#             print(cnt)
#             return 
        
#         budget -= d[i]
#         cnt += 1

# maxBudgetDept([2,3,5,7],10) #오름차순으로 정렬해야됨

#------------------------------------------------------
# 정답 코드

def maxBudgetDept(d, budget):
    d.sort()
    count = 0

    for amount in d:
        if amount > budget:
            break
        budget -= amount
        count += 1
    
    return count if budget >=0 else count - 1


print(maxBudgetDept([1,3,2,5,4], 9))
print(maxBudgetDept([2,2,3,3], 10))