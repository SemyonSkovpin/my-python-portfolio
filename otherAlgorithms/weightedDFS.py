from weightedBFS import *



def weighted_dfs(graph, newNode, endNode, path=[], weight=0, shortestPath=None, shortestWeight=0):
    path = path + [newNode]
    if len(path) != 1: 
        weight += graph[path[-2]][newNode]['weight']
    
    if shortestPath == None or weight <= shortestWeight:
        if newNode == endNode:
            return (path, weight)
        for nextNewNode in graph.neighbors(newNode):
            if nextNewNode not in path:
                newPath, newWeight = weighted_dfs(graph, nextNewNode, endNode, path, weight, shortestPath, shortestWeight)
                if newPath != None:
                    shortestPath = newPath
                    shortestWeight = newWeight
    return (shortestPath, shortestWeight)



G = random_graph()
shortest_path_bfs = weighted_bfs(G, 0, len(G)-1)
shortest_path_dfs = weighted_dfs(G, 0, len(G)-1)[0]
display_graph(G, shortest_path_bfs)
display_graph(G, shortest_path_dfs)

    