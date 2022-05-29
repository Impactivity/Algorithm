INF = 999
adj_mat = [[0, 29, INF, INF, INF, 10, INF],
           [29, 0, 16, INF, INF, INF, 15],
           [INF, 16, 0, 12, INF, INF, INF],
           [INF, INF, 12, 0, 22, INF, 18],
           [INF, INF, INF, 22, 0, 27, 25],
           [10, INF, INF, INF, 27, 0, INF],
           [INF, 15, INF, 18, 25, INF, 0]]

node_num = len(adj_mat)
visited = [False] * node_num
distances = [INF] * node_num

def min_distance():
    # 현재노드에서 갈 수 있는 노드에 대한 distance를 업데이트했기 때문에
    # 방문하지 않은 모든 노드 중 최소 경로를 구한다.
    for i in range(node_num):
        if visited[i] == False:
            print(f'현재 i={i}')
            v = i
            break

    for i in range(node_num):
        if visited[i] == False and distances[i] < distances[v]:
            v = i

    return v


def prim_algorithm(start):

    distances[start] = 0
    for i in range(node_num):
        next_node = min_distance()
        visited[next_node] = True

        for i in range(node_num):
            if visited[i] == False and distances[i] > adj_mat[next_node][i]:
                distances[i] = adj_mat[next_node][i]




print(prim_algorithm(0))
print("distances: ", distances)
print("minimum cost: ", sum(distances))