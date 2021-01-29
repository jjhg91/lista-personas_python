from paquete.mostrar import *

### MUESTRA TODOS LOS DATOS EN PANTALLA PARA QUE ASI SELECCIONES
### EL QUE SE VA A ELIMINAR
def eliminar(lis):
    lista=[]
    lista = lis
    mostrar(lista)
    edit=input("numero a eliminar: ")
    lista.remove(lista[int(edit)])
    return lista