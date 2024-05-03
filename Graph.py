# create graph class for easier managmenet of interference / CFGs

class Node():
    # value = ''
    # block = []
    # edges = set() # TODO: change to list if needed
    # directedTo = [] # for directional graphs
    # directedFrom = [] # for directional graphs
    # color = None

    def __init__(self, value, block=[], color=None, edges=set()):
        self.value = value
        self.edges = edges
        self.color = color
        self.block = block
        self.directedTo = []
        self.directedFrom = []
        self.liveness = []
        self.collected = 0

    def __str__(self):
        node = """"""
        node += '  Node: ' + self.value + '\n'
        node += '    directedTo: ' + str(self.directedTo) + '\n'
        node += '    directedFrom: ' + str(self.directedFrom) + '\n'
        return node

class Graph():
    # vertices = []
    def __init__(self, vertices = []):
        self.vertices = vertices
    
    def addVertex(self, v, block=[], color=None):
        self.vertices.append(Node(value=v, block=block, color=color))
    
    def addEdge(self, v0, v1):
        v0 = self.findVertex(v0)
        v1 = self.findVertex(v1) 
        if v0 not in v1.edges:
            v0.edges.append(v1.value)
        if v1 not in v0.edges:
            v1.edges.append(v0.value)

    def addDirectedEdge(self, fromv, tov):
        fromv = self.findVertex(fromv)
        tov = self.findVertex(tov) 
        if tov not in fromv.directedTo:
            fromv.directedTo.append(tov)
        if fromv not in tov.directedFrom:
            tov.directedFrom.append(fromv)
    
    def findVertex(self, name):
        for vert in self.vertices:
            if vert.value == name:
                return vert
        print(f"error finding vertex {name}")
        return False

    def removeVertex(self, v):
        pass 

    def removeEdge(self, v0, v1):
        pass
    
    def sortGraph(self, reverse=False): # TODO: choose sort vs sorted
        self.vertices = sorted(self.vertices, key=lambda v: len(v.edges), reverse=reverse)
        return self # not sure if we want it returned after sorting

    def __str__(self):
        graph = """{\n"""
        for v in self.vertices:
            graph += '  Node: ' + v.value + '\n'
            graph += '    edges: ' + str(v.edges) + '\n'
            graph += '    directedTo: ' + str([l.value for l in v.directedTo]) + '\n'
            graph += '    directedFrom: ' + str([l.value for l in v.directedFrom]) + '\n'
            graph += '    color: ' + str(v.color) + '\n'
            graph += '    block: ' + str(v.block) + '\n'
            graph += '    liveness: ' + str(v.liveness) + '\n'
        graph += "}"
        return graph


