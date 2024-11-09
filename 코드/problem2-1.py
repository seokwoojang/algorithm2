import sys
input = sys.stdin.readline

n = int(input())

left = 1
right = 1
s = 0
answer = 0

while True:
    if s < n:
        if right > n:
            break
        s += right
        right += 1
    elif s == n:
        answer += 1
        s -= left
        left += 1
    else:
        s -= left
        left += 1
        
print(answer)