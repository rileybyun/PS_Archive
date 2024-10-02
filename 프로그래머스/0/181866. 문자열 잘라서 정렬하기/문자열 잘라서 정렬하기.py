def solution(myString):
    no_x = myString.split("x")
    no_x = [s for s in no_x if s]
    answer = sorted(no_x)
    return answer