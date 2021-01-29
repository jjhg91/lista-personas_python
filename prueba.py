#!/usr/bin/env python
###IMPORTA TODOS LOS PEDASOS  DE CODIGOS QUE ESTAN EN LA CARPETA PAQUETE
import os
from paquete.mostrar import *
from paquete.agregar import *
from paquete.editar import *
from paquete.eliminar import *


### FUNCION MENU IMPRIME EL MENU EN PANTALLA Y 
### RECIBE LA VARIABLE QUE SELECCIONARA LA FUNCION A EJECUTAR
def menu(error=''):
    os.system("cls")
    print("         by Juan Herrera \n ")
    print("0. Mostrar")
    print("1. Agregar Nuevo")
    print("2. Editar")
    print("3. Eliminar")
    print("4. Guardar y Salir")
    if error != '':
        #print('')
        print('\n'+error)
    opc = input("Elije: ")
    return opc

### SE GUARDA EL NOMBRE DEL ARCHIVO LUEGO SE BUSCAN ERRORES 
### SE INTENTA ABRIR, SI EL ARCHIVO NO EXISTE SALTA UN ERROR 
### PARA LUEGO CREAR EL ARCHIVO
name = 'wuilman.txt'
try:
    archivo=open(name, 'r')
    a = archivo.read()
    archivo.close()
    lista = a.split('\n')
    lista.remove('')
except FileNotFoundError:
    archivo = open(name, 'w')
    archivo.close()
    lista = []


### SE HACE UN BUCLE PARA VER QUE OPCION SE SELECCIONO EN EL MENU
### Y ASI ABRIR DICHA FUNCION QUE SE ENCUENTRA EN LA CARPETA PAQUETE
error = ''
while True:
    opcion=menu(error)
    ### LLAMA A LA FUNCION MOSTRAR PARA MOSTRAR LA BASE DE DATOS
    if opcion == '0':
        os.system('cls')
        mostrar(lista)
        cont=input('cualquier tecla para continuar...')
        os.system('cls')
        continue

    ### LLAMA A LA FUNCION AGREGAR PARA AGREGAR UN NUEVO DATO A LA BASE DE DATOS
    elif opcion == '1':
        os.system('cls')
        aa = agregar()
        if  aa == 99:
            pass
        else:
            lista.append(aa)
        cont=input('cualquier tecla para continuar...')
        os.system('cls')
        continue
    ### LLAMA A LA FUNCION EDITAR PARA ESTIDAR LOS DATOS YA GUARDADOS
    elif opcion == '2':
        os.system('cls')
        edit = editar(lista)
        lista = edit
        cont=input('cualquier tecla para continuar...')
        os.system('cls')
        continue
    ### LLAMA A LA FUNCION ELIMINAR UN DATO DE LA BASE DE DATOS 
    elif opcion == '3':
        os.system('cls')
        eliminar(lista)
        cont=input('cualquier tecla para continuar...')
        os.system('cls')
        continue
    ###  GUARDA LOS CAMBIOS Y SE CIERRA
    elif opcion == '4':
        archivo = open(name,'w')
        for art in lista:
            archivo.write(art+'\n')
        archivo.close()

        break
    ### SI NO ESCOGISTE UNA OPCION VALIDA VUELVE A EJECUTAR EL MENU Y TE MUESTRA UN ERROR
    else:
        error = 'Has seleccionado una opcion invalida, vuelve a intentarlo!'
        continue
    error=''
### LIMPIA LA PANTALLA Y TE DA UN MENSAJE DE DESPEDIDA
os.system('cls')
print("         by Juan Herrera \n ")
print('EXITO! se a guardado, Vuelve pronto...')

