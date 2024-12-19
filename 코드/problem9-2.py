def solution(n, stations, w):
    # 이미 커버된 위치를 표시하는 변수
    covered = 0
    count = 0
    idx = 0

    while covered < n:
        if idx < len(stations) and stations[idx] - w <= covered + 1:
            # 현재 기지국이 다음 커버되지 않은 구역을 포함하는 경우
            covered = stations[idx] + w
            idx += 1
        else:
            # 새로운 기지국 설치
            count += 1
            covered += 2 * w + 1

    return count

# 실행 예제
print(solution(11, [4, 11], 1))  # 출력: 3
