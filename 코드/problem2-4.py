# import sys
# input = sys.stdin.readline

# n, k = map(int,input().split())

# a = []
# for i in range(1,n + 1):
#     a.append(i)

# index = 0
# for i in range(n):
#     index = (index + k - 1) % len(a) 
#     print(a[index],end=" ")
#     a.remove(a[index])

#---------------------------------------------

from collections import deque

def solution4(n,k):
    answer = []
    q = deque()

    for i in range(1, n + 1):
        q.append(i)

    while len(q) > 1:
        for i in range(k - 1):
            q.append(q.popleft())
        answer.append(q.popleft())
    
    answer.append(q.popleft())

    return answer

print(solution4(5,2))