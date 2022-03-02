import math
inf = math.inf

graph = [ [0,2,5,1,inf,inf],
              [2,0,3,2,inf,inf],
              [5,3,0,3,1,5],
              [1,2,3,0,1,inf],
              [inf,inf,1,1,0,2],
              [inf,inf,5,inf,2,0]]

n = len(graph)
visited = [0] * n
d = []

def minimum_dist(node):
    num = len(graph[node])
    _min = inf
    for i in range(0,num):
        if d[i] < _min and visited[i] == 0:
            _min = d[i]
            inx = i

    return inx

def dijkstra(start):
    global d
    d = graph[start] #현재 시작되는 노드와의 거리 값 dist 저장

    visited[start] = 1 #현재노드 방문처리

    for i in range(0,len(graph)-1): # 현재 노드를 제외한 경로 최소 구하기
        now = minimum_dist(start) # 현재 노드에서 가장 거리가 최소인 inx 반환
        visited[now] = 1 # 해당 노드 방문처리

        for j in range(0, len(graph[now])): # 최소 거리 노드에서 또 다른 노드 가는 최소 경로 계산
            cost = d[now] + graph[now][j]
            if cost < d[j]: # 노드 거쳐서 가는 경우보다 큰 경우
                d[j] = cost



dijkstra(0)
print(d)