# 최대 보트 개수 = 사람 수, 그래서 2명씩 보트를 태울 수 있는 경우만 계산해서 최대 개수에서 뺀다

def solution(people, limit) :
    answer = 0
    people.sort()

    a = 0
    b = len(people) - 1
    while a < b :
        if people[b] + people[a] <= limit :
            a += 1
            answer += 1
        b -= 1
    return len(people) - answer

print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50],100))