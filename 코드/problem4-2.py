from collections import deque

def bfs(sx, sy, maps, target):
    x = [1, -1, 0, 0]
    y = [0, 0, 1, -1]

    visited = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]
    q = deque()
    visited[sx][sy] = True
    q.append((sx,sy,0))

    while q:
        ox, oy, cnt = q.popleft()

        if maps[ox][oy] == target:
            return cnt

        for i in range(4):
            dx = ox + x[i]
            dy = oy + y[i]

            if 0 <= dx < len(maps) and 0 <= dy < len(maps[0]):
                if maps[dx][dy] != "X" and visited[dx][dy] == False:
                    q.append((dx, dy, cnt + 1))
        
    return -1

def solution(maps):
    answer = 0

    sx, sy, lx, ly = 0, 0, 0, 0

    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == "S":
                sx = i
                sy = j
            elif maps[i][j] == "L":
                lx = i
                ly = j
    
    start_lever_distance = bfs(sx, sy, maps, "L")
    if start_lever_distance == -1:
        return -1
    
    lever_end_distance = bfs(lx, ly, maps, "E")
    if lever_end_distance == -1:
        return -1

    answer = start_lever_distance + lever_end_distance

    return answer
    

maps1 = ["SOOOL",
        "XXXXO",
        "OOOOO",
        "OXXXX",
        "OOOOE"]

maps2 = ["LOOXS",
        "OOOOX",
        "OOOOO",
        "OOOOO",
        "EOOOO"]
print(solution(maps1))
print(solution(maps2))