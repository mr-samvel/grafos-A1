from .grafo import Grafo
import heapq

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
    def cria_fila(dists):
        fila = [(dists[s], s)]
        heapq.heapify(fila)
        return fila
    
    n_vertices = grafo.qtdVertices()
    
    dists = [float('inf')] * (n_vertices+1)
    dists[s] = 0
    predecessores = {i : i for i in range(n_vertices+1)}
    predecessores[s] = s
    fila = cria_fila(dists)
    while fila:
        (d,u) = heapq.heappop(fila)
        for v in grafo.vizinhos(u):
            novo_caminho = dists[u] + grafo.peso(u, v)
            if dists[v] > novo_caminho:
                dists[v] = novo_caminho
                predecessores[v] = u
                heapq.heappush(fila, (dists[v], v))

    # printar resposta
    def caminho_percorrido(v):
        caminho = [v]
        while v != s and v != predecessores[v]:
            caminho = [predecessores[v]] + caminho
            v = predecessores[v]
        return caminho

    for v in range(1, len(dists)):
            print(str(v) + ": " + str(caminho_percorrido(v))[1:-1] + "; d=" + str(dists[v]))