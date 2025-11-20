from codigo_animales import Animal

# Clase hija 2
class Gato(Animal):
    # Constructor de hija 2
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color, personalidad):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)
        self.personalidad = personalidad

    def sueña(self):
        print(f"{self.nombre} esta soñando")

    def interacion_social(self):
        print(f"{self.nombre} esta interatuando con otros animales")

    def arañar(self):
        print(f"{self.nombre} está arañando el sofá 😼")

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Personalidad: {self.personalidad}")
