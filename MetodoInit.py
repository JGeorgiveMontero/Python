class Usuario:
    def __init__(self,
                nombre,
                apellidos,
                edad,
                direccion,
                telefono):
        self.nombre= nombre
        self.apellido = apellidos
        self.edad = edad
        self.direccion = direccion
        self.telefono = telefono

    def iniciar_sesion(self):
        print(f"El usuario {self.nombre} ha iniciado sesion")
    def cerrar_sesion(self):
        print("El usuario ha cerrado sesion")
    def cambiar_nombre_perfil(self):
        print("Se cambio el nombre al perfil")

usuario1 = Usuario("Enrique","Montero Angulo",60,"Luis Fargier",4147662513)
print(usuario1.apellido) 
Usuario.iniciar_sesion(usuario1)
usuario1.iniciar_sesion()
