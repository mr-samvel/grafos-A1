from .aresta import Aresta

class Grafo:
    def __init__(self, rotulos, listaDeAdj, peso_mapper, listaDePesos):
        # Lista de rotulos
        self.__rotulos = rotulos
        # Lista de objetos arestas
        self.__listaDeAdj = listaDeAdj # para cada vertice há uma lista de vizinhos
        # mapeia o peso de cada aresta
        peso_mapper(self.__listaDeAdj)
        self.__listaDePesos = listaDePesos # igual a lista adjacencia, mas com os pesos das arestas

    # Retorna quantidade de vertices
    def qtdVertices(self):
        return len(self.__rotulos)
    
    # Retorna a quantidade de arestas
    def qtdArestas(self):
        quantidade = 0
        for i in range(self.qtdVertices()):
            for adj in self.__listaDeAdj[i]:
                if(adj >= i):
                    quantidade+=1
        return quantidade

    # Retorna o grau do vertice v
    def grau(self, v): # TODO:
        pass
    
    # Retorna o rotulo do vertice v
    def rotulo(self, v):
        return self.__rotulos[v]
    
    # Retorna os vizinhos do vertice v
    def vizinhos(self, v):
        return self.__listaDeAdj[v]
    
    # Retorna True se os dois vertices estiverem ligados por uma aresta
    def haAresta(self, u, v):
        for vizinho in self.__listaDeAdj[u]:
            if(vizinho == v):
                return True
        return False

    # se {u, v} pertence à E, retorna o peso da aresta {u,v}; 
    # se não existir, retorna um valor  infinito positvo(maior ponto flutuante)
    def peso(self, u, v):
        if(self.haAresta(u,v)):
            for i in len(self.__listaDeAdj[u]):
                if(self.__listaDeAdj[u][i] == v):
                    return self.__listaDePesos[u][i]

    # carregar um grafo a partir de um arquivo no formato especificado
    def ler(self, arquivo):
        pass
    