# General implementaion of the algorithm

def dfs_recursive(node, graph, visited = None):
    # If visited is none create it
    if visited is None:
        visited = set()

    # Add the first node to the visited
    visited.add(node)
    print(node, end='')

    # Explore it's neighbors
    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            dfs_recursive(neighbor, graph, visited)

    return visited


