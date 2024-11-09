import sys
input = sys.stdin.readline

def comination(n, r):
    comi = [[0 for _ in range(r + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(r + 1):
            if i == j or j == 0:
                comi[i][j] = 1
            else:
                comi[i][j] = comi[i-1][j] + comi[i-1][j-1]
    
    return comi[8][4]

print(comination(8,4))
