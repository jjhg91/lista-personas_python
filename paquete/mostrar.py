
### RECIBE UNA LISTA DE DATOS Y LOS MUESTRA EN PANTALLA UNO POR UNO
def mostrar(data):
    n=0
    print("         by Juan Herrera \n ")
    for colum in data:
        print(str(n)+'. '+colum)
        n+=1
    