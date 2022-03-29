#Written by Tasin Sayed, December 2019

#Packages necessary for program to run
import numpy as np
import matplotlib.pyplot as plt
import math, operator
#BP6V3 - this is the best condition sfor oscillation of the thick plastic
print('[  IYPT Friction oscillator data curves   ]\n[   3D printed ABS/ Nylon plastic cylinders, 4  Rod types:\n 4-9V Rotation speed, 11.022N/m Spring constant   ]')
print('[    Frame rate = 60 FPS video - 2197 pixels/Meter]')
framerate = 60
#files = input('List of files to plot data on:')  
#f_file = input('List of friction data files:')   #This can be used to input a custom set of files to plot graphs on for data anslysis
f_file = 'FC_TP,FC_WP'
files = 'TP6.5V3,WP9V3'
#'LM6.5V3-2,LM6.5V3-3,LM6.5V3-4,LM9V3,LM9V3-2,SM4V3,SM9V3,TP4V3,TP4V3-2,TP4V3-3,TP4V3-4,TP7V3,TP7V3-2,TP7V3-3,TP9V3,TP9V3-2,WP4V3,WP4V3-2,WP9V3'
files = files.split(',')
filenames = []
for f in files:
    filenames.append(f)
num = len(filenames)

def time_data(f_name):
   # for f in filenames:
   with open(f_name + '.txt', 'r') as fr:
       join_data = []
       for n, val in enumerate(fr.readlines(), 1):
           n = n / framerate
           val = val.replace('\n', ',' + str(n))
           join_data.append(val)
       del join_data[-1]  # The last line does not have \n, this is to delete the stray value
       print(join_data)
   with open(f_name + '.txt', 'w') as fw:
       for i in join_data:  # Files are rewritten with the data points inclusive of time
           fw.writelines(i + '\n')
       return
#Run only once to append the time axis on the files
'''
for f_name in filenames:
    time_data(f_name)
'''
#Adding 2nd column with timedata - of displacement progression
#for f in filenames:


#WP is white plastic - but refers to the thin Black plastic
f_file = f_file.split(',')
K = 11.022 #N/m spring constant
mass = 100 #/grams, mass of rod
def fric_data(f_file):
    friction_data = []
    for ind,f in enumerate(f_file,0):
        with open(f + '.txt', 'r') as f_read:
            volts = []
            fric = []
            for n, ex in enumerate(f_read.readlines(), 4):
                ex = ex.replace('\n','')
                ex = float(ex)
                coeff = (K * (ex / 100) / (mass / 1000))
                volts.append(n)
                fric.append(coeff)
        friction_data.insert(n,[f,volts,fric])
    fric_data.friction_data = friction_data
    return fric_data.friction_data
#Stores the data in a 3 dimensional array: f rows x 3 columns where f is the number of files
fric_data(f_file)
friction = fric_data.friction_data #Array storing data of friction coefficients


#Plotting the data from the graphs
d_array = []
for n,file in enumerate(filenames,0):
    x,y = np.loadtxt(file+'.txt',delimiter = ',',unpack  = True)
    d_array.insert(n,(str(file),(x/2197),y))
    #Format(filename,[x][y]) for the values in d_array - 2D array
print(len(d_array[0][1]))
'''iteration that takes in the filename, stores it in enumerated index n, and adds the list to the 2 dimensional array
x = list[n][0]
y = list[n,1]
x and y can then be plotted
Important note - a number of incremental variables may need to be generated, but without establishing the variable reference
we cannot modify it anyways. Therefore, create a list with n elements, as the number of vairables you need to generate, then
list[n] index can be used as the variable, and can also be attached with attributes
'''
x_val = []
y_val = []

#This sub program plots the graphs
def data_processor(data_mat,friction):
    #fig.add_subplot(x,y,index) - index follows numerical order, left to right from rows:
    #1,2,3
    #4,5,6 etc...

    graph = plt.figure(figsize=(13, 7))
    disp_ = graph.add_subplot(2, 2, 1)
    vel = graph.add_subplot(2, 2, 2)
    acc = graph.add_subplot(2, 2, 3)

    fcof = graph.add_subplot(2,2,4)

    #Plotting the values into the graphs
 ################################################
    for i in d_array:
        legend = i[0]
        y = i[1]
        x = i[2]
        # Obtains the lists form the 2d array
        index = 0
        mu = []  # For the initial mean
        dist = []
        time = []
        # Mean 2 and 1 are found = form the data., then a mean of the means is identified: the checks if mean2 > mean of mean
        # and where it begins to decline, is where each of the peaks are
        while index < (len(y) - 50):
            mean1 = (y[index + 10] - y[index]) / 10
            mean2 = (y[index + 20] - y[index + 10]) / 10
            if len(mu) == 10:
                mu_mean = (mu[0] + mu[1] + mu[2] + mu[3] + mu[4] + mu[5] + mu[6] + mu[7] + mu[8] + mu[9]) / 10
                if mean2 > mu_mean:
                    pass
                elif mean2 <= mu_mean:
                    # Stores the indexes of the times - to obtain corresponding y values
                    dist.append(y[index])
                    time.append(x[index])  # Plots separate graph to extrapolate from
                    #print(x[index])
                mu.clear()
            elif len(mu) < 10:
                pass
            mu.append(mean1)
            index += 1
        # np.where(array, object/value) returns an array of the index of the value
        ##########################################################################################################################################################################################
        disp_.scatter(time, dist, s=30, color='red')
        # Displacement curve from the data measurements
        disp_.plot(x, y, label=legend + '\nDisplacement')
        #disp_.scatter(x, y, label=legend + '\nDisplacement',s = 7)
        # dist.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 200))(np.unique(x)))
        disp_.legend()

        # Function for the derivative
        def deriv(y, x):
            gradient = []
            # Averaging the value over 5 points
            n = 0
            i = 3  # This is the increment for data averaging
            while n < (len(y) - i):  # Make sure it ends on a multiple of 3
                derivative = ((y[n + i] - y[n]) / (x[n + i] - x[n]))
                gradient.append(derivative)
                n += i
            gradient.append(y[n])
            deriv.gradient = gradient[0:]
            global x_val
            x_val = []
            for n, i in enumerate(deriv.gradient, 1):
                x_val.append(n / 60)  # To match x and y dimensions
            return deriv.gradient, x_val

        deriv(y, x)
        # EXTRAPOLATE: np.polyfit(x,y,number of points to average and extrapolate) - this extrapolates a line of best fit
        # vel.plot((x_val), np.poly1d(np.polyfit(x_val, deriv.gradient, 250))(x_val),label = 'LM4V3 Velocity')
        vel.plot(x_val, deriv.gradient, label=legend + '\nVelocity')
        vel.legend()

        deriv(deriv.gradient, x)  # Runs derivative again for acceleration
        acc.plot(x_val, deriv.gradient, label=legend + '\nAcceleration')
        # acc.plot(np.unique(x_val), np.poly1d(np.polyfit(x_val, deriv.gradient, 250))(np.unique(x_val)),label = 'LM4V3 Acceleration')
        acc.legend()
        for val in friction:
            name = val[0]
            x_cor = val[1]
            y_cor = val[2]
            #fcof.plot(x_cor, y_cor, label=name)
            fcof.plot(x_cor, np.poly1d(np.polyfit(x_cor, y_cor, 5))(x_cor), label=name)
        fcof.legend()
    plt.show()
