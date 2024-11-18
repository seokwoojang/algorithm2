from collections import deque
import sys
input = sys.stdin.readline

def bfs(graph, start, visited):
    q = deque([start])
    visited[start] = True
    count = 1

    while q:
        node = q.popleft()
        for n in graph[node]:
            if not visited[n]:
                visited[n] = True
                q.append(n)
                count += 1

    return count

def solution(n, wires):
    answer = float('inf') # 초기 값 무한대로 설정

    # 모든 간선을 한 번씩 끊어보고 두 그래프를 개수를 세서 차이를 구한다
    for i in range(len(wires)):
        # 그래프를 인접 리스트로 표현
        graph = [[] for _ in range(n + 1)]
        for j, (a, b) in enumerate(wires):
            if i == j:
                continue
            graph[a].append(b)
            graph[b].append(a)
        
        # 두 그래프의 노드 개수 구하기
        visited = [False] * (n + 1)
        cnt1 = bfs(graph, 1, visited)
        cnt2 = n - cnt1

        answer = min(answer, abs(cnt1 - cnt2))

    return answer

wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
print(solution(9, wires))
