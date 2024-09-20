from collections import Counter
import random
import string
import numpy as np # type: ignore


num_bacterias = 8
num_iteraciones = 10
num_pasos_quimiotacticos = 20


lg ='======================================================================================'
sg = '----------------'

def formatear_bacterias(bacterias): 
    bacteria_np = np.array(bacterias)
    formatted_bacteria = np.array2string(bacteria_np, separator=' | ',max_line_width=np.inf , formatter={'str_kind': lambda x: x})

    return formatted_bacteria


def imprimir_bacterias(bacterias, puntuacion):
    print(lg)
    
    for i in range (len(bacterias)):
        print(f"Bacteria {i+1}: \n{formatear_bacterias(bacterias[i])} \n  con puntuación {puntuacion[i]}")
    print(lg)
    print("\n")

def creacion_bacterias(num_bacterias, secuencias_geneticas):
    max_len = len(max(secuencias_geneticas, key=len))+1
    bacterias = []
    for _ in range(num_bacterias):
        bacteria = random.sample(secuencias_geneticas, len(secuencias_geneticas))
        bacteria = [seq.ljust(max_len, '-') for seq in bacteria]
        bacterias.append(bacteria)

    for bacteria in range(len(bacterias)):
        for secuencia in range(len(bacterias[bacteria])):
            bacterias[bacteria][secuencia] = list(bacterias[bacteria][secuencia])
    return bacterias


def calcular_puntuacion_columna(lista):
    letras = [letra for letra in lista if letra in string.ascii_letters]
    conteo_letras = Counter(letras)
    max_conteo = max(conteo_letras.values(), default=0)
    puntuacion =(max_conteo - 1) ** 2
    if max_conteo == 1 or max_conteo==0:
        return 0
    return puntuacion

def puntuacion_bacteria(bacteria):
    total_puntuacion = 0
    num_columnas = len(bacteria[0])

    for col in range(num_columnas):
        lista = [word[col] for word in bacteria]
        puntuacion = calcular_puntuacion_columna(lista)
        #print(f"     Columna {col}: {lista} | Puntuación : {puntuacion}")
        total_puntuacion += puntuacion
        lista.clear()

    return total_puntuacion

def TumboNado2(secuencia):
    indices_guiones = [i for i, x in enumerate(secuencia) if x == '-']
    if not indices_guiones:
        return secuencia

    indice_guion = random.choice(indices_guiones)
    secuencia.pop(indice_guion)

    posiciones_validas = [i for i in range(len(secuencia) + 1)]

    nueva_posicion = random.choice(posiciones_validas)
    secuencia.insert(nueva_posicion, '-')

    return secuencia

def procesar_bacterias(bacteria, puntuacion):
    print(lg)

    print(f"Procesando bacteria: \n{formatear_bacterias(bacteria)}")
    print(f"Total de puntuación: {puntuacion} ")
    print(f'{sg}Inicializando quimiotaxis{sg}')

    for i in range(num_pasos_quimiotacticos):
        print(f"\n    Quimiotaxis {i+1}/{num_pasos_quimiotacticos}")
        
        bacteria_T = [TumboNado2(list(bacteria[secuencia])) for secuencia in range(len(bacteria))]
        
        nueva_puntuacion = puntuacion_bacteria(bacteria_T)
        print(f"{formatear_bacterias(bacteria_T)} \n        puntuación: {nueva_puntuacion} ")
        
        if nueva_puntuacion > puntuacion:
            bacteria = bacteria_T
            puntuacion = nueva_puntuacion

            print(f"    Se ha mejorado la puntuación de la bacteria nos cambiamos a: \n{formatear_bacterias(bacteria)} ")
        else :
            
            print(f"    No se ha mejorado la puntuación de la bacteria nos quedamos en: \n{formatear_bacterias(bacteria)}")
            
    print(f'{sg}Fin de la quimiotaxis{sg}')
    print(f"Despues de quimioxis  \n{formatear_bacterias(bacteria)} \n  Total de puntuación: {puntuacion}")
    return bacteria, puntuacion

def reproduccion(bacterias, puntuaciones):
    bacterias_puntuaciones = list(zip(bacterias, puntuaciones))
    bacterias_puntuaciones.sort(key=lambda x: x[1], reverse=True)
    bacterias_ordenadas, puntuaciones_ordenadas = zip(*bacterias_puntuaciones)

    n = len(bacterias)
    mitad = n // 2

    mejores_bacterias = list(bacterias_ordenadas[:mitad])
    mejores_puntuaciones = list(puntuaciones_ordenadas[:mitad])

    resultado_bacterias = mejores_bacterias 
    resultado_puntuaciones = mejores_puntuaciones

    # print (f'{sg} Inicio reproduccion {sg}')
    # print(f"Las MEJORES bacterias son: ")
    # imprimir_bacterias(mejores_bacterias, mejores_puntuaciones)

    # print(f"el resultado seria : ")
    # imprimir_bacterias(resultado_bacterias, resultado_puntuaciones)
    # print (f'{sg} Fin reproduccion {sg}\n')

    return resultado_bacterias, resultado_puntuaciones






#ejemplo de uso chafa
# secuencias_geneticas = [ "murcielago",'perro','gato', 'perico' ]
# bacterias = creacion_bacterias(num_bacterias, secuencias_geneticas)
# puntuacion = [puntuacion_bacteria(bacteria) for bacteria in bacterias]



# for i in range(num_iteraciones):
#     iteracion = i+1
#     print(f"Inicio de la iteracion {iteracion}/{num_iteraciones}:")
#     imprimir_bacterias(bacterias, puntuacion)

#     for j in range(num_bacterias):
#         print(f"Bacteria {j+1}:")
#         bacterias[j], puntuacion[j]=procesar_bacterias(bacterias[j], puntuacion[j])
#         print("\n")

#     print(f"Final de la iteracion {iteracion}/{num_iteraciones}:")

#     imprimir_bacterias(bacterias, puntuacion)
#     bacterias, puntuacion = reproduccion(bacterias, puntuacion)
