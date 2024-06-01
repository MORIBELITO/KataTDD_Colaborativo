class Conjunto:
    def __init__(self, elementos, pesos=None):
        self.elementos = elementos
        self.pesos = pesos if pesos else [1] * len(elementos)

    def promedio(self):
        if not self.elementos:
            return None

        suma_ponderada = sum(elem * peso for elem, peso in zip(self.elementos, self.pesos))
        suma_pesos = sum(self.pesos)
        return suma_ponderada / suma_pesos
