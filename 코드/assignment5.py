
board1 = [[0,0,0],[0,0,0],[0,0,0]]
board2 = [[0,0,0,0,0,0,0,1],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,1,0,0],
    [0,0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0,1],
    [0,0,1,0,0,0,1,0],
    [0,1,0,0,0,1,0,0],
    [1,0,0,0,0,0,0,0]]
board3 = [[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]
board4 = [[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]

def solution(board):
    answer = float('inf')
    queue = [(0, 0, -1, 0)] # x, y, direction, cost
    N = len(board)
    visited = [[[0 for _ in range(4)] for _ in range(N)] for _ in range(N)]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while queue:
        x, y, prev_direction, cost = queue.pop()

        for direction, (dx, dy) in enumerate(directions):
            new_x, new_y = x + dx, y + dy

            # 새로운 좌표가 범위안에 있고, 기둥이 없다면 ㄱㄱ
            if 0 <= new_x < N and 0 <= new_y < N and board[new_x][new_y] != 1:
                #새로운 비용 계산
                new_cost = 0
                if prev_direction == -1 or (prev_direction - direction) % 2 == 0:
                    new_cost = cost + 100
                else:
                    new_cost = cost + 600
                
                #끝에 도착했다면 답 기록
                if (new_x, new_y) == (N - 1, N - 1):
                    answer = min(answer, new_cost)
                # 방문한 기록이 없거나 기존 비용보다 새로운 비용이 작다면 큐에 추가하고 비용 갱신
                elif visited[new_x][new_y][direction] == 0 or visited[new_x][new_y][direction] > new_cost:
                    queue.append((new_x, new_y, direction, new_cost))
                    visited[new_x][new_y][direction] = new_cost


    return answer
    
print(solution(board4))