class Grafo:
    def __init__(self):
        self.vertices = []
        self.adjacencia = []

    def adicionar_vertice(self, vertice):
        if vertice not in self.vertices:
            self.vertices.append(vertice)
            for linha in self.adjacencia:
                linha.append(0)
            self.adjacencia.append([0] * len(self.vertices))

    def adicionar_aresta(self, vertice1, vertice2):
        if vertice1 not in self.vertices:
            self.adicionar_vertice(vertice1)
        if vertice2 not in self.vertices:
            self.adicionar_vertice(vertice2)
        idx1 = self.vertices.index(vertice1)
        idx2 = self.vertices.index(vertice2)
        self.adjacencia[idx1][idx2] = 1
        self.adjacencia[idx2][idx1] = 1

    def imprimir_pares(self):
        impressos = set()
        for i, vertice1 in enumerate(self.vertices):
            for j, vertice2 in enumerate(self.vertices):
                if self.adjacencia[i][j] == 1 and (vertice2, vertice1) not in impressos:
                    print(f"({vertice1}, {vertice2})")
                    impressos.add((vertice1, vertice2))

    def contar_arestas(self):
        count = 0
        for i in range(len(self.adjacencia)):
            for j in range(i + 1, len(self.adjacencia)):
                if self.adjacencia[i][j] == 1:
                    count += 1
        return count

grafo = Grafo()

arestas = [
    ("escova", "esmalte"), 
    ("escova", "shampoo"), 
    ("esmalte", "acetona"), 
    ("esmalte", "creme"),
    ("shampoo", "condicionador"), 
    ("acetona", "algodão"), 
    ("creme", "hidratante"), 
    ("condicionador", "máscara")
]

for produto1, produto2 in arestas:
    grafo.adicionar_aresta(produto1, produto2)

grafo.imprimir_pares()

num_arestas = grafo.contar_arestas()
print(f"Número de arestas no grafo: {num_arestas}")
