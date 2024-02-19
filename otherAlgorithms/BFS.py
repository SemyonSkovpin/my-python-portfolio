'''
1. Make a random graph of alphabet letters  
2. Implement BFS and return node that contains certain letter
'''

import random
import string
import numpy as np



class node:
    def __init__(self, value):
        self.value = value
        self.edges = []


        
class graph:
    '''
    Make an undirected graph class where each node can have object of any type assigned to it
    '''
    def __init__(self):
        self.nodes = []
        
    def addNode (self, value):
        self.nodes.append(node(value))

    def addEdge (self, a, b):
        a.edges.append(b)
        b.edges.append(a)

    def randomGraph (self):
        """
        Generate graph with random edges (each of 2 nodes will have a 50/50 chance to be connected). Each node will have a random letter of alphabet as its value. 
        """
        nodes = 40
        for i in range(nodes):
            letter = string.ascii_lowercase[np.random.randint(0, 25)]
            self.addNode(letter)
        for i in range(nodes):
            for j in range(nodes):
                if i < j:
                    if random.randint(0, 1) == 1:
                        self.addEdge(self.nodes[i], self.nodes[j])

    def BFS (self, start, neededValue):
        queue = []
        visited = []
        queue.append (start)
        visited.append (start)
        while queue:
            currentNode = queue.pop(0)
            for connectedNode in currentNode.edges:
                if connectedNode not in visited:
                    visited.append(connectedNode)
                    queue.append(connectedNode)
            if currentNode.value == neededValue:
                return currentNode
        return None
        



myGraph = graph()
myGraph.randomGraph()

myGraph.showGraph()
print(myGraph.BFS(myGraph.nodes[0], 'a'))
