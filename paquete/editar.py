import os
from paquete.mostrar import *
from paquete.agregar import *

### MUESTRA UNA LISTA EN PANTALLA DE TODOS LOS DATOS 
### SELECCIONAS EL QUE QUIERES EDITAR Y SELECCIONAS EL CAMPO
### QUE QUEIRES EDITAR
def editar(lis):
    
    lista = []
    lista = lis
    mostrar(lista)
    edit = input("numero a editar: ")
    camp = input("que quieres editar (0.nombre, 1.apellido, 2.cedula): ")
    inf = input("nuevo dato: ")
    if ' ' in inf:
        os.system('cls')
        print('por favor sin espacios, vuelva a intentarlo')
        return lista
    a = str(lista[int(edit)]).split(" ")
    if ' ' in a:
         a.remove('')
    
    a[int(camp)] = inf
    lista[int(edit)]=a[0]+" "+a[1]+" "+a[2]
    return lista
