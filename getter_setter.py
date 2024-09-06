class Usuario:
    def __init__(self,id,nombre,edad):
        self.id =id
        self.nombre = nombre
        self.__edad = edad

#Getter

    def obtener_edad(self):
        return self.__edad
#Setter

    def colocar_edad(self,edad):
        self.__edad = edad

usuario_1 = Usuario(8019940,"Jose",62)
edad_usuario = usuario_1.obtener_edad()
print(edad_usuario)

usuario_1.colocar_edad(64)

print(usuario_1.obtener_edad())


