# def solution(enroll, referral, seller, amount):
#     answer = []
#     enroll_money = {}
#     parent_child = {}

#     for i in range(len(enroll)):
#         enroll_money[enroll[i]] = 0
#         parent_child[enroll[i]] = referral[i]
    
#     def dfs(child, money):
#         parent = parent_child[child]
#         remain_money = money // 10

#         if remain_money >= 1:
#             add_money = money - remain_money
#         else:
#             add_money = money
        
#         if parent != "-" and enroll_money[child] == 0:
#             enroll_money[child] = add_money
#         else:
#             enroll_money[child] += add_money
        
#         if parent == "-":
#             return
        
#         if remain_money > 0:
#             dfs(parent, remain_money)

#     for i in range(len(seller)):
#         dfs(seller[i], amount[i] * 100)
    
#     answer = list(enroll_money.values())

#     return answer



def solution(enroll, referral, seller, amount):
    answer = []
    enroll_money = {}
    parent_child = {}

    for i in range(len(enroll)):
        enroll_money[enroll[i]] = 0
        parent_child[enroll[i]] = referral[i]
    
    for i in range(len(seller)):
        a = amount[i] * 100
        s = seller[i]
        while s != "-" and a > 0:
            enroll_money[s] += a - a // 10
            s = parent_child[s]
            a = a // 10
        
    answer = list(enroll_money.values())
    return answer

enroll1 = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral1 = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller1 = ["young", "john", "tod", "emily", "mary"]
amount1 = [12, 4, 2, 5, 10]
# print(solution(enroll1,referral1,seller1,amount1))
#[360, 958, 108, 0, 450, 18, 180, 1080]


#--------------------------------------------------------------------
enroll2 = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral2 = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller2 = ["sam", "emily", "jaimie", "edward"]
amount2 = [2, 3, 5, 4]

print(solution(enroll2,referral2,seller2,amount2))
#[0, 110, 378, 180, 270, 450, 0, 0]