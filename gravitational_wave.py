import math #Importing the math module (python)
import matplotlib.pyplot as plt #Importing matplotlib for plotting (neccesary for visual shit)

xs = [i*0.1 for i in range (62)] # list comprehension (it computes the values of 0 to 6.2 aprox, to give us the entire 0 to 2Pi)

ys_sin = [math.sin(x) for x in xs] # Another list comprehension but to compute the y - axis values
ys_cos = [math.cos(x) for x in xs] # # Another list comprehension but to compute the x - axis values

plt.plot(xs, ys_sin, label = 'Sine wave')
plt.show()