# 입력 데이터
mygraph = {
    'vertices': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    'edges': [
        (7, 'A', 'B'),
        (5, 'A', 'D'),
        (7, 'B', 'A'),
        (8, 'B', 'C'),
        (9, 'B', 'D'),
        (7, 'B', 'E'),
        (8, 'C', 'B'),
        (5, 'C', 'E'),
        (5, 'D', 'A'),
        (9, 'D', 'B'),
        (7, 'D', 'E'),
        (6, 'D', 'F'),
        (7, 'E', 'B'),
        (5, 'E', 'C'),
        (7, 'E', 'D'),
        (8, 'E', 'F'),
        (9, 'E', 'G'),
        (6, 'F', 'D'),
        (8, 'F', 'E'),
        (11, 'F', 'G'),
        (9, 'G', 'E'),
        (11, 'G', 'F')
    ]
}

parent = dict()
rank = dict()

# 노드 parent 초기화
def make_set(node):
    parent[node] = node
    rank[node] = 0
    return

def union(node_v,node_u):
    root1 = find(node_v)
    root2 = find(node_u)

    # union-by-rank 기법
    if rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2] += 1
    return

def find(node):
    # path-compression 기법
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]

def kruskal(graph):
    mst = list()
    # 1. 노드 초기화 : 서로소 집합으로 만들기
    for node in graph['vertices']:
        make_set(node)

    # 2. 노드 가중치 별로 오름차순으로 sort
    graph['edges'].sort()

    # 3. 노드 사이클 없는 간선 연결
    for edge in graph['edges']:
        weight, node_v , node_u = edge
        if find(node_v) != find(node_u):
            union(node_v,node_u)
            mst.append(edge)

    return mst

print(kruskal(mygraph))
