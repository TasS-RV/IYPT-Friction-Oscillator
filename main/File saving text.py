#Written by Tasin Sayed, December 2019 - this code was unfinished due to a halt in data analysis due to Covid19 

import numpy as np
import matplotlib.pyplot as plt
import math, operator
#BP6V3 - this is the best condition for oscillation of the thick plastic
print('[  IYPT Friction oscillator data curves   ]\n[   3D printed ABS/ Nylon plastic cylinders, 4  Rod types:\n 4-9V Rotation speed, 11.022N/m Spring constant   ]')
print('[    Frame rate = 60 FPS video - 2197 pixels/Meter]')
framerate = 60
#files = input('List of files to plot data on:') #Can enter a list of files in the same directory to plot data on 
#f_file = input('List of friction data files:')
files = 'SM4V3'
#LM9V3-2,WP4V3,WP4V3-2,BP9V3,LM9V3
files = files.split(',')
filenames = []
for f in files:
    filenames.append(f)
num = len(filenames)

def time_data(filenames,n):
    for f in filenames:
        with open(f + '.txt', 'r') as fr:
            join_data = []
            if n == 0:
                for n, val in enumerate(fr.readlines(), 1):
                    n = n / framerate
                    val = val.replace('\n', str(''))
                    #val = val.replace('\n', ',' + str(n))
                    join_data.append(val)
                del join_data[-1] #The last line does not have \n, this is to delete the stray value

                for i in join_data:
                    var = join_data.index(i)
                    var = int(var)
                    if ('#NUM!' in str(i)) == True:
                        del join_data[var]
                    else:
                        pass
            print(join_data)
        with open(f + '.txt', 'w') as fw:
            for i in join_data: #Files are rewritten with the data points inclusive of time
                fw.writelines(i + '\n')
            return
n = 0
time_data(filenames,n)
#n+=1
#time_data(filenames,n)


with open(f + '.txt', 'r') as fr:
    join_data = []
    for n, val in enumerate(fr.readlines(), 1):
        n = n / framerate
        val = val.replace('\n', ',' + str(n))
        join_data.append(val)
    del join_data[-1]  # The last line does not have \n, this is to delete the stray value
    print(join_data)
with open(f + '.txt', 'w') as fw:
    for i in join_data:  # Files are rewritten with the data points inclusive of time
        fw.writelines(i + '\n')
    #return
