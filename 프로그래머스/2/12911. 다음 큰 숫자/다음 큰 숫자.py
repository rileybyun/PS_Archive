def solution(n):
    ones = bin(n)[2:].count('1')
    answer = n
    while True:
        answer += 1
        temp = bin(answer)[2:].count('1')
        if ones == temp: break
    return answer