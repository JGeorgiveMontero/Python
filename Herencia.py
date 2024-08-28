class Ciudadano:
    def __init__(self,nombre,profesion):
        self.nombre = nombre
        self.profesion = profesion
    def saludar(self):
        print(f"Hola, soy {self.nombre} y mi profesion es {self.profesion}")
class Medico(Ciudadano):
    def __init__(self,nombre):
        super().__init__(nombre,"Medico")
class Policia(Ciudadano):
    def __init__(self,nombre):
        super().__init__(nombre,"Policia")


a = Medico("Javier")
b = Policia("Ana")
c = Ciudadano("Jose","Ingeniero")
a.saludar()
b.saludar()
c.saludar()