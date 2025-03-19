def str_to_sec(str_time):
    mm, ss = map(int, str_time.split(':'))
    answer = mm * 60 + ss
    return answer

def sec_to_str(int_sec):
    mm = int_sec // 60
    ss = int_sec % 60
    return f'{mm:02d}:{ss:02d}'

def solution(video_len, pos, op_start, op_end, commands):
    video_len = str_to_sec(video_len)
    pos = str_to_sec(pos)
    op_start = str_to_sec(op_start)
    op_end = str_to_sec(op_end)
    
    for c in commands:
        if op_start <= pos <= op_end:
            pos = op_end    # 오프닝 건너뛰기
        
        if c == 'prev':
            pos -= 10
        else:
            pos += 10
        
        if pos < 0:
            pos = 0
        elif pos > video_len:
            pos = video_len
        
    if op_start <= pos <= op_end:   # 마지막에 한 번 더 체크
        pos = op_end    # 오프닝 건너뛰기
    return sec_to_str(pos)