#The graphing section ends here
    val1 = np.where(x == time[0])
    val2 = np.where(x == 1.7)
    val1 = int(val1[0][0])
    val2 = int(val2[0][0])
    val2 = y[val2]
    val1 = y[val1]
    val_mean = (val1 + val2) / 2
    # print(val_mean)
    eq = []
    for eq_ in range(len(x)):
        eq.append(val_mean)
        # Equilibrium line of the oscillations
        #disp.plot(x,eq)
    return
data_processor(d_array,friction)
################################################################################################################################################

'''
fig = plt.figure(figsize = (10,10))
plot1 = fig.add_subplot(2,1,1)
plot2 = fig.add_subplot(2,1,2)
#data = [['file1',[1,2,3,4,5],[1,2,3,4,5]],
       # ['file2',[1,2,3,4,5],[2,4,6,8,10]]]
for i in d_array:
    legend = i[0]
    y = i[1]
    x = i[2]
    #Obtains the lists form the 2d array
    index = 0
    mu = [] #For the initial mean
    dist = []
    time = []
    #Mean 2 and 1 are found = form the data., then a mean of the means is identified: the checks if mean2 > mean of mean
    #and where it begins to decline, is where each of the peaks are
    while index<(len(y)-50):
        mean1 = (y[index + 10] - y[index]) / 10
        mean2 = (y[index + 20] - y[index + 10]) / 10
        if len(mu) == 10:
            mu_mean = (mu[0] + mu[1] + mu[2] + mu [3]+mu[4]+mu[5]+mu[6]+mu[7]+mu[8]+mu[9]) / 10
            if mean2  > mu_mean:
               pass
            elif mean2  <= mu_mean:
                #Stores the indexes of the times - to obtain corresponding y values
                dist.append(y[index])
                time.append(x[index]) #Plots separate graph to extrapolate from
                print(x[index])
            mu.clear()
        elif len(mu) < 10:
            pass
        mu.append(mean1)
        index +=1
#np.where(array, object/value) returns an array of the index of the value
    val1 = np.where(x == time[0])
    val2 = np.where(x == 1.7)
    val1 = int(val1[0][0])
    val2 = int(val2[0][0])
    val2 = y[val2]
    val1 = y[val1]
    val_mean = (val1+val2)/2
    print(val_mean)
    eq = []
    for eq_ in range(len(x)):
        eq.append(val_mean)
    #Equilibrium line of the oscillations
    plot1.plot(x,eq)
    plot1.plot(x, y)
    plot1.scatter(time,dist,s = 30,color = 'red')
    plt.show()  # plt.show() is fundamental so the graph gets displayed

'''#m = GEKKO()#Can be used to smoothen the curve

'''Options for program:
1)For each 4 segments of values, find their means and discard any values more than 2 standard deviations (of original sd)
Find their indexes, and delete the corresponding data points for time and replot the graph

2)Run an iteration through the y values, and find any that are 1-2 sd from the equilibrium - store their indexes:
then any indexes with close proximity:

add a starting 0 by default to store the first index

for i in indexes:
if i - index <=3:
do NOT append index to the new list of indices, but if the difference between subsequent indexes is MORE than 6, then store them 
in the amplitude indexes - 
find the time differences (for x values at the indexes to caluclate the period)

Overall: use averages and averages of averages to get a finer graph, and potentially use scipy.interpolate to get a smoother curve
'''

#Calculates the standard deviation - for the minimum increment: Implemented later on, however data was initially too noisy for this to be a suitable implementation
y_first = y[:41]
y_sd = 0
y_mean = 0
n = 0
for j in y_first:
    y_mean += j
    n+=1
y_mean = y_mean / n
for j in y_first:
    y_sd += math.pow(j - y_mean, 2)
y_sd = math.sqrt(y_sd / n)
#print(y_sd)

