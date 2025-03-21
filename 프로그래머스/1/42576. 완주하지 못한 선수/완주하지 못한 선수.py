def solution(participant, completion):
    parti_dict = dict()
    
    for p in participant:
        if p in parti_dict.keys():
            parti_dict[p] += 1
        else:
            parti_dict[p] = 1
    
    for c in completion:
        if parti_dict[c] == 1:
            del parti_dict[c]
        else:
            parti_dict[c] -= 1
    return str(set(parti_dict.keys()).pop())