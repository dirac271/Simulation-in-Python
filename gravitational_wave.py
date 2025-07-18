import math #Importing the math module (python)
import matplotlib.pyplot as plt #Importing matplotlib for plotting (neccesary for visual shit)

xs = [0.1*i for i in range (62)] # list comprehension (it computes the values of 0 to 6.2 aprox, to give us the entire 0 to 2Pi)

ys_sin = [math.sin(x) for x in xs] # Another list comprehension but to compute the y - axis values
ys_cos = [math.cos(x) for x in xs] # # Another list comprehension but to compute the x - axis values

plt.grid(True) # draw the grid lines on the background, without this it would be harder to see the graph

plt.plot(xs, ys_cos, label = 'Cosine wave') #Plotting the sin - wave
plt.plot(xs, ys_sin, label = 'Sine wave') #Plotting the sin - wave

plt.legend() # This put a square that differences between the two sin and cos plots
plt.title("Sin and Cosine waves") # Main title of the plot
plt.xlabel('x Radians')# label the x - axxis
plt.ylabel('value')# label the y - axxis

plt.show() # Show the final result
