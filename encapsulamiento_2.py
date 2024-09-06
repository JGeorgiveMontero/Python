class Animal:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self._edad = edad
class Perro(Animal):
    def __init__(self,nombre,edad,raza):
        super().__init__(nombre,edad)
        self.raza = raza
    
    def mostrar_edad(self):
        print(f"Tengo {self._edad} años")
    

perro1 = Perro("Chester",3,"Husky")
perro1.mostrar_edad()