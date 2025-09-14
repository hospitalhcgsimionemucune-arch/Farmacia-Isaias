class Medicamento:
    def __init__(self, id, nome, preco, estoque):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

catalogo = [
    Medicamento(1, "Paracetamol 500mg", 300, 10),
    Medicamento(2, "Amoxicilina 250mg", 1200, 5),
    Medicamento(3, "Ibuprofeno 400mg", 850, 8),
    Medicamento(4, "Dipirona 1g", 250, 12),
    Medicamento(5, "Omeprazol 20mg", 600, 6),
]
