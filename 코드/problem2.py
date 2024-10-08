import sys
input = sys.stdin.readline

def comination(n, r):
    B = [ [0 for _ in range(r+1)] for _ in range(n+1)]

    for i in range(n+1):
        for j in range(min(i, r) + 1):
            if j == 0 or j == i:
                B[i][j] = 1
            else:
                B[i][j] = B[i-1][j-1] + B[i-1][j]
    
    return B[n][r]

print(comination(8,4))