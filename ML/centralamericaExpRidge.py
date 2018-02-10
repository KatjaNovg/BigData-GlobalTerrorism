#!/usr/bin/env python2
# -*- coding: utf-8 -*-



import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import Ridge
from sklearn.pipeline import make_pipeline


file = open("camericaexp1990bigtest.csv", "r")
# this file is the big dataset of testing data

year_list = []
kill_list = []
month_list = []
day_list = [] # lists for extracting values
for line in file:
    	nline = line.split(",")
    	if nline[1] != "iyear":
        	year_list.append(int(nline[1]))
        	month_list.append(int(nline[2]))
        	day_list.append(int(nline[3]))
        	kill_list.append(nline[4])

file.close()
monthday = []
for i in range(len(month_list)):
	if (month_list[i] > 9): # if clauses now obsolete. leftover of old code
        	if (day_list[i] > 9):
			monthday.append(str(month_list[i]) + str(day_list[i]*3))
                        # days multiplied to increase their weight
                        #  30*3 days equals 90% of 100 and therefore 
                        # the weight on timescale is closer to truth
		else:
	        	day_listnew = str(day_list[i]*3)
	        	monthday.append(str(month_list[i]) + str(day_listnew))
            	
        else:
        	if (day_list[i] > 9):
			month_listnew = str(month_list[i])
			monthday.append(str(month_listnew) + str(day_list[i]*3))
		else:
	        	day_listnew = str(day_list[i]*3)
			month_listnew =  str(month_list[i])
	        	monthday.append(str(month_listnew) + str(day_listnew))

yearmonthday = []
for i in range(len(year_list)): # transform years + months as float
        yearmonthday.append(float((str(year_list[i]) + '.' + str(monthday[i]))))


ylist = np.array(yearmonthday) # the set of years for this this data set
klist2 = np.array(kill_list) # the set of kill statistics for this data set


file2 = open("camericaexp1990smalltrain.csv", "r")
# thi file is the small dataset of training data

year_list2 = []
kill_list2 = []
month_list2 = []
day_list2 = []
for line in file2:
    	nline2 = line.split(",")
    	if nline2[1] != "iyear":
        	year_list2.append(int(nline2[1]))
        	month_list2.append(int(nline2[2]))
        	day_list2.append(int(nline2[3]))
        	kill_list2.append(nline2[4])

file2.close()
monthday2 = []
for i in range(len(month_list2)):
	if (month_list2[i] > 9):
        	if (day_list2[i] > 9):
			monthday2.append(str(month_list2[i]) + str(day_list2[i]*3))
		else:
	        	day_list2new = str(day_list2[i]*3)
	        	monthday2.append(str(month_list2[i]) + str(day_list2new))
            	
        else:
        	if (day_list2[i] > 9):
			month_list2new =  str(month_list2[i])
			monthday2.append(str(month_list2new) + str(day_list2[i]*3))
		else:
	        	day_list2new = str(day_list2[i]*3)
			month_list2new =  str(month_list2[i])
	        	monthday2.append(str(month_list2new) + str(day_list2new))

yearmonthday2 = []
for i in range(len(year_list2)):
        yearmonthday2.append(float((str(year_list2[i]) + '.' + str(monthday2[i]))))


ysubset = np.array(yearmonthday2) # the set of years for this this data set
ksubset = np.array(kill_list2) # the set of kill statistics for this data set


# add dimension to the nparray
ysubset2D = ysubset[:, np.newaxis]
ylist2D = ylist[:, np.newaxis]

colors = ['teal', 'yellowgreen', 'gold', "navy"] # left for self reference
lw = 2# linewidth

plt.scatter(ysubset, ksubset, color='navy', s=30, marker='o', label="training points")
# plotting the individual data points

plt.scatter(ylist, klist2, color='teal', s=10, marker='o', label="test points")
# plotting the individual data points

model = make_pipeline(Ridge(alpha=0.1))
model.fit(ysubset2D, ksubset) # fit model on training data set
y_plot = model.predict(ylist2D) # use the model on test data set to see if it holds up
plt.yticks([0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300],\
               [0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300])
# yticks describe the number of kills in intervals or 20
plt.plot(ylist, y_plot, color="red", linewidth=lw,
             label="Ridge")

plt.legend(loc='upper left')

fig_size = plt.rcParams["figure.figsize"]
 

plt.figure(figsize=(250,100)) # increase graph size

plt.show()