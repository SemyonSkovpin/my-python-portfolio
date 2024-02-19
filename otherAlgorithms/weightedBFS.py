'''
1. Make random weighted graph

2. Find minimum weight path from A to B

3. Display the graph along with the walked path
'''

import random
import networkx as nx
from matplotlib import pyplot as plt
from bisect import insort
     

def random_graph(n=20, connectProb=0.05):
    '''
    Returns nx.Graph with n nodes. Each node has at least 1 edge with random other node. For each of the rest, it has *connectProb* chance to have edge with it. Each edge has random weight from 0 to 1
    '''
    G = nx.Graph()
    for i in range(n):
        G.add_node(i)
        if i != 0:
            nodes = list(G.nodes)
            # Add the first connection
            G.add_edge(i, nodes.pop(random.randint(0, len(nodes)-2)), weight=random.random())
            # Go through rest of possible connections
            for k in nodes[:-1]:
                if random.random() < connectProb:
                    G.add_edge(i, k, weight=random.random())
    return G


def display_graph_old(G, path):
    # HELPER FUNCTIONS -------------------
    def color_gradient(edge_weight):
        if edge_weight < 0.5:
            r = 2*edge_weight
            g = 1
            b = 2*edge_weight
        else:
            r = 1
            g = 1 - 2*(edge_weight - 0.5)
            b = 1 - 2*(edge_weight - 0.5)
        return (r, g, b)

    def color_three(edge_weight):
        if edge_weight < 0.33:
            return 'green'
        elif edge_weight < 0.66:
            return 'grey'
        else:
            return 'red'
    # ------------------------------------
    """
    Edges have red, gray, green colors depending on weight. Style walked edges differently
    """
    edge_color_map = []
    walked_edges = []
    other_edges = []
    for i, k in G.edges:
        edge_weight = G[i][k]['weight']
        color = color_three(edge_weight)
        edge_color_map.append(color)

        if i in path and k in path and abs(path.index(i) - path.index(k)) == 1:
            walked_edges.append((i, k))
        else:
            other_edges.append((i, k))

    pos = nx.spring_layout(G, seed = 9)
    nx.draw_networkx_edges(G, pos, edgelist=walked_edges, edge_color=edge_color_map, alpha=1, width = 3, style='dotted')
    nx.draw_networkx_edges(G, pos, edgelist=other_edges, edge_color=edge_color_map, alpha=0.8,  width = 2)
    nx.draw_networkx_labels(G, pos)
    plt.show()


def display_graph(G, path=[]):
    '''
        Open pyplot diagram with the graph. Also show the walked edges
    '''
    node_size = 72
    labels_size = 10
    edge_labels_size = 7
    edges_width = 2
    walked_edges_width = 2
    walked_edges_style = 'dotted'
    walked_edges_color = 'white'

    # Round displayed edge labels
    edge_labels = nx.get_edge_attributes(G, "weight")
    for edge in edge_labels:
        edge_labels[edge] = edge_labels[edge] // 0.1
    
    # Divide walked and unwalked edges into separate lists
    walked_edges = []
    other_edges = []
    for u, v in G.edges:
        if u in path and v in path and abs(path.index(u) - path.index(v)) == 1:
            walked_edges.append((u, v))

    # Make colormap for edges. Edges colors range from grey to black as particular edge's weight goes from 0 to 1
    def edge_color_function(weight):
        return 3*(0.8 - 0.8 * weight,)
    edge_colormap = []
    weights = [G[u][v]['weight'] for u, v in G.edges]
    for weight in weights:
        edge_colormap.append(edge_color_function(weight))
    
    pos = nx.spring_layout(G, seed=1, iterations=800)
    #nx.draw_networkx_nodes(G, pos, node_size=node_size)
    #nx.draw_networkx_labels(G, pos, font_size=labels_size)
    nx.draw_networkx_edges(G, pos, edge_color=edge_colormap, width=edges_width)
    nx.draw_networkx_edges(G, pos, walked_edges, edge_color=walked_edges_color, width=walked_edges_width, style=walked_edges_style)
    nx.draw_networkx_edge_labels(G, pos, edge_labels, font_size=edge_labels_size)
    plt.show()


def weighted_bfs(graph, start, end):
    sorted_paths = [(0, [start])]
    while sorted_paths:
        weight, path = sorted_paths.pop(0)
        u = path[-1]
        if end == u:
            return path
        for v in graph.neighbors(u):
            if v not in path:
                insort(sorted_paths, (weight + graph[u][v]['weight'], path + [v]))
    return []
        
    
def test():
    G = random_graph(10, 0.1)
    shortest_path = weighted_bfs(G, 0, len(G)-1)
    display_graph(G, shortest_path)

if __name__ == '__main__':
    test()
