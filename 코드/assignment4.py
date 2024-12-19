import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000) # n의 제한 조건이 1000000이여서 제한을 풀어두기 위함, 파이썬의 기본 제한은 1000

n, m = map(int, input().split())

parent = [i for i in range(n + 1)] #초기에는 자기 자신이 부모인 상태

def find(i):
    if parent[i] != i:
        parent[i] = find(parent[i]) # 경로 압축
    return parent[i]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for r in range(m):
    o, a, b = map(int, input().split())

    if o == 0: # 합집합 연산
        if a == b:
            continue
        union(a, b)
    else: # 같은 집합인지 확인
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")