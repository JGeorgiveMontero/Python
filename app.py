import funciones
while True:

    print("\n********** Gestor de tareas de Consola  *******\n")
    print("1. Añadir Tarea")
    print("2. Ver Tareas")
    print("3. Marcar Tarea como Completada")
    print("4. Eliminar Tarea")
    print("5. Salir")
    print("\n")
    opcion = int(input("Introduzca una opcion: "))
    print("\n")
    if   opcion == 1:
        funciones.agregar_tareas(funciones.tareas)             
    elif opcion == 2:
        funciones.ver_tareas(funciones.tareas)
    elif opcion == 3:
        funciones.tarea_completada(funciones.tareas)
    elif opcion == 4:
        funciones.eliminar_tarea(funciones.tareas)
    elif opcion == 5:
        print("Gracias por utilizar el gestor de tareas, estoy desconectando")
        break           
    else:
        print("Verifique por favor, opcion invalida")
        