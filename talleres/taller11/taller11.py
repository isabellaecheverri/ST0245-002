import numpy as np


class GraphAM:
    def __init__(self, size):
        self.size = size
        self.matrix = np.zeros((size,size))

    def addArc(self, source, destination, weight):
        i = source # O(1)
        j = destination # O(1)
        self.matrix[i][j] = weight # O(1)
        # Total: O(1)

    def getSuccesors(self, vertex):
        respuesta = []
        for j in range(self.size):
            if matrix[vertex][j] is not 0:
                respuesta.add(j)
            return respuesta

    def getWeight(self, source, destination):
        '''for i in range(size):
            for j in range(size):
                self.matrix[i][j] ??? '''
        return matrix[source][destination]

    def getEdges(self):
        ...

    def __str__(self):
        ...
    

    class GraphAL:
        def __init__(self, size):
            ...

        def addArc(self, vertex, edge, weight):
            ...

        def getSuccessors(self, vertice):
            ...

        def getWeight(self, source, destination):
            ...

        def __str__(self):
            ...