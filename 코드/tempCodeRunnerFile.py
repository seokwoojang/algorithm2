import sys
input = sys.stdin.readline

n, m = map(int, input().split())

parent = [i for i in range(n + 1)]

def find(i):
    root = i
    while root != parent[root]:
        root = parent[root]

    trail = i
    while trail != root:
        lead = parent[trail]
        parent[trail] = root
        trail = lead

    return root

for r in range(m):
    o, a, b = map(int, input().split())

    if o == 0:
        if a == b:
            continue
        parent[b] = a
    else:
        if a == b:
            print("YES")
        else:
            if find(a) == find(b):
                print("YES")
            else:
                print("NO")