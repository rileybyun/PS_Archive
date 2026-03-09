from collections import deque

def solution(begin, target, words):
    n = len(begin)
    
    if target in words:
        target_idx = words.index(target)
    else:
        return 0
    
    begin_list = list(begin)
    target_list = list(target)
    for i in range(n):
        words[i] = list(words[i])
    
    visited = [False] * len(words)
    shortest_dist = [100] * len(words)
    
    # bfs 알고리즘
    queue = deque()
    queue.append((begin_list, 0))
    
    while queue:
        cur_v, dist = queue.popleft()
        
        if cur_v == target_list:
            continue
        
        for k in range(len(words)):
            next_v = words[k]
            for idx in range(n):
                s1 = [x for i, x in enumerate(cur_v) if i != idx]
                s2 = [x for i, x in enumerate(next_v) if i != idx]
                if s1 == s2:
                    if not visited[k] or dist + 1 < shortest_dist[k]:
                        visited[k] = True
                        shortest_dist[k] = dist + 1
                        queue.append((next_v, dist + 1))
    
    return shortest_dist[target_idx]