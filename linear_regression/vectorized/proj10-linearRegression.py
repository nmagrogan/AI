'''
Class: CPSC 427 
Team Member 1: Nathan Magrogan
Team Member 2: None
Submitted By Nathan Magrogan
GU Username: nmagrogan
File Name: proj10-linearRegression.py
Preforms linear regression using a vectorized approach.
Outputs a plot of regression line and input data
Usage :  python proj10-linearRegression.py

'''

import numpy as np
import csv
import matplotlib.pyplot as plt


def regression(X,Y,m,learning_rate,theta_init):
	theta = theta_init
	diff = theta + 2

	while(not all(diff < .0001)):
		theta_old = theta
		theta = theta - (learning_rate/m)*np.matmul(X,(np.matmul(np.transpose(X),theta)-Y))
		diff = theta - theta_old #compare for convergance
		
	return theta



def plot_results(points,theta):
    x_training = [point[0] for point in points]
    y_training = [point[1] for point in points]

    y_prediction = [theta[1,0]*x + theta[0,0] for x in x_training]
    plt.plot(x_training,y_prediction,color='r')
    plt.scatter(x_training,y_training,color='g')
    plt.title("Vectorized Linear Regression")
    plt.show()


def init():
    #read file into list of x,y coordinates, one set of coords per line
    reader = list(csv.reader(open("input.csv", "rb"), delimiter=','))
    points = np.array(reader).astype('float')

    #setting up vectors in correct form
    x1,Y = np.split(points,2,1)
    x1 = x1.transpose()
    x0 = np.ones(x1.size)
    X = np.vstack((x0,x1))
    
    #set the initial parameters
    learning_rate = 0.0001 #step size
    theta_init = np.zeros(2) # initial theta guess
    theta_init = np.reshape(theta_init, (2,1)) 
    m = x1.size   #number of iterations of gradient across all points

    return X, Y, m, learning_rate, theta_init,points

def main():
	X,Y,m,learning_rate,theta_init,points = init()

	theta = regression(X,Y,m,learning_rate,theta_init)

	plot_results(points,theta)

main()