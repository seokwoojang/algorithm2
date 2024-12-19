def solution(nums):
    num_set = set(nums)
    n = len(nums)
    k = n // 2

    return min(k, len(num_set))

nums1 = [3,1,2,3]
print(solution(nums1))

nums2 = [3,3,3,2,2,4]
print(solution(nums2))

nums3 = [3,3,3,2,2,2]
print(solution(nums3))