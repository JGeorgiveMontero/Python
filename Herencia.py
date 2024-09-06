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

    def pedir_refuerzos(self):
        print(f"el Agente policial: {self.nombre} pidiendo refuerzos")
    def saludar(self):
        print(f"Hola soy el agente: {self.nombre} y les deseo un excelente dia")
a = Medico("Javier")
b = Policia("Ana")
c = Ciudadano("Jose","Ingeniero")
a.saludar()
b.saludar()
b.pedir_refuerzos()
b.saludar()
