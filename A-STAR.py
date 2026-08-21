#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# A* Algorithm

from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt

def a_star(graph, heuristic, start, goal):
    open_set = {start}
    closed_set = set()
    g = {start: 0}
    parent = {start: None}
    while open_set:
        current = min(open_set, key=lambda node: g[node] + heuristic[node])
        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            path.reverse()
            print("\nShortest Path :", " -> ".join(path))
            print("Total Cost :", g[goal])
            return path
        open_set.remove(current)
        closed_set.add(current)
        for neighbour, cost in graph[current]:
            if neighbour in closed_set:
                continue
            new_cost = g[current] + cost
            if neighbour not in open_set:
                open_set.add(neighbour)
            elif new_cost >= g.get(neighbour, float('inf')):
                   continue
            g[neighbour] = new_cost
            parent[neighbour] = current
    print("Path does not exist!")
    return None

graph = defaultdict(list)
G = nx.Graph()
n, e = map(int, input("Enter number of nodes and edges: ").split())
print("\nEnter the edges (u v cost):")
for i in range(e):
    u, v, cost = input(f"Edge {i+1}: ").split()
    cost = int(cost)
    graph[u].append((v, cost))
    graph[v].append((u, cost))
    G.add_edge(u, v, weight=cost)

print("\nAdjacency List")
for node in graph:
    print(node, "->", graph[node])

heuristic = {}
print("\nEnter Heuristic Values")
for i in range(n):
    node, h = input(f"{i+1}. Node Heuristic : ").split()
    heuristic[node] = int(h)
print("\nHeuristic Values")
print(heuristic)

plt.figure(figsize=(8,6))                                # Draw Original Graph

pos = nx.spring_layout(G, seed=20)
nx.draw_networkx_nodes(G, pos, node_color="skyblue", node_size=1800)
nx.draw_networkx_labels(G, pos, font_size=12,font_weight="bold")
nx.draw_networkx_edges(G, pos, width=2)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos,  edge_labels=edge_labels)
plt.title("Original Graph")
plt.axis("off")
plt.show()

start = input("\nEnter Start Node: ")
goal = input("Enter Goal Node: ")
if start not in graph:
    print("Invalid Start Node!")
elif goal not in graph:
    print("Invalid Goal Node!")
else:
    shortest_path = a_star(graph, heuristic, start, goal)
    if shortest_path:                                               # Highlight Shortest Path
        path_edges = []
        for i in range(len(shortest_path)-1):
            path_edges.append((shortest_path[i], shortest_path[i+1]))
        plt.figure(figsize=(8,6))

        nx.draw_networkx_nodes(G, pos, node_color="skyblue",  node_size=1800)
        nx.draw_networkx_labels(G, pos, font_size=12,   font_weight="bold")

        # Draw all edges
        nx.draw_networkx_edges(G , pos, edge_color="gray", width=2)
                                                 
        # Highlight shortest path
        nx.draw_networkx_edges(G, pos,  edgelist=path_edges, edge_color="red", width=4)                                              
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        plt.title("Shortest Path Highlighted (Red)")
        plt.axis("off")
        plt.show()