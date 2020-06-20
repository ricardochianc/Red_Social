import os

def mostrar_bienvenida():
    print(""" __            _       _     __          _ 
/ _\ ___   ___(_) __ _| |   /__\ ___  __| |
\ \ / _ \ / __| |/ _` | |  / \/// _ \/ _` |
_\ \ (_) | (__| | (_| | | / _  \  __/ (_| |
\__/\___/ \___|_|\__,_|_| \/ \_/\___|\__,_|""" )

def obtener_nombre():
    nombre = input("Dinos como te llamas ")
    return nombre

def obtener_edad():
    anio = int(input("¿En qué año naciste? "))
    return 2020-anio-1

def obtener_estatura():
    estatura = float(input("¿Cuánto mides en metros? "))
    metros = float(estatura)
    return metros

def obtener_genero():
    genero = input("Ingresa tu sexo: M=masculino, F=Femenino: ")
    
    while genero != "M" and genero != "F":
        genero = input("Ingresa tu sexo: M=masculino, F=Femenino: ")
    
    return genero

def obtener_pais():
    pais = input("Indica tu país de nacimiento: ")
    return pais

def obtener_amigos():
    linea = input("Escrib una lista con los nombres de tus amigos, separalos con coma ',':")
    lista_amigos = linea.split(',')
    return lista_amigos

def mostrar_perfil(nombre, edad, estatura, genero, pais, amigos):
    
    print("" * 25, end="\n")
    print("Nombre:    ", nombre)
    print("Edad:      ", edad, "años")
    print("Estatura:  ", estatura, "m")
    print("Pais:      ", pais)
    print("Amigos:    ", len(amigos))
    print("" * 25, end="\n")

def opcion_menu():
    print("Menú:", "-"*15)
    print("  1. Escribir un mensaje")
    print("  2. Mostrar mi muro")
    print("  3. Mostrar los datos de perfil")
    print("  4. Actualizar el perfil de usuario")
    print("  0. Salir")
    opcion = int(input("Ingresa una opción: "))
    while opcion < 0 or opcion > 5:
        print("Inténtalo otra vez.")        
        opcion = int(input("Ingresa una opción: "))
    return opcion