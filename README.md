<h1>ExpNo 4 : Implement A* search algorithm for a Graph</h1> 
<h3>Name: Pradeep Kumar G</h3>
<h3>Register Number: 212223230150</h3>
<H3>Aim:</H3>
<p>To ImplementA * Search algorithm for a Graph using Python 3.</p>
<H3>Algorithm:</H3>

``````
// A* Search Algorithm
1.  Initialize the open list
2.  Initialize the closed list
    put the starting node on the open 
    list (you can leave its f at zero)

3.  while the open list is not empty
    a) find the node with the least f on 
       the open list, call it "q"

    b) pop q off the open list
  
    c) generate q's 8 successors and set their 
       parents to q
   
    d) for each successor
        i) if successor is the goal, stop search
        
        ii) else, compute both g and h for successor
          successor.g = q.g + distance between 
                              successor and q
          successor.h = distance from goal to 
          successor (This can be done using many 
          ways, we will discuss three heuristics- 
          Manhattan, Diagonal and Euclidean 
          Heuristics)
          
          successor.f = successor.g + successor.h

        iii) if a node with the same position as 
            successor is in the OPEN list which has a 
           lower f than successor, skip this successor

        iV) if a node with the same position as 
            successor  is in the CLOSED list which has
            a lower f than successor, skip this successor
            otherwise, add  the node to the open list
     end (for loop)
  
    e) push q on the closed list
    end (while loop)

``````

<hr>
<h2>Program:</h2>
<hr>

```
Developed By : Pradeep Kumar G
Register No. : 212223230150
```
```py
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
```
<hr>

<h2>Output:</h2>

<img width="595" height="767" alt="output" src="https://github.com/user-attachments/assets/cc0c7f30-2c11-4fb8-83d0-612a26515186" />


<h3>Graph:</h3>

<img width="1536" height="855" alt="graph" src="https://github.com/user-attachments/assets/2e714140-7c14-48ea-a869-0330b8596e64" />


<img width="800" height="600" alt="graph_output" src="https://github.com/user-attachments/assets/f63732ee-6a30-47e7-81f5-89720a1bf133" />


<hr>
<h2>Sample Graph I</h2>
<hr>

![image](https://github.com/natsaravanan/19AI405FUNDAMENTALSOFARTIFICIALINTELLIGENCE/assets/87870499/b1377c3f-011a-4c0f-a843-516842ae056a)

<hr>
<h2>Sample Input</h2>
<hr>
10 14 <br>
A B 6 <br>
A F 3 <br>
B D 2 <br>
B C 3 <br>
C D 1 <br>
C E 5 <br>
D E 8 <br>
E I 5 <br>
E J 5 <br>
F G 1 <br>
G I 3 <br>
I J 3 <br>
F H 7 <br>
I H 2 <br>
A 10 <br>
B 8 <br>
C 5 <br>
D 7 <br>
E 3 <br>
F 6 <br>
G 5 <br>
H 3 <br>
I 1 <br>
J 0 <br>
<hr>
<h2>Sample Output</h2>
<hr>
Path found: ['A', 'F', 'G', 'I', 'J']


<hr>
<h2>Sample Graph II</h2>
<hr>

![image](https://github.com/natsaravanan/19AI405FUNDAMENTALSOFARTIFICIALINTELLIGENCE/assets/87870499/acbb09cb-ed39-48e5-a59b-2f8d61b978a3)


<hr>
<h2>Sample Input</h2>
<hr>
6 6 <br>
A B 2 <br>
B C 1 <br>
A E 3 <br>
B G 9 <br>
E D 6 <br>
D G 1 <br>
A 11 <br>
B 6 <br>
C 99 <br>
E 7 <br>
D 1 <br>
G 0 <br>
<hr>
<h2>Sample Output</h2>
<hr>
Path found: ['A', 'E', 'D', 'G']

<hr>
<h3>Result:</h3>

The A* Search algorithm was successfully implemented in Python and correctly found the optimal shortest path between the given start and goal nodes.
<hr>
