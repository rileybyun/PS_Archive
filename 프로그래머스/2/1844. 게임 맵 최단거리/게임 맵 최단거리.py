from collections import deque

def solution(maps):
    row = len(maps)   # 가로 길이
    col = len(maps[0])
    visited = [[False] * col for i in range(row)]
    shortest_dist = [[100] * col for i in range(row)]
    
    def bfs(start_x, start_y):
        nonlocal visited, shortest_dist
        queue = deque()
        queue.append((start_x, start_y, 0)) # 튜플의 세 번째 값은 dist(이동거리)이다.
        
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        
        while queue:
            cur_x, cur_y, dist = queue.popleft()
            
            # 연결된 노드를 큐에 추가
            for k in range(4):
                next_x = cur_x + dx[k]
                next_y = cur_y + dy[k]
                
                if 0 <= next_x < row and 0 <= next_y < col and maps[next_x][next_y]:
                    if not visited[next_x][next_y] or dist + 1 < shortest_dist[next_x][next_y]:
                        visited[next_x][next_y] = True
                        shortest_dist[next_x][next_y] = dist + 1
                        queue.append((next_x, next_y, dist + 1))
    
    bfs(0,0)    # 시작 위치는 (0,0) 이므로, 이렇게 호출한다.
    
    if shortest_dist[row-1][col-1] == 100:
        return -1   # 목적지에 도착하지 못한다는 말이므로 -1 반환
    else:
        return shortest_dist[row-1][col-1] + 1 # 지나가는 칸의 개수의 최소값