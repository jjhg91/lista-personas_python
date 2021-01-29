import os

### TE PIDE EN PANTALLA LOS DISTINTOS DATOS QUE PUEDES AGREGAR
def agregar():   
    print("         by Juan Herrera \n ")
    nombre = input("Agregar Primer Nombre: ")
    apellido = input("Agregar Primer Apellido: ")
    cedula = input("Agregar cedula de indentidad: ")
    inf = nombre+" "+apellido+" "+cedula
    if ' ' in nombre or ' ' in apellido or ' ' in cedula:
        os.system('cls')
        print('por favor sin espacios, vuelva a intentarlo')
        return 99
    return inf