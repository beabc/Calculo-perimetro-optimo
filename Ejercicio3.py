# =============================================================================
# ~LIBRERÍAS A EMPLEAR
# =============================================================================
import numpy as np
import math
import random
from operator import itemgetter
from collections import OrderedDict
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go
import matplotlib.pyplot as plt

# =============================================================================
# FUNCIONES DESARROLLADAS
# =============================================================================
#1.- Introducción aleatoria de puntos con dos coordenadas:
def bosque ():
    num= int(input('¿Cuántos árboles desea introducir?'))
    
    arboles = dict()
    for n in range(num):
        punto= np.random.randint(-10000, 10000, 2)
        arboles[n] = punto
    
    return arboles

#2.- Cálculo del primer punto del perímetro:
def primer_punto(dicci):
    p = sorted(dicci.items(), key = lambda x: x[1][0])[0][0]
    
    return p

#3.-Cálculo del perímetro más óptimo:
def determinar_cuadrante(posicion1,posicion2,diccionario):
    if diccionario[posicion2][0] >= diccionario[posicion1][0]:
        if diccionario[posicion2][1] >= diccionario[posicion1][1]:
            cuadrante = 1
        else:
            cuadrante = 2
    else:
        if diccionario[posicion2][1] >= diccionario[posicion1][1]:
            cuadrante = 4
        else:
            cuadrante = 3
    
    return cuadrante


def calculo_siguiente_punto(posicion,diccionario,cuadrante_ant):
    pend=dict()
    for i in range(1,5):
        pend[i] = dict()
    
    for p in range(len(diccionario)):
        cuadrante = determinar_cuadrante(posicion, p, diccionario)
        if p != posicion:
            pend[cuadrante][p] = math.degrees(math.atan((diccionario[p][1] - diccionario[posicion][1])/(diccionario[p][0] - diccionario[posicion][0])))

#    print('Ángulos calculados:' , pend)
    nuevo_punto = -1
    for cuad in range(1,5):
#        print('Tamaño cuadrante:',cuad, len(pend[cuad]))
        if len(pend[cuad]) > 0 and cuad >= cuadrante_ant:
            lista_ordenada= sorted(pend[cuad], key = pend[cuad].get, reverse = True)
            nuevo_punto = lista_ordenada[0]
            break
    if nuevo_punto == -1:
        #Tiene que volver a buscar en cuadrante I (Serán los puntos en su vertical)
        cuad = 1
        lista_ordenada= sorted(pend[cuad], key = pend[cuad].get, reverse = True)
        nuevo_punto = lista_ordenada[0]

    return nuevo_punto, cuad

#4.- Representación gráfica:
def dibujar_perimetro(arbol,perimetro):
    #Dibujamos el bosque
    x_arbol= list()
    y_arbol= list()
    for a in range(len(arbol)):
        x_arbol.append(arbol[a][0])
        y_arbol.append(arbol[a][1])
        
    #Dibujamos la valla
    x_per = list()
    y_per = list()
    for pos in range(len(perimetro)):
        posicion = perimetro[pos]
        x_per.append(arbol[posicion][0])
        y_per.append(arbol[posicion][1])
    
    plt.scatter(x_arbol, y_arbol, c ='green')
    plt.plot( x_per, y_per, linestyle= '--',c ='black')
    plt.xlabel('Bosque')
    plt.ylabel('Bosque')
    plt.show()
    

#---------------------------------------------------------------------------------#
arboles =bosque()

perimetro =dict()

punto_inicio = primer_punto(arboles)
perimetro[0] = punto_inicio
nuevo_punto = -1
direccion = 1

while punto_inicio != nuevo_punto:
    punto_aconsultar= perimetro[len(perimetro) -1]
    nuevo_punto,direccion = calculo_siguiente_punto(punto_aconsultar,arboles, direccion)
    perimetro[len(perimetro)] = nuevo_punto

    
print('Perímetro hallado', perimetro)
    
dibujar_perimetro(arboles, perimetro)





