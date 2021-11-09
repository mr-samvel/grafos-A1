from .aresta import Aresta

class Grafo:
    def __init__(self, vertices, arestas, peso_mapper):
        # Lista de rotulos
        self.__vertices = vertices
        # Lista de objetos arestas
        self.__arestas = arestas
        # mapeia o peso de cada aresta
        peso_mapper(self.__arestas)

    # Retorna quantidade de vertices
    def qtdVertices(self):
        return len(self.__vertices)
    
    # Retorna a quantidade de arestas
    def qtdArestas(self):
        return len(self.__arestas)

    # Retorna o grau do vertice v
    def grau(self, v):
        grau = 0
        for aresta in self.__arestas:
            if(aresta.u == v or aresta.v == v):
                grau+=1
        return grau
    
    # Retorna o rotulo do vertice v
    def rotulo(self, v):
        return self.__vertices[v]
    
    # Retorna os vizinhos do vertice v
    def vizinhos(self, v):
        pass
    
    # Retorna True se os dois vertices estiverem ligados por uma aresta
    def haAresta(self, u, v):
        pass

    # se {u, v} pertence à E, retorna o peso da aresta {u,v}; 
    # se não existir, retorna um valor  infinito positvo(maior ponto flutuante)
    def peso(self, u, v):
        pass

    # carregar um grafo a partir de um arquivo no formato especificado
    def ler(self, arquivo):
        pass
    