
info1 = [0,0,1,1,1,0,1,0,1,0,1,1] # 방문할 노드들
edge1 = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]

info2 = [0,1,0,1,1,0,1,0,0,1,0]
edge2 = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]

# def solution(info, edges):
#     answer = []
#     visited = [0] * len(info)

#     def dfs(sheep, wolf):
#         if sheep > wolf:
#             answer.append(sheep)
#         else:
#             return
        
#         for p, c in edges:
#             if visited[p] and not visited[c]:
#                 visited[c] = 1
#                 if info[c] == 0:
#                     dfs(sheep + 1, wolf)
#                 else: 
#                     dfs(sheep, wolf + 1)
#                 visited[c] = 0
    
#     visited[0] = 1
#     dfs(1, 0)

#     return max(answer)

def solution(info, edge):
    answer = []
    visited = [0] * len(info)

    def dfs(sheep, wolf):
        if sheep > wolf:
            answer.append(sheep)
        else:
            return
        
        for p, c in edge:
            if visited[p] and not visited[c]:
                visited[c] = 1
                if info[c] == 0:
                    dfs(sheep + 1, wolf)
                else:
                    dfs(sheep, wolf + 1)
                visited[c] = 0
    
    visited[0] = 1
    dfs(1, 0)

    return max(answer)

print(solution(info2,edge2))