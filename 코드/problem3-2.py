
genres = ["classic", "pop", "classic","classic","pop"]

plays = [500,600,150,800,2500]

def solution(genres, plays):
    answer = []
    idx_genres = []
    genres_plays = {}

    for i in range(len(genres)):
        idx_genres.append((i, genres[i], plays[i]))
        if genres[i] not in genres_plays:
            genres_plays[genres[i]] = plays[i]
        else:
            genres_plays[genres[i]] += plays[i]
    
    idx_genres = sorted(idx_genres, key = lambda x : (-x[2], x[0]))
    genres_plays = dict(sorted(genres_plays.items(), key = lambda x : -x[1]))
    
    for genre in genres_plays.keys():
        count = 0
        for i in range(len(idx_genres)):
            if count < 2 and genre == idx_genres[i][1]:
                count += 1
                answer.append(idx_genres[i][0])

    return answer

print(solution(genres,plays))