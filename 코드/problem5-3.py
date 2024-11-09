
def solution(cards1, cards2, goal):
    answer = ''
    result = []

    a,b,g = 0, 0, 0

    for g in range(len(goal)):
        if a < len(cards1) and cards1[a] == goal[g]:
            result.append(cards1[a])
            a += 1
        elif b < len(cards2) and cards2[b] == goal[g]:
            result.append(cards2[b])
            b += 1
        else:
            answer = 'No'
            return answer

    answer = 'Yes'
    return answer

# cards1 = ["i", "drink", "water"]
# cards2 = ["want", "to"]

cards1 = ["show", "lot", "please", "the", "me"]
cards2 = ["money"]

goal = ["show", "me", "the", "money"]
solution(cards1, cards2, goal)