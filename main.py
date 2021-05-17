from scipy import misc
from math import *
import random
import numpy as np
import matplotlib.pyplot as plt
import solutions

# Import A Star class
import A_Star


# Se procesa el mapa y se obtiene el punto de inicio, final y matriz binarizada
## Map processing.
## @param imagen: path a la imagen del mapa
## @return (m_plan, init, goal)
## m_plan: mapa en forma de matriz binarizada
## init  : punto de inicio del recorrido
## goal  : punto final del recorrido

def map_process(imagen):
    m_imagen = misc.imread(imagen)
    m_plan = np.zeros((len(m_imagen),len(m_imagen[0])))
    for i in range(len(m_imagen)):
        for j in range(len(m_imagen[0])):
            if (m_imagen[i][j] > 200 ):
                m_plan[i][j] = 1
    return m_plan

# Read database
file_data = open('database.log')
file_data_lines = file_data.readlines()
data = []
for i in file_data_lines:
    data.append(i.replace('\n','').split())

soluciones = []
for i in data:
    m_plan = map_process('maps/'+i[0])

    init = [int(i[1]),int(i[2])]
    goal = [int(i[3]),int(i[4])]
    ####################
    # A Star Algorithm
    ####################
    # Creamos el objeto A_Star
    path = A_Star.A_Star(m_plan,init,goal)
    # Aplicamos el algoritmo segun la matriz, punto de inicio y punto final
#    try:
    path.astar()
    # Suavizamos el trayecto
    path.smooth(0.5,0.15)
    path_hard = path.path
    path_soft = path.spath
    print('path_soft: {}'.format(path_soft))
    print('path_hard: {}'.format(path_hard))
    # Plot grid and path
    x_soft = np.array(path_soft)[0::,0]
    y_soft = np.array(path_soft)[0::,1]
    x_hard = np.array(path_hard)[0::,0]
    y_hard = np.array(path_hard)[0::,1]
    x_grid = []
    y_grid = []
    for i in range(len(path.grid)):
        for j in range(len(path.grid[0])):
            if (path.grid[i][j] == 1):
                y_grid.append(j)
                x_grid.append(i)
    soluciones.append(path.path)
    plt.plot(x_grid,y_grid,'ro')
    plt.plot(x_soft,y_soft,'bo-')
    plt.plot(x_hard,y_hard,'go-')
    plt.show()
#    except:
#        x_grid = []
#        y_grid = []
#        print " %s : Error calculando A Star" % i[0]
#        for i in range(len(path.grid)):
#            for j in range(len(path.grid[0])):
#                if (path.grid[i][j] == 1):
#                    y_grid.append(j)
#                    x_grid.append(i)
#        plt.plot(init[0],init[1],'yo')
#        plt.plot(goal[0],goal[1],'co' )
#        plt.plot(x_grid,y_grid,'ro')
#        plt.show()

if (solutions.soluciones_golden == soluciones ):
    print "Soluciones correctas. Ejercicio Terminado"
else:
    print "Una o mas soluciones son incorrectas."
