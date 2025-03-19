def solution(s):
    s_list = list(map(int, s.split()))
    answer = f'{min(s_list)} {max(s_list)}'
    return answer