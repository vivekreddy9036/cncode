import heapq
import networkx as nx
import matplotlib.pyplot as plt

# Step 1: Define the network topology
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 1, 'D': 5},
    'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
    'D': {'B': 5, 'C': 8, 'E': 2, 'Z': 6},
    'E': {'C': 10, 'D': 2, 'Z': 3},
    'Z': {'D': 6, 'E': 3}
}

# Step 2: Dijkstra's Algorithm
def dijkstra(graph, start):
    pq = [(0, start)]
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous_nodes = {node: None for node in graph}

    while pq:
        current_distance, current_node = heapq.heappop(pq)
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))

    return distances, previous_nodes

# Step 3: Function to reconstruct path
def shortest_path(previous_nodes, start, end):
    path = []
    node = end
    while node is not None:
        path.append(node)
        node = previous_nodes[node]
    path.reverse()
    if path[0] == start:
        return path
    return []

# Step 4: Compute shortest paths from source 'A'
source_node = 'A'
distances, previous_nodes = dijkstra(graph, source_node)

print("Shortest distances from node A:")
for node, distance in distances.items():
    print(f"A -> {node} = {distance}")

print("\nShortest paths from node A:")
for node in graph:
    path = shortest_path(previous_nodes, source_node, node)
    print(f"A -> {node} : {path}")

# Step 5: Visualize the network
G = nx.Graph()
for node, edges in graph.items():
    for neighbor, weight in edges.items():
        G.add_edge(node, neighbor, weight=weight)

pos = nx.spring_layout(G)
plt.figure(figsize=(10,6))
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, font_size=12, font_weight='bold')
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Highlight shortest paths from source
for node in graph:
    if node != source_node:
        path = shortest_path(previous_nodes, source_node, node)
        path_edges = list(zip(path, path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)

plt.title("Network Topology and Shortest Paths from Node A")
plt.show()
