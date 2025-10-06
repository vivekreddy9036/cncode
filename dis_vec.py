# Step 1: Define the network topology
graph = {
    'A': {'B': 1, 'C': 5},
    'B': {'A': 1, 'C': 2, 'D': 4},
    'C': {'A': 5, 'B': 2, 'D': 1},
    'D': {'B': 4, 'C': 1, 'E': 3},
    'E': {'D': 3}
}

# Step 2: Initialize routing tables
nodes = graph.keys()
routing_table = {}

for node in nodes:
    table = {}
    for dest in nodes:
        if dest == node:
            table[dest] = (0, '-')
        elif dest in graph[node]:
            table[dest] = (graph[node][dest], dest) 
        else:
            table[dest] = (float('inf'), None)  
    routing_table[node] = table

# Step 3: Distance Vector Algorithm Iteration
updated = True
while updated:
    updated = False
    for node in nodes:
        for neighbor in graph[node]:
            for dest in nodes:
                
                new_cost = graph[node][neighbor] + routing_table[neighbor][dest][0]
                if new_cost < routing_table[node][dest][0]:
                    routing_table[node][dest] = (new_cost, neighbor)
                    updated = True

# Step 4: Display routing tables
for node in nodes:
    print(f"Routing Table for Node {node}:")
    print(f"{'Destination':<12}{'Cost':<8}{'Next Hop':<10}")
    for dest in nodes:
        cost, next_hop = routing_table[node][dest]
        cost_str = str(cost) if cost != float('inf') else "∞"
        next_hop_str = str(next_hop) if next_hop is not None else "-"
        print(f"{dest:<12}{cost_str:<8}{next_hop_str:<10}")
    print("\n")
