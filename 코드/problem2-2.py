
def solution2(answers):
    patterns = [
        [1,2,3,4,5],
        [2,1,2,3,2,4,2,5],
        [3,3,1,1,2,2,4,4,5,5]
    ]

    scores = [0] * 3

    for i, answer in enumerate(answers):
        for j, pattern in enumerate(patterns):
            if answer == pattern[i % len(pattern)]:
                scores[j] += 1
    
    answer = []
    maxScore = max(scores)

    for i, score in enumerate(scores):
        if score == maxScore:
            answer.append(i + 1)    
    
    return answer

answer1 = [1,2,3,4,5]
print(solution2(answer1))