
def solution(dirs):
    answer = set()

    move = {"U":(0, 1), "D":(0, -1), "R":(1, 0), "L": (-1, 0)}
    x, y = 0, 0
    for d in dirs:
        dx, dy = move[d]
        nx, ny = x + dx, y + dy

        if -5 <= nx <= 5 and -5 <= ny <= 5:
            answer.add((x, y, nx, ny))
            answer.add((nx, ny, x, y))
            x = nx
            y = ny

    return len(answer) // 2

dirs1 = "ULURRDLLU"
dirs2 = "LULLLLLLU"
print(solution(dirs2))