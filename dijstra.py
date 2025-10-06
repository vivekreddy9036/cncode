import networkx as nx
import matplotlib.pyplot as plt


def create_network_graph():
    """Create and return a weighted graph with predefined edges."""
    G = nx.Graph()
    edges = [
        ('A', 'B', 4),
        ('A', 'C', 2),
        ('B', 'C', 1),
        ('B', 'D', 5),
        ('C', 'D', 8),
        ('C', 'E', 10),
        ('D', 'E', 2),
        ('D', 'Z', 6),
        ('E', 'Z', 3)
    ]
    G.add_weighted_edges_from(edges)
    return G


def compute_shortest_paths(graph, source_node):
    """Compute shortest paths and distances from source node using Dijkstra's algorithm."""
    shortest_paths = nx.single_source_dijkstra_path(graph, source=source_node)
    shortest_distances = nx.single_source_dijkstra_path_length(graph, source=source_node)
    return shortest_paths, shortest_distances


def print_shortest_paths(shortest_paths, shortest_distances, source_node):
    """Print shortest paths and distances in a formatted manner."""
    print(f"Shortest paths from node {source_node}:")
    for target in shortest_paths:
        path_str = " -> ".join(shortest_paths[target])
        print(f"To {target}: Path = {path_str}, Distance = {shortest_distances[target]}")


def visualize_graph(graph):
    """Visualize the graph with edge weights."""
    pos = nx.spring_layout(graph, seed=42)  # Fixed seed for consistent layout
    edge_labels = nx.get_edge_attributes(graph, 'weight')
    
    plt.figure(figsize=(12, 8))
    nx.draw(graph, pos, with_labels=True, node_color='lightblue', 
            node_size=2000, font_size=14, font_weight='bold')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_size=12)
    plt.title("Network Topology with Edge Weights (Dijkstra's Algorithm)", fontsize=16)
    plt.tight_layout()
    plt.show()


def main():
    """Main function to execute Dijkstra's algorithm demonstration."""
    # Create the network graph
    graph = create_network_graph()
    
    # Set source node
    source_node = 'A'
    
    # Compute shortest paths
    shortest_paths, shortest_distances = compute_shortest_paths(graph, source_node)
    
    # Print results
    print_shortest_paths(shortest_paths, shortest_distances, source_node)
    print("\n" + "="*50)
    print("Displaying network visualization...")
    
    # Visualize the graph
    visualize_graph(graph)


if __name__ == "__main__":
    main()
