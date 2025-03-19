def is_integer(x):
    int_x = int(x)
    return x - int_x == 0

def solution(n):
    # 첫 항이 a이고, 공차가 1인 등차수열의 항이 x개일 때의 합 = x * (a + (x-1)/2)
    # a가 자연수라면 해당하는 케이스이다.
    answer = 0
    x = 0
    while True:
        x += 1
        a = n/x - (x-1)/2
        if a < 1: break
        if is_integer(a) and a >= 1:
            answer += 1
    return answer