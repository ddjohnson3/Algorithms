def main():
    t = int(input().strip())
    
    for _ in range(t):
        n = int(input().strip())
        
        adjacency_list = {}
        node_names = []  
        for _ in range(n):
            parts = input().strip().split()
            node = parts[0]
            neighbors = parts[1:]
            adjacency_list[node] = neighbors
            node_names.append(node)
        
        visited = set()
        traversal_order = []

        def dfs(start_node):
            stack = [start_node]
            while stack:
                current_node = stack.pop()
                if current_node not in visited:
                    visited.add(current_node)
                    traversal_order.append(current_node)
                    #last pushed is first visited
                    for neighbor in reversed(adjacency_list[current_node]):
                        if neighbor not in visited:
                            stack.append(neighbor)

        #disconnected nodes
        for node in node_names:
            if node not in visited:
                dfs(node)
        
        print(' '.join(traversal_order))

if __name__ == "__main__":
    main()