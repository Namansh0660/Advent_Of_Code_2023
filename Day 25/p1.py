import networkx as nx

g = nx.Graph()
file_path = "C:/Users/Hp/Documents/Visual Studio/AOC_2023/Day 25/d25.txt"
with open(file_path , 'r')as file:
    for line in file:
        left, right = line.split(":")
        for node in right.strip().split():
            g.add_edge(left, node)
            g.add_edge(node, left)

g.remove_edges_from(nx.minimum_edge_cut(g))
a, b = nx.connected_components(g)

print(len(a) * len(b))
