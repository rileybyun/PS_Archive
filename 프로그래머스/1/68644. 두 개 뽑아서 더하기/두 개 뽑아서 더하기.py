def solution(numbers):
    answer = set()
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            temp = numbers[i] + numbers[j]
            answer.add(temp)
    return sorted(list(answer))