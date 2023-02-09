import sys


# Union - Find
def union(x, y):
    v1 = find(x)
    v2 = find(y)

    if v1 < v2: # v2의 부모 노드 번호가 크다면
        parent[v2] = v1 # v2의 부모 노드를 v1로 변환
    else:
        parent[v1] = v2


def find(x):
    if parent[x] != x:  # 자기 자신이 부모 노드가 아니면
        parent[x] = find(parent[x])  # 부모 노드 탐색
    return parent[x]  # 부모 노드 반환


# 정점의 개수와 간선의 개수 입력
v, e = map(int, sys.stdin.readline().split())

graph = []

# 각 간선에 대한 정보 입력
for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    graph.append((c, a, b))

# 부모 리스트 초기화
parent = [i for i in range(v+1)]

# 간선 비용을 기준으로 오름차순 정렬
graph.sort()

answer = 0

# 크루스칼 알고리즘
for i in range(e):
    c, a, b = graph[i]
    if find(a) != find(b): # 부모노드가 다르면 사이클이 발생하지 않기 때문에, union 수행
        union(a, b)
        answer += c # 간선 비용 추가

print(answer)

"""
    문제 : 1197번 - 최소 스패닝 트리
    메모리 : 47324 KB
    시간 : 316 ms
"""
