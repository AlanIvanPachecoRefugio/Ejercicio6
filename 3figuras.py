import math

class Figura:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def area(self):
        pass

    def perimetro(self):
        pass

class HexagonoRegular(Figura):
    def __init__(self, color, lado):
        super().__init__(color)
        self.lado = lado

    def area(self):
        return 3 * math.sqrt(3) * (self.lado ** 2) / 2

    def perimetro(self):
        return 6 * self.lado

class Rombo(Figura):
    def __init__(self, color, diagonal_mayor, diagonal_menor):
        super().__init__(color)
        self.diagonal_mayor = diagonal_mayor
        self.diagonal_menor = diagonal_menor

    def area(self):
        return (self.diagonal_mayor * self.diagonal_menor) / 2

    def perimetro(self):
        return 4 * math.sqrt(((self.diagonal_mayor / 2) ** 2) + ((self.diagonal_menor / 2) ** 2))

class Trapecio(Figura):
    def __init__(self, color, base_mayor, base_menor, altura):
        super().__init__(color)
        self.base_mayor = base_mayor
        self.base_menor = base_menor
        self.altura = altura

    def area(self):
        return ((self.base_mayor + self.base_menor) / 2) * self.altura

    def perimetro(self):
        lado_a = (self.base_mayor - self.base_menor) / 2
        lado_b = math.sqrt((lado_a ** 2) + (self.altura ** 2))
        return self.base_mayor + self.base_menor + (2 * lado_b)

# Ejemplo de uso
hexagono = HexagonoRegular("verde", 5)
print(f"Área del hexágono regular: {hexagono.area()}")
print(f"Perímetro del hexágono regular: {hexagono.perimetro()}")

rombo = Rombo("azul", 6, 8)
print(f"Área del rombo: {rombo.area()}")
print(f"Perímetro del rombo: {rombo.perimetro()}")

trapecio = Trapecio("rojo", 10, 6, 4)
print(f"Área del trapecio: {trapecio.area()}")
print(f"Perímetro del trapecio: {trapecio.perimetro()}")
