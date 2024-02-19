import random
import matplotlib.pyplot as plt
import networkx as nx



class Node():
    nodeCount = 0

    def __init__(self):
        self.id = Node.nodeCount 
        Node.nodeCount += 1
        self.children = []

    def add_child(self, child):
        self.children.append(child)
        child.children.append(self)

    def get_children(self):
        return self.children



class Graph():
    def __init__(self):
        self.nodes = []

    def get_nodes(self):
        return self.nodes

    def add_node(self, node):
        self.nodes.append(node)
        
 

def make_random_digraph(n, a):
    '''
    :n: Amout of nodes. Make undirected graph (just a directed graph, where nodes point back at each other). Add n nodes one by one. Each new node makes minimum 1 connection with random alredy added node. 
    :a: Float. There is *a* chance to create connection with each of the rest nodes
    '''
    assert 0 <= a <= 1
    myGraph = Graph()
    for i in range(n):
        myNode = Node()

        if len(myGraph.get_nodes()) != 0:
            nodesToPick = myGraph.get_nodes()[:]
            myNode.add_child(nodesToPick.pop(random.randint(0, len(nodesToPick)-1)))
            while nodesToPick:
                picked_node = nodesToPick.pop()
                if random.random() <= a:
                    myNode.add_child(picked_node)   

        myGraph.add_node(myNode)
    return myGraph



def visualise_graph (myGraph):
    edges = []
    for myNode in myGraph.get_nodes():
        for nodeChild in myNode.get_children():
            edges.append([myNode.id, nodeChild.id])
    G = nx.Graph()
    nx.draw_networkx(G) 
    plt.show() 



def visualise_walked_graph (myGraph, path):
    # Initialise
    G = nx.Graph()
    
    # Add nodes and color_map for them
    color_map = []
    for myNode in myGraph.get_nodes():
        # Each node in this graph is represented by its id
        G.add_node(myNode.id)

        # Walked nodes colored in black
        if myNode in path:
            color_map.append('yellow')
        else:
            color_map.append('gray')
    
    # Add edges
    for myNode in myGraph.get_nodes():
        for nodeChild in myNode.get_children():
            G.add_edge(myNode.id, nodeChild.id)

    # Show the graph
    nx.draw(G, node_color=color_map, with_labels=False)
    plt.show()


    


# DFS version with my adjustment
def DFS_1(graph, start, end, path=[], shortest=None):
    '''
    This function will return the *path* but continued from *start* to *end* in shortest way
    '''
    path = path + [start]
    if start == end:
        return path
    if shortest == None or len(path) < len(shortest):
        for child_node in start.get_children():
            if child_node not in path:
                new_path = DFS_1(graph, child_node, end, path, shortest)
                if new_path != None:
                    shortest = new_path
    return shortest



# Lecture DFS version
def DFS_2(graph, start, end, path=[], shortest=None):
    path = path + [start]
    if start == end:
        return path
    for child_node in start.get_children():
        if shortest == None or len(path) < len(shortest):
            if child_node not in path:
                new_path = DFS_2(graph, child_node, end, path, shortest)
                if new_path != None:
                    shortest = new_path
    return shortest
    


n = 100
thickness = 0.0001
myGraph = make_random_digraph(n, thickness)
shortest_path = DFS_1(myGraph, myGraph.get_nodes()[0], myGraph.get_nodes()[n-1])
visualise_walked_graph(myGraph, shortest_path)
