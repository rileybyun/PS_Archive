def dfs(node_num):
    global N, graph, visited

    visited[node_num] = True    # 방문 표시
    print(node_num, end=' ')

    for i in range(1, N+1):
        if (not visited[i]) and graph[node_num][i]:
            dfs(i)  # 재귀


def bfs(node_num):
    global N, graph, visited
    visited[node_num] = True
    q = [node_num]  # 방문할 곳을 저장하는 큐 (핵심)

    while len(q) > 0:
        n = q.pop(0)    # 0번째 인덱스값 pop
        # visited[n] = True   #  방문 표시를 여기서 하면 안 됨
        print(n, end=' ')
        for i in range(1, N+1):
            if (not visited[i]) and graph[n][i]:
                visited[i] = True   # 방문 표시를 여기서 해야 함
                q.append(i) # 큐에 방문할 곳 추가


# 1. 문제 정보 입력 (N: 노드 수, M: 간선 수, V: 탐색시작 노드)
N, M, V = map(int, input().split())
graph = [[False] * (N+1) for _ in range(N+1)]   # dfs, bfs
visited = [False] * (N+1)   # dfs, bfs

# 2. graph 정보 입력
for i in range(M):
    r, c = map(int, input().split())
    graph[r][c] = True
    graph[c][r] = True

# 3. dfs
dfs(V)
print()

visited = [False] * (N+1)   # visited 초기화

# 4. bfs
bfs(V)
print()
