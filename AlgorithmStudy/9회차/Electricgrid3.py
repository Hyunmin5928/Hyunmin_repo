from collections import deque

def BFS(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    cnt = 0
    while queue :
        v = queue.popleft()
        cnt += 1
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    return cnt
    
def solution(n, wires):
    answer = n - 2
    for i in range(len(wires)):
        tree = wires.copy()
        graph = [[] for i in range(n+1)]
        visited = [False] * (n+1)
        tree.pop(i)
        for wire in tree:
            v1, v2 = wire
            graph[v1].append(v2)
            graph[v2].append(v1)
        for idx,g in enumerate(graph) :
            if g != [] :
                start = idx
                break
        cnt1 = BFS(graph, start, visited)
        cnt2 = n - cnt1
        if abs(cnt1 - cnt2) < answer:
            answer = abs(cnt1 - cnt2)
    return answer
