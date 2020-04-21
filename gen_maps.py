from scipy import misc
from math import *
import random
import time
import math
import numpy as np
import matplotlib.pyplot as plt
import sys
import select
import tty
import termios

X_LEN = 50
Y_LEN = 50
THRESH = 0.8
m_plan = []

init = [random.randint(0,X_LEN), random.randint(0,Y_LEN)]

distance = 0.0

while (distance < 30.0) :
    goal = [random.randint(0,X_LEN), random.randint(0,Y_LEN)]

    distance = sqrt(pow(init[0]-goal[0],2)+pow(init[1]-goal[1],2))
    

name_image = 'test4.jpg'

file_datab = open('database.log','a')

file_datab.write(name_image + ' ' + str(init[0]) + ' ' + str(init[1]) + ' ' + str(goal[0]) + ' ' + str(goal[1]) + '\n' )

for i in range(Y_LEN):
    row_temp = []
    for j in range(X_LEN):
        if ( i == init[0] or j == init[1] or i == goal[0] or j == goal[1] ):
            row_temp.append(0)
        else:
            row_temp.append(int(random.random()>THRESH))
    m_plan.append(row_temp)
        
x_grid = []
y_grid = []
for i in range(len(m_plan)):
    for j in range(len(m_plan[0])):
        if (m_plan[i][j] == 1):
            y_grid.append(j)
            x_grid.append(i)

plt.plot(x_grid,y_grid,'ro')
plt.show()

misc.imsave('maps/' + name_image, m_plan)

file_datab.close()
