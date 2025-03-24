def solution(data, ext, val_ext, sort_by):
    col_dict = {'code':0, 'date':1, 'maximum':2, 'remain':3}
    ext_idx = col_dict[ext]
    sort_idx = col_dict[sort_by]
    filtered_data = [record for record in data if record[ext_idx] < val_ext]
    
    filtered_data.sort(key = lambda x: x[sort_idx])
    return filtered_data