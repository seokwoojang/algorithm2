from collections import deque
import sys
input = sys.stdin.readline

def dfs(graph, node, visited):
    visited[node] = True
    cnt = 1
    for n in graph[node]:
        if not visited[n]:
            cnt += dfs(graph, n, visited)
    return cnt

def solution(n, wires):
    answer = float('inf')

    for i in range(len(wires)):
        g = [[] for _ in range(n + 1)]
        for j, (a, b) in enumerate(wires):
            if i == j:
                continue
            g[a].append(b)
            g[b].append(a)
        
        visited = [False] * (n + 1)
        cnt1 = dfs(g, 1, visited)
        cnt2 = n - cnt1

        answer = min(answer, abs(cnt1 - cnt2))
    
    return answer

wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
print(solution(9, wires))
