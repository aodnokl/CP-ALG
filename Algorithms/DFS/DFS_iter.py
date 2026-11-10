# General implementation but iterative version

def dfs_iterative(start_node, graph):
    visited = set()
    stack = [start_node]
    
    while stack:
        node = stack.pop()
        
        if node not in visited:
            visited.add(node)
            print(node, end=" ")
            
            # Explore the neighbor preserving the order
            for neighbor in reversed(graph.get(node, [])):
                if neighbor not in visited:
                    # Add to stack if needed
                    stack.append(neighbor)
                    
    return visited