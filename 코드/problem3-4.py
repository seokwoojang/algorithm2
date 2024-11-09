
record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

def solution(record):
    answer = []

    uid_name = {}
    u = []
    for r in record:
        u.append(r.split(" "))
        
    for i in u:
        if i[0] == "Enter" or i[0] == "Change":
                uid_name[i[1]] = i[2]

    for i in u:
        if i[0] == "Enter":
            answer.append(uid_name[i[1]] + "님이 들어왔습니다.")
        elif i[0] == "Leave":
            answer.append(uid_name[i[1]] + "님이 나갔습니다.")

    return answer

print(solution(record))