#Written by Tasin Sayed, December 2019

import numpy as np
import matplotlib.pyplot as plt
import math, csv

items_metal = []
items_plastic = []
#csv does not work with pycharm - does work on trinket.io, so to run this can be run there
#Best to use numpy to open the data
#x,y = np.loadtxt(filename,delimiter, unpack = True) - unpack state so it can obtain the values
with open('metal.txt', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=' ')
    for val in plots:
        items_metal.append(int(val[0]))

with open('plastic.txt', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=' ')
    for val in plots:
        items_plastic.append(int(val[0]))


# Should open another file and take the data, and plot a graph from that - this
# will be the data for metal

class graphing:
    framerate = 100

    def __init__(self, x_plot, y_plot1, y_plot2):
        self.x_plot = x_plot
        self.y1 = y_plot1
        self.y2 = y_plot2
        self.name = self
        return

    def calc(self, y_plot):
        x = 0
        self.gradient = []
        while x < (len(self.x_plot) - 1):
            derivative = ((y_plot[x + 1] - y_plot[x]) / (self.x_plot[x + 1] - self.x_plot[x]))
            self.gradient.append(derivative)
            x += 1
        self.gradient.append(0)
        return

    def graphing(self):
        fig = plt.figure(figsize=(6.0, 10.0))
        d_graph = fig.add_subplot(3, 1, 1)
        v_graph = fig.add_subplot(3, 1, 2)
        a_graph = fig.add_subplot(3, 1, 3)

        d_graph.plot(time, self.y1, label='Plastic\nCurve', color='red')
        d_graph.plot(time, self.y2, label='Metal\nCurve', color='cyan')

        d_graph.set_xlabel('Time Elapsed')
        d_graph.set_ylabel('Displacement(from C)(m)')
        d_graph.legend()

        self.calc(self.y1)
        v_graph.plot(time, self.gradient, label='Plastic\nCurve', color='red')
        self.calc(self.gradient)
        a_graph.plot(time, self.gradient, label='Plastic\nCurve', color='red')

        self.calc(self.y2)
        v_graph.plot(time, self.gradient, label='Metal\nCurve', color='cyan')
        self.calc(self.gradient)
        a_graph.plot(time, self.gradient, label='Metal\nCurve', color='cyan')

        v_graph.set_xlabel('Time Elapsed')
        v_graph.set_ylabel('Velocity(m/s)')
        a_graph.set_xlabel('Time Elapsed')
        a_graph.set_ylabel('Acceleration(m/s^2)')
        v_graph.legend()
        a_graph.legend()

        plt.show()
        return


framerate = 100
time = []
for i in range(1, len(items_metal) + 1):
    sec = i / framerate
    time.append(sec)
    plastic = []
    metal = []

for a in items_plastic:
    plastic.append(a)
for a in items_metal:
    metal.append(a)

dist = graphing(time, plastic, metal)
dist.graphing()
# Now make the graphing function take in a parameter - for different values
# of a different material -
# Takes parameter of self.y_plot (x_plot remains the same) and creates another line
while index < (700):
    for n, val in enumerate(y, 0):

        mean1 = (y[index + 3] - y[index]) / 4
        # mean2 = (y[index + 5] - y[index + 2]) / 4
        if len(mu) == 4:
            mu_mean = (mu[0] + mu[1] + mu[2] + mu[3]) / 4
            # if mean2 - mean1 > mu_mean:
            #   pass
            # elif mean2 - mean1 <= mu_mean:
            #   print(x[index])
            mu.clear()
        elif len(mu) < 4:
            pass
        mu.append(mean1)
        index += 1