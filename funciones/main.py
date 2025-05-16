from Paquete_curso.Funciones_Calculadora import *


operacion = input("Indicar que operación desea realizar con su numero[suma(1), resta(2), multiplicacion(3), division(4)]: ")
operacion = int(operacion)

while operacion < 1 or operacion > 4:
    operacion = input("ERROR. Indicar un número valido de operacion [suma(1), resta(2), multiplicacion(3), division(4)]: ")
    operacion = int(operacion)

numero_a = float(input("Introducir el primer número: "))

numero_b = float(input("Introducir el segundo número: "))


match operacion:
    case 1:
        print(suma(numero_a, numero_b))
    case 2:
        print(resta(numero_a, numero_b))
    case 3:
        print(multiplica(numero_a, numero_b))
    case 4:
        if numero_b == 0:
            print("ERROR MATEMATICO. No es posible dividir entre 0")
        else:
            print(divide(numero_a, numero_b))



