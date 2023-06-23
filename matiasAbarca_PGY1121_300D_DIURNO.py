import os
import time
import sys
import random


datos_vehiculo = []
patentes = []


def borrarPantalla():
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")


def grabar():
    print("-- GUARDAR DATOS VEHICULO --\n")

    tipo = input("Ingrese tipo de vehiculo: ")
    print("")

    patente = input("Ingrese patente vehiculo: ")
    while len(patente) > 6 or len(patente) < 0:
        print("\nERROR: Patente no valida")
        time.sleep(1)
        borrarPantalla()
        print("-- GUARDAR DATOS VEHICULO --\n")
        print(f"Ingrese tipo de vehiculo: {tipo}\n")

        patente = input("Ingrese patente de vehiculo: ")
    print("")

    marca = input("Ingrese marca vehiculo: ")
    while len(marca) > 15 or len(marca) < 2:
        print("\nERROR: La marca debe contener entre 2 y 15 caracteres")
        time.sleep(1)
        borrarPantalla()
        print("-- GUARDAR DATOS VEHICULO --\n")
        print(f"Ingrese tipo de vehiculo: {tipo}\n")
        print(f"Ingrese patente vehiculo: {patente}\n")

        marca = input("Ingrese marca vehiculo: ")
    print("")

    try:
        precio = int(input("Ingrese precio vehiculo: "))
        while precio < 5_000_000:
            print("\nERROR: El precio debe ser superior a $5.000.000")
            time.sleep(1)
            borrarPantalla()
            print("-- GUARDAR DATOS VEHICULO --\n")
            print(f"Ingrese tipo de vehiculo: {tipo}\n")
            print(f"Ingrese patente vehiculo: {patente}\n")
            print(f"Ingrese marca vehiculo: {marca}\n")

            precio = input("Ingrese marca vehiculo: ")
    except:
        ValueError
    print("")

    try:
        multa_monto = int(input("Ingrese monto multa (si no tiene ingrese ´0´): "))
    except:
        ValueError
    print("")
    multa_fecha = input("Ingrese fecha multa (si no tiene ingrese ´0´): ")
    print("")

    fecha_registro = input("Ingrese fecha registro vehiculo: ")
    print("")

    nombre_duenyo = input("Ingrese nombre dueño vehiculo: ")

    tipo = tipo.capitalize()
    nombre_duenyo = nombre_duenyo.capitalize()
    marca = marca.capitalize()
    patente = patente.upper()

    patentes.append(patente)
    datos_vehiculo.append([tipo, patente, marca, precio, multa_monto, multa_fecha, fecha_registro, nombre_duenyo])


def buscar_patente():
    print("-- BUSCAR PATENTE VEHICULO --\n")
    patente_x = input("Ingrese patente vehiculo a buscar: ")
    while len(patente_x) > 6 or len(patente_x) < 0:
        print("\nERROR: Patente no valida")
        time.sleep(1)
        borrarPantalla()
        print("-- BUSCAR PATENTE VEHICULO --\n")
        patente_x = input("Ingrese patente vehiculo a buscar: ")
    patente_x = patente_x.upper()

    if patente_x in patentes:
        borrarPantalla()
        resultado = datos_vehiculo[patentes.index(patente_x)]

        print(f"-- MOSTRANDO DATOS SOLICITADOS PARA #{patente_x} --\n")
        print(f"Tipo de vehiculo: {resultado[0]}")
        print(f"Patente: {resultado[1]}")
        print(f"Marca vehiculo: {resultado[2]}")
        print(f"Precio vehiculo: {resultado[3]}")
        print(f"Monto multa: {resultado[4]}")
        print(f"Fecha multa: {resultado[5]}")
        print(f"Fecha registro: {resultado[6]}")
        print(f"Nombre dueño: {resultado[7]}")

        print("")
        input("# pulse 'enter' para salir #")
    else:
        print("\n❌ Vehiculo no registrado ❌")
        time.sleep(1.5)
        borrarPantalla()


def imprimir_certificado():
    print("-- IMPRIMIR CERTIFICADOS --\n")
    patente_x = input("Ingrese patente vehiculo: ")
    while len(patente_x) > 6 or len(patente_x) < 0:
        print("\nERROR: Patente no valida")
        time.sleep(1)
        borrarPantalla()
        print("-- IMPRIMIR CERTIFICADOS --\n")
        patente_x = input("Ingrese patente vehiculo: ")
    patente_x = patente_x.upper()

    if patente_x in patentes:
        borrarPantalla()
        resultado = datos_vehiculo[patentes.index(patente_x)]

        print("-- IMPRIMIR CERTIFICADOS --\n")
        print("# seleccione tipo de certificado #\n")
        print("1 - emisión de contaminantes")
        print("2 - anotaciones vigentes")
        print("3 - multas")
        print("")
        opcion_usuario = input(">> ")
        borrarPantalla()

        match opcion_usuario:
            case "1":
                valor = random.randint(1500, 3500)

                print("CERTIFICADO EMISIÓN DE CONTAMINANTES\n\n")
                print(f"Patente vehiculo: {resultado[1]}")
                print(f"Dueño vehiculo: {resultado[7]}")
                print(f"Total a pagar: ${valor}")
                print("")
                print("CAUSAL:\n *sample text*")

            case "2":
                valor = random.randint(1500, 3500)

                print("ANOTACIONES VIGENTES\n\n")
                print(f"Patente vehiculo: {resultado[1]}")
                print(f"Dueño vehiculo: {resultado[7]}")
                print(f"Total a pagar: ${valor}")
                print("")
                print("CAUSAL:\n *sample text*")

            case "3":
                valor = random.randint(1500, 3500)

                print("MULTAS\n\n")
                print(f"Patente vehiculo: {resultado[1]}")
                print(f"Dueño vehiculo: {resultado[7]}")
                print(f"Total a pagar: ${valor}")
                print("")
                print("CAUSAL:\n *sample text*")
    else:
        print("\n❌ Vehiculo no registrado ❌")
        time.sleep(1.5)
        borrarPantalla()


def menu():
    print("/// 🚦 AUTO SEGURO 🚦 ///")
    print("")
    print(" -- ingrese una opcion -- ")
    print("")
    print("1 - grabar datos vehiculo")
    print("2 - buscar vehiculo")
    print("3 - imprimir certificados")
    print("4 - salir")
    print("")
    opcion_usuario = input(">> ")
    borrarPantalla()

    match opcion_usuario:
        case "1":
            grabar()
        case "2":
            buscar_patente()
        case "3":
            imprimir_certificado()
        case "4":
            print("¡Gracias por preferirnos!")
            print("Que tenga un buen viaje 😎🚗")
            print("\n\n")
            print("Desarrolador: Matias Abarca")
            print("Versión del sistema: 0.1")
            print("\nmodelo sujeto a cambios")
            time.sleep(2)
            sys.exit()


while True:
    borrarPantalla()
    menu()
    