
def solution(cards1, cards2, goal):
    answer = ''

    a,b,g = 0, 0, 0

    while True:
        if len(cards1) > a and cards1[a] == goal[g]:
            a += 1
            g += 1
        elif len(cards2) > b and cards2[b] == goal[g]:
            b += 1
            g += 1
        else:
            break
    
    if g >= len(goal):
        answer = "Yes"
    else:
        answer = "No"

    return answer

# cards1 = ["i", "drink", "water"]
# cards2 = ["want", "to"]

cards1 = ["show", "lot", "please", "the", "me"]
cards2 = ["money"]

goal = ["show", "me", "the", "money"]
print(solution(cards1, cards2, goal))