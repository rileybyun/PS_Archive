def solution(a, b):
    iter_num = max(len(a), len(b))
    if len(a) < iter_num:
        a = '0' * (iter_num - len(a)) + a
    elif len(b) < iter_num:
        b = '0' * (iter_num - len(b)) + b
    
    answer = []
    carry = 0
    
    for i in range(1, iter_num+1):
        temp = int(a[-i]) + int(b[-i]) + carry
        carry = (temp // 10)
        remainder = temp - carry * 10
        answer.append(str(remainder))
    
    if carry != 0:
        answer.append(str(carry))
    answer.reverse()
    
    return ''.join(answer)