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
      # Agregar el calculo de la matriz heuristica
      # No hace falta utilizar el parametro cost
      self.heuristic = [[0 for row in range(len(grid[0]))]for col in range(len(grid))]
      print heuristic
      #
      #
      #
      #

    # -------------------------------------
    # A* para buscar el camino al objetivo
    # -------------------------------------

    def astar(self):
        if self.heuristic == []:
            raise ValueError, "La matriz Heuristica debe estar definida para ejecutar A*"

        # Movimientos del robot
        # Si tomamos un pixel (x,y) los vectores definidos debajo
        # seran el incremento/decremento de cada eje
        delta = [[-1,  0],  
                 [ 0, -1],  
                 [ 1,  0],  
                 [ 0,  1],  
                 [ 1,  1],
                 [ -1, 1],
                 [  1,-1],
                 [ -1,-1]]

        # Closed tiene la misma dimension que la matriz de mapa.
        # Cada punto si esta en cero no esta cerrado, inicializamos
        # todos los puntos como no cerrados
        closed = [[0 for row in range(len(self.grid[0]))]
                     for col in range(len(self.grid))]

        # La matriz de accion indicara en cada punto que accion debe realizarse
        # para conectarse con el nodo anterior.
        self.action = [[0 for row in range(len(self.grid[0]))]
                          for col in range(len(self.grid))]

        # Marcar el punto inicial como cerrado
        closed[self.init[0]][self.init[1]] = 1

        # Inicializar el primer elemento de la lista de abiertos con el punto inicial
        # Elementos de la lista open son del tipo: [f, g, h, x, y]
        x = self.init[0]
        y = self.init[1]
        h = self.heuristic[x][y]
        g = 0
        f = g + h

        open = [[f, g, h, x, y]]

        found  = False # flag que es verdadera cuando la busqueda se completo
        resign = False # flag que es verdadera cuando no se puede expandir mas
        count  = 0

        while not found and not resign:
            # Chequeamos si todavia hay elementos en la lista open
            if len(open) == 0:
                resign = True
                print '###### Busqueda terminada pero fallida ######'
            else:
                pass
                # TODO: removemos un nodo de la lista de abiertos para expandir
                # Para elegir el nodo a remover hay que buscar el que tenga el valor de f
                # mas chico. Se puede utilizar la funcion lista.sort(),lista.reverse(),lista.pop()

            if (not resign):
            # chequeamos si encontramos el objetivo
                if x == self.goal[0] and y == self.goal[1]:
                    found = True
                    print '###### A* Busqueda Realizada Exitosamente ######'
                else:
                    # TODO: Expandimos el elemento seleccionado y anadimos a la lista
                    # 1. Para expandir debemos recorrer los 8 movimientos que puede realizar el robot
                    # 2. Creamos una variable temporal x2 e y2 aplicando el incremento/decremento al valor x
                    #    e y del elemento seleccionado y el movimiento seleccionado.
                    # 3. Chequear que el resultado x2 e y2 no sea mayor a la longitud de la matriz y que no sea
                    #    menor a cero.
                    # 4. Chequear que en la matriz grid[x2][y2] el valor es cero y que closed[x2][y2] es cero tambine
                    # 5. Calcular g2, h2, f2 del nuevo punto x2, y2 y agregarlo a la lista de los nodos abiertos.
                    # 6. Ponemos en la matriz de cerrados el punto x2,y2 en 1
                    # 7. Finalmente en la matriz de accion en el punto x2,y2 colocamos el movimiento que se realizo para llegar alli.
                    #
                    #
                    #
                    #
                    #
                    resign = True # Remover esto cuando se realice el ejercicio
                    pass
            count += 1

        # Extraemos el camino
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
                #print self.path[i]
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
        # Minimizar la condicion (xi-yi)^2 (yi yi+1)^2
        # Condicion de corte = tolerance
        # TODO: implementar la funcion de suavizado, pueden utilizar la del teorico.
        #
        #
        #
        
        self.spath = newpath
