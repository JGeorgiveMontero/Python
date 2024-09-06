class Usuario:
    def __init__(self,id,nombre,apellidos):
        self.id = id #publico
        self._nombre = nombre # protegido
        self.__apellidos = apellidos # privado
    def mostrar_apellido(self):
        print(self.__apellidos)

usuario_1 = Usuario(8019940,"Jose Georgive","Montero Angulo")
print(usuario_1.id)
print(usuario_1._nombre)
usuario_1.mostrar_apellido()
print(usuario_1._Usuario__apellidos)
