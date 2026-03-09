from collections import deque

def solution(n, computers):
    answer = 0
    visited = [False] * n  # 노드 범위: 0 ~ n-1
    
    def bfs(cur_v):
        nonlocal visited
        queue = deque()
        queue.append(cur_v)
        
        while queue:    # queue 안에 노드가 없어질 때까지 계속
            cur_v = queue.popleft()
            for k in range(n):
                if computers[cur_v][k] and not visited[k]:
                    queue.append(k)
                    visited[k] = True
    
    for i in range(n):
        if not visited[i]:
            bfs(i)
            answer += 1
    
    return answer