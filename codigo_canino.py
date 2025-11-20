from codigo_animales import Animal

# Clase hija 1
class perro(Animal):
    # Constructor de hija 2
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color, raza):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)
        self.raza = raza

    def descanso(self):
        print(f"{self.nombre} esta descansando ")

    def sonido(self):
        print(f"{self.nombre} ladra: ¡Guau guau! 🐶")

    def jugar(self):
        print(f"{self.nombre} está jugando con la pelota 🎾")

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Raza: {self.raza}")
