from collections import deque
def bfs(start, graph):
    queue = deque([start])
    visited = set([start])
    while queue:
        curr_node = queue.popleft()
        for next_node in graph[curr_node]:
            if next_node not in visited:
                visited.add(next_node)
                queue.append(next_node)
    return -1


def solution():
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }



