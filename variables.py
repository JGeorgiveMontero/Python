# Este programa calcula el area de un cuadrado

def calcular_area(lado):

    lado = float(input("entre el lado del cuadrado: "))

    area = lado*lado
    return area

calculo = calcular_area(4)
print(f"El area del cuadrado es: {calculo}")
