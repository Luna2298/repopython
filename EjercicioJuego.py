"""Ejercicio Juego.

Le hago preguntas matematicas a un jugador y este debe responder.
Segun su respuesta aumentara o disminura su puntaje. El jugador comenzara con el puntaje = 30.
Se le preguntara que tipo de operaciones quiere responder: suma, resta, multi, div.
Dependiendo el tipo de operacion, se le hara las preguntas matematicas correspondientes.
Tambien se le preguntara si desea continuar jugando o no.
Y una vez su puntaje sea menor a cero, quedara eliminado y sera informado.
Si alcanza llegar a 50 o mas, sera informado que ya supero y gano."""


import random

global bandera
global bandera2
bandera = True
bandera2 = True
global respuesta
respuesta = 0
global resultado
resultado = 0
global puntajeInicial
puntajeInicial = 30


def validarRespuestaSuma(respuesta, resultado, nro1, nro2):

    respuesta = int(input(f"Cuanto es {nro1} + {nro2}? : ")) 
    resultado = nro1 + nro2

    valido = True
    while valido:

        if respuesta.is_integer() : 
           validarResultado(respuesta, resultado) 
           valido = False

        else:
           print("Ingrese solo nros")
           valido = True
           respuesta = int(input(f"Cuanto es {nro1} + {nro2}? : "))
           

def validarRespuestaResta(respuesta, resultado, nro1, nro2):

    respuesta = int(input(f"Cuanto es {nro1} - {nro2}? : ")) 
    resultado = nro1 - nro2

    valido = True
    while valido:

        if respuesta.is_integer() : 
           validarResultado(respuesta, resultado) 
           valido = False

        else:
           print("Ingrese solo nros")
           valido = True
           respuesta = int(input(f"Cuanto es {nro1} - {nro2}? : "))



def validarRespuestaDiv(respuesta, resultado, nro1, nro2):

    respuesta = int(input(f"Cuanto es {nro1} / {nro2}? : ")) 
    resultado = nro1 / nro2

    valido = True
    while valido:

        if respuesta.is_integer() : 
           validarResultado(respuesta, resultado) 
           valido = False

        else:
           print("Ingrese solo nros")
           valido = True
           respuesta = int(input(f"Cuanto es {nro1} / {nro2}? : "))


def validarRespuestaMulti(respuesta, resultado, nro1, nro2):

    respuesta = int(input(f"Cuanto es {nro1} * {nro2}? : ")) 
    resultado = nro1 * nro2

    valido = True
    while valido:

        if respuesta.is_integer() : 
           validarResultado(respuesta, resultado) 
           valido = False

        else:
           print("Ingrese solo nros")
           valido = True
           respuesta = int(input(f"Cuanto es {nro1} * {nro2}? : "))


def validarResultado(respuesta, resultado):
    
    global puntajeInicial

    if resultado == respuesta:

        puntajeInicial += 5
        print("Correcto! Sumas 5 puntos")
    else:

        puntajeInicial -= 5
        print("Incorrecto! Restas 5 puntos")


def quiereContinuar():

    valido = True
    repetir = True

    while repetir:
        deseaContinuar = input("Desea continuar? (si, no): ")
        if deseaContinuar.strip().lower() == "si":
            repetir = False
            valido
        elif deseaContinuar.strip().lower() == "no":
           print(f"Puntaje final: {puntajeInicial}")
           repetir = False
           valido = False
        else:
           print("Respete, responda si o no")
           repetir
    
    return valido




    

while bandera:

    tipoOperacion = input("Que tipo de operacion matematica desea responder (suma, resta, div, multi)? : ")

    if not tipoOperacion.isdigit():

        respuesta = 0
        resultado = 0
        global nro1
        global nro2
        bandera2 = True

        nro1 = random.randint(1, 11)
        nro2 = random.randint(1, 11)

        while bandera2:
            
            if tipoOperacion.strip().lower() == "suma":
                
                validarRespuestaSuma(respuesta, resultado, nro1, nro2)
                
                if quiereContinuar():
                    bandera2 = False
                    bandera
                else:
                    bandera = False
                    break

            elif tipoOperacion.strip().lower() == "resta":

                validarRespuestaResta(respuesta, resultado, nro1, nro2)
                
                if quiereContinuar():
                    bandera2 = False
                    bandera
                else:
                    bandera = False
                    break

            elif tipoOperacion.strip().lower() == "div":

                validarRespuestaDiv(respuesta, resultado, nro1, nro2)
                
                if quiereContinuar():
                    bandera2 = False
                    bandera
                else:
                    bandera = False
                    break

            elif tipoOperacion.strip().lower() == "multi":

                validarRespuestaMulti(respuesta, resultado, nro1, nro2)
                
                if quiereContinuar():
                    bandera2 = False
                    bandera
                else:
                    bandera = False
                    break
            else:
                print("Ingrese una de las 4 operaciones")
                bandera2 = False
                bandera
    else:
        
        input("Respete el formato (enter)")

    if puntajeInicial <= 0:
        bandera = False
        print("Jugador Eliminado, su puntaje es 0")  
    elif puntajeInicial == 50:
        print(f"Has ganado! Tu puntaje es: {puntajeInicial}")   
        bandera = False








    