
# def solution(n, a, b):
#     answer = 0

#     while True:
#         if a == b:
#             break
#         else:
#             answer += 1
#             if a % 2 == 1:
#                 a = a // 2 + 1
#             else:
#                 a = a // 2
#             if b % 2 == 1:
#                 b = b // 2 + 1
#             else:
#                 b = b // 2
            
#     return answer

import math

def solution(n, a, b):
    answer = 0

    while a != b:
        a = math.ceil(a/2)
        b = math.ceil(b/2)
        answer += 1

    return answer

print(solution(8,4,7))
