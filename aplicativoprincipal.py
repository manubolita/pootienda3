from leer import *
from producto import *
from venta import *
from factura import *
from tienda import *
import os
def crear_tienda():
    tienda=Tienda([],[])
    tienda.adicionar_productos()
    return tienda
def menuPrincipal():
    creado=False
    while True:
        os.system("cls")
        print("            Menu Principal            ")
        print("-------------------------------------")
        print("1.Cargar producto tienda")
        print("2.Mostrar productos")
        print("3.Realizar ventas")
        print("4.Realizar pedidos")
        print("5.Estadísticas")
        print("6.Salir")
        opcion=int(input("Opcion-> "))
        match opcion:
            case 1: 
                if not creado:
                    tienda=crear_tienda()
                    creado=True
                else:
                    print('Productos ya cargados')

                os.system("pause")
            case 2:
                if creado==True:
                    tienda.mostrar_productos()
                os.system("pause")
            case 3:
                menuVentas()
                os.system("pause")
            case 4:
                menuPedido()
                os.system("pause")
            case 5:
                menuEstadisticas()
                os.system("pause")  
            case 6:
                print("Fin del programa")
                break

            case other:
                print("El numero digitado no esta disponible")
                os.system("pause")
menuPrincipal()