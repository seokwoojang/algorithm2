def solution(k, dungeons):
    def dfs(k, cnt, visited):
        max_cnt = cnt
        for i in range(len(dungeons)):
            if not visited[i] and dungeons[i][0] <= k:
                visited[i] = True
                max_cnt = max(dfs(k - dungeons[i][1], cnt + 1, visited), max_cnt)
                visited[i] = False
        
        return max_cnt
    visited = [False] * len(dungeons)
    return dfs(k, 0, visited)

dungeons = [[80,20],[50,40],[30,10]]
print(solution(80, dungeons))