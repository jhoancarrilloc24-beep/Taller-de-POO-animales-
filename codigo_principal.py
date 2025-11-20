from codigo_canino import perro
from codigo_felino import Gato

# Crear objetos
# Zona de codigo principal

animal1 = perro("Max", 6, "casa de perro", "comida de perro", "45cm", "Marrón","salchicha")
animal2 = Gato("Luna", 3, "casa de luis(domestico)", "comida de gato", "25cm", "Blanco", "jugetona")

print("========== PERRO ==========")
animal1.mostrar_info()
animal1.moverse()
animal1.comunicacion()
animal1.reproducion()
animal1.alimentacion()
animal1.adaptacion()
animal1.instintos()
animal1.descanso()
animal1.sonido()
animal1.jugar()

print("\n========== GATO ==========")
animal2.mostrar_info()
animal2.moverse()
animal2.comunicacion()
animal2.reproducion()
animal2.alimentacion()
animal2.adaptacion()
animal2.instintos()
animal2.sueña()
animal2.interacion_social()
animal2.arañar()
