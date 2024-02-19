
class Node():
    nodeCount = 0

    def __init__(self):
        self.name = str(Node.nodeCount)
        Node.nodeCount += 1
        self.children = []
        self.edgeWeights= []


    def addEdges (self, nodes, edgeWeights):
        self.children += nodes
        self.edgeWeights += edgeWeights
        for i in range(len(nodes)):
            nodes[i].children.append(self)
            nodes[i].edgeWeights.append(edgeWeights[i])


    def getChildren(self):
        return self.children
    
    
    def edgeWeights(self):
        return self.edgeWeights


    
class weightedGraph():
    def __init__(self, nodes):
        self.nodes = nodes