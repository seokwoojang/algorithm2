from heapq import heappop, heappush

def solution(N, road, K):
    answer = 0

    g = [[] for _ in range(N + 1)]

    for a, b, w in road:
        g[a].append((b, w))
        g[b].append((a, w))
    
    distance = [float('inf')] * (N + 1)
    distance[1] = 0

    h = [(1, 0)]

    while h:
        cur_town, cur_cost = heappop(h)

        if cur_cost > distance[cur_town]:
            continue

        for next_town, cost in g[cur_town]:
            new_cost = cur_cost + cost
            if new_cost < distance[next_town]:
                distance[next_town] = new_cost
                heappush(h, (next_town, new_cost))
    
    for i in range(1, N + 1):
        if distance[i] <= K:
            answer += 1

    return answer

road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
print(solution(5, road, 3))