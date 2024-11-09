from itertools import combinations

orders1 = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course1 = [2,3,4]

orders2 = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
course2 = [2,3,5]

orders3 = ["XYZ", "XWY", "WXA"]
course3 = [2,3,4]

def solution(orders, course):
    answer = []

    for course_item in course:

        # course에 따라 조합에서 가장 많은 것을 찾기위해 갯수를 세는 딕셔너리
        comb_count = {}
        # course에 따라 조합에서 가장 많은 코스를 저장
        max_order = []

        # course에 따라 order를 조합해서 해당 조합이 com_count 딕셔너리에 있으면 +1을 하고 없으면 추가해서 1을 넣어준다
        for order in orders:
            # orders에 주문 하나를 course_item으로 조합
            order_comb = combinations(list(order), course_item)

            for o in order_comb:
                #문자 배열로 조합되어 있기때문에 한 문자로 합쳐서 한다
                order_comb_string = "".join(sorted(o))

                #딕셔너리에 있으면 +1 없으면 추가해서 1을 대입
                if comb_count.get(order_comb_string):
                    comb_count[order_comb_string] += 1
                else:
                    comb_count[order_comb_string] = 1
        
        #해당 course_item 에서 가장 많은 것을 배열에 추가
        max_order = [k for k, v in comb_count.items() if ((v == max(comb_count.values())) and v >= 2)]

        answer.extend(max_order)
    
    answer = sorted(answer)
    return answer

print(solution(orders1,course1))
print(solution(orders2,course2))
print(solution(orders3,course3))