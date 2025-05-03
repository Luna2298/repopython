"""Generar un nro, y pedirle al usuario que ingrese un valor, ver si coincide y de ser asi, decirle que gano,
de lo contrario, dejar volver a ingresar otro valor al usuario. Solo tendra 3 intentos. Una vez
acabados los 3 intentos decirle que ya perdio."""

import random


print("Juego: Adivinar el numero generado!\n")
print("Instrucciones: tendras que adivinar que nro genero el programa, en un rango del 1 - 10, \n" \
"te permitire ingresar 1 nro en cada intento, solo tendras 3 oportunidades\n")

diccionario = {1: "Feliciades ganaste!", 2 : "Se terminaron tus intentos. Perdiste!", 
               3 : "Vuelve a intentar!", 
               4 : "Formato incorrecto, solo ingrese un nro", 
               5 : "Adivinaste el valor. ", 
               6 : "El nro ingresado es MENOR al nro generado. ",
               7 : "El nro ingresado es MAYOR al nro generado. ",
               8 : "El valor a adivinar era: ",
               9 : "Intentos que aun te quedan: ",
               10 : "El rango debe ser entre 1 - 10"}

nro = random.randint(1, 10)
maxIntentos = 3

while (maxIntentos > 0):
    
    try:
        
        respuesta = int(input("Ingrese un nro entre 1 y 10: "))
        
        if respuesta > 0 and respuesta < 11:

            maxIntentos-=1
            if respuesta == nro:
                print(diccionario[5] + diccionario[1])
                break
        
            elif respuesta < nro:
                print(diccionario[6] + "\n" + diccionario[9] + f"{maxIntentos}" + "\n" + diccionario[3] + "\n")
            else: 
                print(diccionario[7] + "\n" + diccionario[9] + f"{maxIntentos}" + "\n" + diccionario[3] + "\n")
        
        else:
            print(diccionario[10] + "\n")
    
    except ValueError:
        print(diccionario[4] + "\n" + diccionario[3] + "\n")
        continue

    if maxIntentos == 0:
        print(diccionario[2] + "\n" + diccionario[8] + f"{nro}")



