def solution(sizes):
    answer = 0
    min_x = 0
    min_y = 0
    
    for i in range(len(sizes)):
        a, b = sizes[i]
        
        # 가로길이가 세로길이보다 길도록 통일 (a: 가로, b: 세로)
        if a < b:
            a, b = b, a
        
        if a > min_x:
            min_x = a
        
        if b > min_y:
            min_y = b
    
    return min_x * min_y