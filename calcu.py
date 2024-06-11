import calculadora_suma
import RESTA
import Funcion_Multiplicacion
import calculadora_divicion
import raiz
# main.py



def mostrar_menu():
    print("Suma {1}")
    print("Resta {2}")
    print("Multiplicación {3}")
    print("División {4}")
    print("Raíz cuadrada {5}")

def main():
    mostrar_menu()
    opcion = int(input("Elija su modo: "))

    if opcion == 1:
        calculadora_suma.suma()
    elif opcion == 2:
        RESTA.resta()
    elif opcion == 3:
        Funcion_Multiplicacion.multiplicacion()
    elif opcion == 4:
        calculadora_divicion.divicion()
    elif opcion == 5:
        raiz.raiz()
    else:
        print("Opción no válida")

if __name__ == "__main__":
    main()
