from collections import deque, defaultdict

def ford_fulkerson(graph, source, sink):
    flow = defaultdict(lambda: defaultdict(int))
    max_flow = 0

    def bfs():
        parent = {}
        visited = set()
        queue = deque([source])
        visited.add(source)

        while queue:
            u = queue.popleft()
            for v in graph[u]:
                capacity = graph[u][v]
                residual = capacity - flow[u][v]
                if residual > 0 and v not in visited:
                    parent[v] = u
                    visited.add(v)
                    if v == sink:
                        return parent
                    queue.append(v)
        return None

    parent = bfs()
    while parent:
        path_flow = float('inf')
        s = sink
        while s != source:
            p = parent[s]
            
            #bottle neck
            path_flow = min(path_flow, graph[p][s] - flow[p][s])
            s = p

        v = sink
        while v != source:
            u = parent[v]
            flow[u][v] += path_flow
            flow[v][u] -= path_flow
            v = u

        max_flow += path_flow
        parent = bfs()

    return max_flow

def main():
    inst = int(input())
    results = []

    for _ in range(inst):
        m, n, q = map(int, input().split())

        graph = defaultdict(dict)
        A = [f'A{i}' for i in range(1, m + 1)]
        B = [f'B{j}' for j in range(1, n + 1)]

        for a in A:
            graph['s'][a] = 1
            graph[a] 

        for b in B:
            graph[b]['t'] = 1
            graph['t'] 

        for _ in range(q):
            i, j = map(int, input().split())
            a_node = f'A{i}'
            b_node = f'B{j}'
            graph[a_node][b_node] = 1
            graph[b_node] 

        max_matching = ford_fulkerson(graph, 's', 't')
        is_perfect = (max_matching == m)
        results.append(f"{max_matching} {'Y' if is_perfect else 'N'}")

    for result in results:
        print(result)

if __name__ == "__main__":
    main()

