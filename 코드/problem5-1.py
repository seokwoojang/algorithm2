def solution(nums):
    answer = 0
    r = []
    for n in nums:
        if n in r:
            continue
        else:
            if len(r) < len(nums)/2:
                r.append(n)
                answer += 1
    return answer

nums1 = [3,1,2,3]
print(solution(nums1))

nums2 = [3,3,3,2,2,4]
print(solution(nums2))

nums3 = [3,3,3,2,2,2]
print(solution(nums3))