from modules.grafo import Grafo
import modules.algoritmos as algoritmos

def main():
    caminho_arquivo = input("Insira o caminho pro arquivo que contem o grafo:\n> ")
    grafo = Grafo(caminho_arquivo)
    print("===> Exercicio 2)")
    s = input("Insira o indice do vertice de partida:\n> ")
    algoritmos.busca_em_largura(grafo, int(s))
    print("===> Exercicio 4)")
    s = input("Insira o indice do vertice de partida:\n> ")
    algoritmos.dijkstra(grafo, int(s))

if __name__ == "__main__":
    main()