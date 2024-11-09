
def solution3(board, moves):
    answer = 0
    
    cols = [[] for _ in range(len(board[0]))]
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[j][i] != 0:
                cols[i].append(board[j][i])
    
    basket = []

    for m in moves:
        if cols[m-1]:
            doll = cols[m-1].pop()

        if basket and basket[-1] == doll:
            basket.pop()
            answer += 2
        else:
            basket.append(doll)

    return answer

board = [[0,0,0,0,0],
        [0,0,1,0,3],
        [0,2,5,0,1],
        [4,2,4,4,2],
        [3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

answer = solution3(board,moves)
print(answer)