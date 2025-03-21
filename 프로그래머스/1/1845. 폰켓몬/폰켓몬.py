def solution(nums):
    take_away = int(len(nums) / 2)
    ponket_summary = dict()
    for p in nums:
        if p in ponket_summary.keys():
            ponket_summary[p] += 1
        else:
            ponket_summary[p] = 1
    answer = min(len(ponket_summary.keys()), take_away)
    return answer