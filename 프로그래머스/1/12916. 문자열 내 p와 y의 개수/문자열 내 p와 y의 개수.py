def solution(s):
    s = s.upper()
    p_num = s.count('P')
    y_num = s.count('Y')
    return True if p_num == y_num else False