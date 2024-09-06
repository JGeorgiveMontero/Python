class Animal:
    def hablar(self):
        print("Soy un animal")
class Perro(Animal):
    def hablar(self):
        print("guao guaus")
class Gato(Animal):
    def hablar(self):
        print("Miauuuss")

animal = Animal()
perro  = Perro()
gato   = Gato()

def dar_voz(objeto):
    objeto.hablar()

dar_voz(animal)
dar_voz(gato)
dar_voz(perro)
