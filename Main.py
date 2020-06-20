#En el archivo de cada usuario, luego de escribir su estado actual, se agrega una lista de mensajes
#que han sido publicados por sus amigos, de manera de formar una lista de mensajes que llamaremos "muro", o 'timeline',

import social

social.mostrar_bienvenida()
nombre = social.obtener_nombre()
print("\nHola ", nombre, "bienvenido", end="\n")

if social.existe_archivo(nombre + ".user"):
    print("Leyendo datos de usuario", nombre, "desde archivo.", end="\n")
    (nombre, edad, estatura, genero, pais, amigos, estado, muro) = social.leer_usuario(nombre)
else:
    print()
    edad = social.obtener_edad()
    estatura = social.obtener_estatura()
    genero = social.obtener_genero()
    pais = social.obtener_pais()
    amigos = social.obtener_amigos()
    estado = ""
    muro = list()

print("Datos de tu perfil: ","-"*10, end="\n")
social.mostrar_perfil(nombre, edad, estatura,genero, pais, amigos)
social.mostrar_mensaje(nombre, estado)


#se muestra el menu y se consultan las opciones
opcion = 1
while opcion != 0:
    opcion = social.opcion_menu()

    if opcion == 1:
        estado = social.obtener_mensaje()
        social.publicar_mensaje(nombre, amigos, estado, muro)
    elif opcion == 2:
        social.mostrar_muro(muro)
    elif opcion == 3:
        social.mostrar_perfil(nombre, edad,estatura, genero, pais, amigos)
    elif opcion == 4:
        edad = social.obtener_edad()
        estatura = social.obtener_estatura()
        genero = social.obtener_genero()
        pais = social.obtener_pais()
        amigos = social.obtener_amigos()
        social.mostrar_perfil(nombre, edad, estatura, genero, pais, amigos)
    elif opcion == 0:
        print("Has decidido salir. Guardando perfil en ",nombre +".user", end="\n")
        social.escribir_usuario(nombre, edad, estatura, genero, pais, amigos, estado,muro)
        print("Archivo ",nombre+".user","guardado", end="\n")

print("¡Hasta pronto! :)")