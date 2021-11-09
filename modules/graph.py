from vertex import Vertex

class Graph:
    def __init__(self, vertices, edges, weight_mapper):
        self.__vertices = vertices
        self.__edges = edges
        self.__weight_mapper = weight_mapper

    