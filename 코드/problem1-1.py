
def maxBudgetDept(d, budget):
    answer = 0

    for i in range(len(d)):
        for j in range(len(d)):
            if d[i] < d[j]:
                temp = d[i]
                d[i] = d[j]
                d[j] = temp

    for i in range(len(d)):
        if budget - d[i] >= 0:
            answer += 1
            budget -= d[i]

    return answer


print(maxBudgetDept([1,3,2,5,4], 9))
print(maxBudgetDept([2,2,3,3], 10))