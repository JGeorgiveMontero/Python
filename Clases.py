class Vehiculo():
    # Atributos
    color = None
    longitud = None
    ruedas = 4

    # Metodos
    def arrancar(self):
        print("El motor arranco")
    def detener(self):
        print("el motor esta detenido")

carro1 = Vehiculo()
carro1.arrancar()
carro1.detener()
carro2 = Vehiculo()
carro2.color = "azul"
carro1.ruedas = 3
print(carro1.ruedas)
print(carro2.color)

