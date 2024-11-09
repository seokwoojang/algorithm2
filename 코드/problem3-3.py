id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]

def solution(id_list, report, k):
    answer = []

    report = list(set(report))

    user_report = {}
    report_cnt = {}

    for i in range(len(report)):
        a, b = report[i].split(" ")

        if a not in user_report:
            user_report[a] = [b]
        else:
            user_report[a].append(b)

        if b not in report_cnt:
            report_cnt[b] = 1
        else:
            report_cnt[b] += 1
        
    for uid in id_list:
        cnt = 0
        if uid in user_report:
            for rid in user_report[uid]:
                if rid in report_cnt and report_cnt[rid] >= k:
                    cnt += 1
        answer.append(cnt)       

    return answer

print(solution(id_list,report,2))