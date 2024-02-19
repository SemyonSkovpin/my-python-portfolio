import random
from matplotlib import pyplot as plt
import networkx as nx


class weightedGraphV2():    
    def __init__(self, nodeNames, edges, edgeWeights):
        """
        :nodeNames: list of str
        :edges: list of tuples
        :edgeWeights: list of numbers
        """
        self.nodeNames = nodeNames[:]
        self.edges = edges[:]
        self.edgeWeights = edgeWeights[:]

    def getNodeChildren(self, nodeName):
        children = []
        for edge in self.edges:
            if nodeName in edge:
                    a = edge[:]
                    a.remove(nodeName)
                    children.append(a[0])
        return children
    
    def getEdgeWeight(self, edge):
        # (a, b) and (b, a) are same edges
        if edge[1] + edge[0] in self.edges:
            edge = edge[1] + edge[0]

        return self.edgeWeights[self.edges.index(edge)]
    


def makeRandomWGraph(n = 20, connectProb = 0.02):
    """
    Make a graph with <n> nodes. Add each node one after another. Each new node has 100% chance to make an edge with random already existing one and <connectProb> chance for each of the rest. For each new edge, assign weight - random number from 0 to 1
    """
    nodeNames = []
    edges = []
    edgeWeights = []
    # Add each node one by one
    for n1 in range(n):
        nodeName = str(n1) # Name for each node is just its number
        nodeNames.append(nodeName)

        if len(nodeNames) != 1:
            # Create the first edge for this node
            nodesToConnect = nodeNames[:-1]
            n2 = random.randint(0, len(nodesToConnect)-1)
            edges.append((nodeName, nodesToConnect.pop(n2)))
            edgeWeights.append(random.random())

            # Go through the rest of possible edges
            for n2 in range(len(nodesToConnect)):
                if random.random() < connectProb:
                    edges.append((nodeName, nodesToConnect[n2]))
                    edgeWeights.append(random.random())
    
    # Pack everything in a graph object
    return weightedGraphV2(nodeNames, edges, edgeWeights)



myGraph = makeRandomWGraph()
G = nx.Graph()
for i in range(len(myGraph.edges)):
    weight = myGraph.edgeWeights[i]
    G.add_edge(myGraph.edges[i][0], myGraph.edges[i][1], weight=weight)

pos = nx.spring_layout(G, seed=1)  # positions for all nodes - seed for reproducibility

# nodes
nx.draw_networkx_nodes(G, pos, node_size=3)

# edges
nx.draw_networkx_edges(G, pos, width=1)

# edge weight labels
edge_labels = nx.get_edge_attributes(G, "weight")
#nx.draw_networkx_edge_labels(G, pos, edge_labels)

plt.show()



def weightedBFS(graph, start, end):
    # Keep track of all paths that are avaliable for continuation. Keep track of each paths total weight as well
    # Add distance equal to zero and the first path: just the start node
    sortedPaths = [(0, [start])]

    while sortedPaths:
        # pick the shortest path of already explored to continue it. There will never be a path thats shorter than alredy existing ones when its added
        currentPathWeight, currentPath = sortedPaths.pop(0)

        n0 = currentPath[-1]

        if n0 == end:
            return currentPath

        for n1 in graph.getNodeChildren(n0):
            if n1 not in currentPath: 
                sortedPaths.append((currentPathWeight + graph.edgeWeight(n0, n1), currentPath + [n1]))
        sortedPaths.sort()
    return None
