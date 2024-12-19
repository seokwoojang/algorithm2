def solution(triangle):
    # 삼각형의 아래에서부터 위로 이동
    for row in range(len(triangle) - 2, -1, -1):  # 마지막부터 시작
        for col in range(len(triangle[row])):
            # 현재 위치에 아래 두 위치 중 더 큰 값을 더함
            triangle[row][col] += max(triangle[row + 1][col], triangle[row + 1][col + 1])
    
    # 최상단에 최종 최대 합이 저장됨
    return triangle[0][0]

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))