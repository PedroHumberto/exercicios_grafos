class Grafo:
    def __init__(self):
        self.adjacencia = {}

    def adicionar_aresta(self, produto1, produto2):
        if produto1 not in self.adjacencia:
            self.adjacencia[produto1] = []
        if produto2 not in self.adjacencia:
            self.adjacencia[produto2] = []
        self.adjacencia[produto1].append(produto2)
        self.adjacencia[produto2].append(produto1)

    def imprimir_pares(self):
        impressos = set()
        for produto in self.adjacencia:
            for adjacente in self.adjacencia[produto]:
                if (adjacente, produto) not in impressos:
                    print(f"({produto}, {adjacente})")
                    impressos.add((produto, adjacente))

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
