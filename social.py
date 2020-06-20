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

