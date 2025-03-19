def solution(s):
    paren_num_dict = {'(':1, ')':-1}
    pos = 0
    
    for c in s:
        pos += paren_num_dict[c]
        if pos < 0:
            return False
    return True if pos == 0 else False