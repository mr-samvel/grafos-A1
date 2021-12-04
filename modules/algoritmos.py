from .grafo import Grafo
import heapq

# questao 2
# recebe um grafo e um vertice s
def busca_em_largura(grafo: Grafo, s: int):
    fila = [s]
    visitados = []
    distanciaAte = dict()
    distanciaAte[s] = 0

    while fila:
        v = fila.pop(0)
        if v not in visitados:
            visitados.append(v)
            for vizinho in grafo.vizinhos(v):
                if vizinho not in visitados:
                    fila.append(vizinho)
                    distanciaAte[vizinho] = distanciaAte[v] + 1
    
    # Exibe o resultado no formato da questao
    texto = '0: '
    indice = 0
    for vertice in distanciaAte:
        if indice != distanciaAte[vertice]:
            texto = texto[:-2]
            indice = distanciaAte[vertice]
            texto += '\n' + str(indice) + ': '
        texto = texto + str(vertice) + ', '
    print(texto)


def dijkstra(grafo: Grafo, s: int):
    def cria_fila():
        pass

    n_vertices = grafo.qtdVertices()
    dists = [float('inf')] * (n_vertices+1)
    dists[s] = 0
    caminho_percorrido = [[]] * (n_vertices+1)
    fila = cria_fila()

    # printar resposta
    for v in range(1, len(dists)):
            print(str(v) + ": " + str(caminho_percorrido[v])[1:-1] + "; d=" + str(dists[v]))
    

#  def floyd_warshall(grafo: Grafo):
    