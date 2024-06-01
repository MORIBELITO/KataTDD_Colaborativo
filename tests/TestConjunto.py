class Conjunto:
    def __init__(self, datos, pesos):
        self.__datos = datos
        self.__pesos = pesos

    def promedio(self):
        if not self.__datos:
            return None  # Si el conjunto está vacío, retornamos None

        if len(self.__datos) != len(self.__pesos):
            raise ValueError("La cantidad de datos y pesos deben ser iguales")

        total = sum(d * p for d, p in zip(self.__datos, self.__pesos))
        total_pesos = sum(self.__pesos)

        return total / total_pesos
