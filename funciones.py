tareas=[]
def agregar_tareas(lista):
    
    tarea = input("Introduzca la descripcion de la tarea: ")
    lista.append(tarea)
    print("\n La tarea se añadio a la lista de tareas pendientes \n")
    print(f"la taraea añadida es: {tarea} ")
    print(f"La tarea se añadio en la posicion {len(lista)}\n ")

def ver_tareas(lista):
    if lista:
        for indice,tarea in enumerate(lista):
            print(f"{indice +1}.{tarea} \n")
    else:
        print("la lista no tiene tareas asignadas \n")
    print ("*******FIN DEL LISTADO *******\n")
def tarea_completada(lista):
    ver_tareas(lista)
    completada= int(input((" Introduzcca el numero de la tarea completada: ")))
    if completada > 0 and completada <= len(lista):
        if "(completada)" in lista [completada -1]:
            print(f"La Tarea {completada}  ya esta marcada como completada")
        else:
            lista [completada -1] = "(completada)" + lista[completada -1]
            print(f"Se marco la tarea {completada} como completada")
    else:
        print("Opcion invalida")    

def eliminar_tarea(lista):
    if lista:
        ver_tareas(lista)
        borrar_tarea = int(input("intoduzca el numero de la tarea que desea borrar: "))
        if borrar_tarea > 0 and borrar_tarea <= len(lista):
            del lista[borrar_tarea - 1]
            print(f"La tarea {borrar_tarea} fue eliminada de la lista")
        else:
            print(f"La tarea {borrar_tarea} no existe")
    else:
        print("La lista de tareas esta vacia")
