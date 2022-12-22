import matplotlib.pyplot as plt
import numpy as np

print("Ingrese 3 coordenadas para el eje X")
x1= int (input( "coordenada 1: "))
x2= int (input( "coordenada 2: "))
x3= int (input( "coordenada 3: "))

print("Ingrese 3 coordenadas para el eje Y")
y1= int (input( "coordenada 1: "))
y2= int (input( "coordenada 2: "))
y3= int (input( "coordenada 3: "))

print("Graficando la función matemática... ")

x=[x1,x2,x3]
y=[y1,y2,y3]

plt.plot(x,y,)

plt.show()
