def solution(arr):
    idx = []
    temp = ''
    for i, x in enumerate(arr):
        if temp != x:
            idx.append(i)
            temp = x
    answer = [arr[i] for i in idx]
    return answer