def solution(sizes):
    answer = 0
    min_x = 0
    min_y = 0
    
    for i in range(len(sizes)):
        a, b = sizes[i]
        
        if a < b:
            a, b = b, a
        
        if a > min_x:
            min_x = a
        
        if b > min_y:
            min_y = b
    
    return min_x * min_y