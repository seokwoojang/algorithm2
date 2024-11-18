
def solution(n, computers):
    def dfs(node):
        visited[node] = True
        for i in range(n):
            if computers[node][i] == 1 and not visited[i]:
                dfs(i)
    
    answer = 0
    visited = [False] * n  # 방문 여부를 기록할 배열
    
    for i in range(n):
        if not visited[i]:  # 방문하지 않은 노드가 있다면 새로운 네트워크
            dfs(i)
            answer += 1  # 새로운 네트워크를 발견할 때마다 카운트
    
    return answer

computers1 = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
computers2 = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
print(solution(3, computers2))