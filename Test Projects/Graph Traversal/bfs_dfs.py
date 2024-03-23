def dfs_traversal(graph, start):
    visited = set()
    stack = [start]
    path = []
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            path.append(vertex)
            if vertex in graph:
                stack.extend(set(graph[vertex]) - visited)
    return path


def bfs_traversal(graph, start):
    visited = set()
    queue = [start]
    path = []
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            path.append(vertex)
            if vertex in graph:
                queue.extend(set(graph[vertex]) - visited)
    return path


graphs = [
    {
        "A": ["B", "C"],
        "C": ["D"],
        "D": ["E"]
    },
    {
        "A": ["B"],
        "B": ["C", "D"],
        "C": ["D", "E"]
    },
    {
        "A": ["B", "C", "D"],
        "B": ["C", "D"],
        "C": ["E"],
        "D": ["F"]
    }
]

for graph in graphs:
    print(f"Graph traversal using DFS: {dfs_traversal(graph, 'A')}")
    print(f"Graph traversal using BFS: {bfs_traversal(graph, 'A')}")