import numpy as np
import math

THETA_STACK = 50 # numero de porciones que tiene el stack de thetas

class A_Star:

    def __init__(self, grid, init,goal, cost = 1):
        self.cost = cost
        self.grid = grid
        self.init = init
        self.goal = goal
        self.make_heuristic(grid, goal, self.cost)
        self.path = []
        self.spath = []
        self.action = []

    # ----------------------------------------
    # TODO: Crear la funcion heuristica para el grid
    # ----------------------------------------

    def make_heuristic(self, grid, goal, cost):
      from math import sqrt
      # Agregar el calculo de la matriz heuristica
      # No hace falta utilizar el parametro cost
      # Distancia Manhattan
      self.heuristic = [[ (abs(col-self.goal[0])+abs(row-self.goal[1]))
          for row in range(len(grid[0]))]for col in range(len(grid))]
      # Distancia Euclidea
      #self.heuristic = [[ sqrt((col-self.goal[0])**2+(row-self.goal[1])**2)
      #   for row in range(len(grid[0]))]for col in range(len(grid))]
      #print self.heuristic
      #
      #
      #
      #

    def expand(self, state):
        next_states = []
        for delta in range(-35, 40, 5):
            # Crear las trayectorias con delta de -35 a 40
            # con pasos de 5 grados

            # Modelo de movimiento
            delta_rad = np.deg2rad(delta) # conversion por librerias
            omega = 1 * math.tan(delta_rad) # velocidad de giro/angular: r*seg
            next_x = state[3] + 1 * math.cos(omega) # calcular nueva pos x
            next_y = state[4] + 1 * math.sin(omega) # calcular nueva pos y
            next_theta = (state[5] + omega) % (2*math.pi) # direccion de trompa

            # Costo total del nodo expandido
            next_g = state[1] + 1
            next_h = self.heuristic[int(next_x)][int(next_y)]
            next_f = next_g + next_h

            # Crea un nuevo 'estado' o nodo expandido con los datos
            # que luego seran parte de la lista de nodos abiertos
            state = [next_f, next_g, next_h, next_x, next_y, next_theta]
            next_states.append(state)

        return next_states

    # -------------------------------------
    # A* para buscar el camino al objetivo
    # -------------------------------------

    def astar(self):
        if self.heuristic == []:
            raise ValueError, "La matriz Heuristica debe estar definida para ejecutar A*"

        # Closed tiene la misma dimension que la matriz de mapa.
        # Cada punto si esta en cero no esta cerrado, inicializamos
        # todos los puntos como no cerrados
        closed = [[[0 for row in range(len(self.grid[0]))]
                     for col in range(len(self.grid))]
                  for cell in range(THETA_STACK)]

        # La matriz de accion indicara en cada punto que accion debe realizarse
        # para conectarse con el nodo anterior.
        self.action = [[[0 for row in range(len(self.grid[0]))]
                          for col in range(len(self.grid))]
                       for cell in range(THETA_STACK)]

        # Marcar el punto inicial como cerrado
        closed[self.init[0]][self.init[1]][0] = 1

        # Inicializar el primer elemento de la lista de abiertos con el punto inicial
        # Elementos de la lista open son del tipo: [f, g, h, x, y]
        x = self.init[0]
        y = self.init[1]
        theta = 0
        h = self.heuristic[x][y]
        g = 0
        f = g + h

        open = [[f, g, h, x, y, theta]]

        found  = False # flag que es verdadera cuando la busqueda se completo
        resign = False # flag que es verdadera cuando no se puede expandir mas
        count  = 0


        while not found and not resign:
            element = 0;
            # Chequeamos si todavia hay elementos en la lista open
            if len(open) == 0:
                resign = True
                print '###### Busqueda terminada pero fallida ######'
            else:
                open.sort(reverse=True, key=lambda x: x[0])
                element = open.pop()
                # TODO: removemos un nodo de la lista de abiertos para expandir
                # Para elegir el nodo a remover hay que buscar el que tenga el valor de f
                # mas chico. Se puede utilizar la funcion lista.sort(),lista.reverse(),lista.pop()


            if (not resign):
                f, g, h, x, y, theta = element
            # chequeamos si encontramos el objetivo
                if x == self.goal[0] and y == self.goal[1]:
                    found = True
                    print '###### A* Busqueda Realizada Exitosamente ######'
                else:
                    # TODO: Expandimos el elemento seleccionado y anadimos a la lista
                    next_states = self.expand(element)
                    # 1. Para expandir debemos recorrer los 8 movimientos que puede realizar el robot
                    for next_s in next_states:
                    # Chequear que el resultado x2 e y2 no sea mayor a la longitud de la matriz y que no sea
                    # menor a cero.
                        if (next_s[3] > (len(self.grid[0])-1)) or next_s[3] < 0:
                            continue

                        if (next_s[4] > (len(self.grid)-1)) or next_s[4] < 0:
                            continue

                    # Chequear que en la matriz grid[x2][y2] el valor es cero y que closed[x2][y2] es cero tambien
                        if self.grid[int(next_s[3])][int(next_s[4])] != 0 or closed[int(next_s[3])][int(next_s[4])] != 0:
                            continue

                        open.append(next_s)

                        theta_index = int((next_s[5]*THETA_STACK)/(2*math.pi))
                    # Ponemos en la matriz de cerrados el punto x2,y2 en 1
                        closed[next_s[3]][next_s[4]][theta_index] = 1
                    # Finalmente en la matriz de accion en el punto x2,y2 colocamos el movimiento que se realizo para llegar alli.
                        self.action[next_s[3]][next_s[4]][theta_index] = element
                    #
                    #
                    #
                    #
                    #
            count += 1

        # Extraemos el camino
        # desapilar
        # guardar x, y, theta (continuos)
        # hacer returnde self.path
        # TODO: explicar en el informe que funcion cumple esta porcion del codigo
        if (not resign):
            invpath = []
            x = self.goal[0]
            y = self.goal[1]
            invpath.append([x, y])
            while x != self.init[0] or y != self.init[1]:
                x2 = x - delta[self.action[x][y]][0]
                y2 = y - delta[self.action[x][y]][1]
                x = x2
                y = y2
                invpath.append([x, y])
            self.path = []
            for i in range(len(invpath)):
                self.path.append(invpath[len(invpath) - 1 - i])
        return resign

    # ----------------------------------------
    # Smooth Path
    # ----------------------------------------

    def smooth(self, weight_data = 0.5, weight_smooth = 0.25, tolerance = 0.000001):

        # Copia de self.path
        newpath = [[0 for row in range(len(self.path[0]))] for col in range(len(self.path))]
        for i in range(len(self.path)):
            for j in range(len(self.path[0])):
                newpath[i][j] = self.path[i][j]
                change = tolerance
                while change >= tolerance:
                    change = 0.0
                    for u in range(1,len(self.path)-1):
                        for t in range(len(self.path[0])):
                            aux = newpath[u][t]
                            newpath[u][t] += weight_data * (self.path[u][t] - newpath[u][t])
                            newpath[u][t] += weight_smooth * (self.path[u-1][t] + newpath[u+1][t] - 2.0 * newpath[u][t])
                            change += abs(aux - newpath[u][t])
                            
        # Minimizar la condicion (xi-yi)^2 (yi-yi+1)^2
        # Condicion de corte = tolerance
        # TODO: implementar la funcion de suavizado, pueden utilizar la del teorico.
        #
        #
        #
        
        self.spath = newpath
