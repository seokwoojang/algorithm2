import sys
input = sys.stdin.readline

n, l = map(int,input().split())
a = list(map(int,input().split()))

for i in range(len(a)):
    minimum = 1e9
    x = i - l + 1
    if x <= -1:
        x = 0
    for j in range(x, i+1):
        minimum = min(minimum, a[j])
    print(minimum, end=" ")
