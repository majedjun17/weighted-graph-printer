import networkx as nx
import matplotlib.pyplot as plt

adj_matrix = [
    [0, 1, 4, float('inf')],
    [1, 0, 2, 5],
    [4, 2, 0, 1],
    [float('inf'), 5, 1, 0]
]

G = nx.Graph()
for i in range(len(adj_matrix)):
    G.add_node(i)
for i in range(len(adj_matrix)):
    for j in range(i, len(adj_matrix[i])):
        if adj_matrix[i][j] != float('inf'):
            G.add_edge(i, j, weight=adj_matrix[i][j])

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue',
        edge_color='gray', width=1, alpha=0.7, font_size=12)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(
    G, pos, edge_labels=edge_labels, font_size=10, label_pos=0.5)
plt.show()
