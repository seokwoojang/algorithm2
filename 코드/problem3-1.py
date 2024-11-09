
p1 = ["leo", "kiki", "eden"]
c1 = ["eden","kiki"]

def s(participant, completion):
    part_num = {}

    for p in participant:
        if p in part_num:
            part_num[p] += 1
        else:
            part_num[p] = 1
    
    for c in completion:
        part_num[c] -= 1
    
    for n in part_num.keys():
        if part_num[n] > 0:
            return n
    
    return []

print(s(p1,c1))