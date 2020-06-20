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

def obtener_mensaje():
    mensaje = input("¿Qué piensas hoy? ")
    return mensaje

def mostrar_mensaje(origen, mensaje):
    print("-"*25)
    print(origen+":", mensaje)
    print("-" * 25)

#Muestra los mensajes recibidos
def mostrar_muro(muro):
     print("------ MURO ("+str(len(muro))+" mensajes) ---------")
     for mensaje in muro:
         print(mensaje)
     print("-" * 25)

#Verifica que exista el archivo del usuario
def existe_archivo(ruta):
    return os.path.isfile(ruta)

#Publica un mensaje en el timeline personal y en el de los amigos
def publicar_mensaje(origen, amigos, mensaje, muro):
    print("-" * 25)
    print(origen, "dice:", mensaje)
    print("-" * 25, end="\n")
    #Agrega el mensaje al final del timeline local
    muro.append(mensaje)
    #Agrega, al final del archivo de cada amigo, el mensaje publicado
    for amigo in amigos:
        if existe_archivo(amigo+".user"):
            archivo = open(amigo+".user","a")
            archivo.write(origen+":"+mensaje+"\n")
            archivo.close()

def leer_usuario(nombre):
    archivo_usuario = open(nombre+".user","r")
    nombre = archivo_usuario.readline().rstrip()
    edad = int(archivo_usuario.readline())
    estatura = float(archivo_usuario.readline())
    genero = archivo_usuario.readline().rstrip()
    pais = archivo_usuario.readline().rstrip()
    amigos = archivo_usuario.readline().rstrip().split(",")
    estado = archivo_usuario.readline().rstrip()
    #Lee el 'muro'. Esto es, todos los mensajes que han sido publicados en el timeline del usuario.
    muro = list()
    mensaje = archivo_usuario.readline().rstrip()
    while mensaje != "":
        muro.append(mensaje)
        mensaje = archivo_usuario.readline().rstrip()
    archivo_usuario.close()
    return(nombre, edad, estatura, genero, pais, amigos, estado, muro)

def escribir_usuario(nombre, edad, estatura,genero, pais, amigos, estado, muro):
    archivo_usuario = open(nombre+".user","w")
    archivo_usuario.write(nombre+"\n")
    archivo_usuario.write(str(edad)+"\n")
    archivo_usuario.write(str(estatura)+"\n")
    archivo_usuario.write(genero+"\n")
    archivo_usuario.write(pais+"\n")
    archivo_usuario.write(",".join(amigos)+"\n")
    archivo_usuario.write(estado+"\n")
    #Escribe el 'timeline' en el archivo, a continuación del último estado
    for mensaje in muro:
        archivo_usuario.write(mensaje+"\n")
    
    archivo_usuario.close()