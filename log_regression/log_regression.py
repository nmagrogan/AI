'''
Class: CPSC 427
Team Member 1: Nathan Magrogan
Team Member 2: None
Submitted By Nathan Magrogan
GU Username: nmagrogan
File Name: log_regression.py
Preforms logarighmic regression using a vectorized approach.
Outputs a plot of regression line and input data
Usage :  python log_regression.py

'''

import numpy as np
import csv
import matplotlib.pyplot as plt


def regression(theta_init,learning_rate,m,X,g,Z,Y):
	theta = theta_init
	diff = theta + 2

	while(not all(diff < .0001)):
		theta_old = theta
		theta = theta - (learning_rate/m)*np.matmul(np.transpose(X), g*Z - Y)
		diff = theta - theta_old #compare for convergance

	return theta

def decision_boundary(X,theta):

	x = [X[:,0].item(i) for i in range(len(X))]
	xVals = np.array([min(x),max(x)])
	yVals = -1/theta[2]*(theta[1]*xVals + theta[0])
	yVals = [yVals[0,0],yVals[0,1]]
	return xVals, yVals


def plot_results(X,y,theta,theta_given):

	points0 = [[X[i,0],X[i,1]] for i in range(len(X)) if y[i] == 0]
	points1 = [[X[i,0],X[i,1]] for i in range(len(X)) if y[i] == 1]


	xVals,yVals = decision_boundary(X,theta_given)



	#y_prediction = [theta[1,0]*x + theta[0,0] for x in x_training]
	plt.plot(xVals,yVals)
	plt.scatter(*zip(*points0),color='y', label ="rejected")
	plt.scatter(*zip(*points1),color='k',marker="+",label = "accepted")
	plt.title("Admitted/Not Admitted")
	plt.xlabel("Exam 1 Score")
	plt.ylabel("Exam 2 Score")
	plt.legend()

	plt.show()


def init():
	#read file into list of x,y coordinates, one set of coords per line
	reader = list(csv.reader(open("data1.txt", "rb"), delimiter=','))
	data = np.mat(reader).astype('float')

	theta_given = list(csv.reader(open("theta.txt", "rb"),delimiter=' '))
	theta_given = np.mat(theta_given).astype('float')



	X = data[:,:2]
	y = data[:,2]

	#set the initial parameters
	learning_rate = 0.0001 #step size
	theta_init = np.zeros(3) # initial theta guess
	theta_init = np.reshape(theta_init, (3,1))

	m = X.size   #number of iterations of gradient across all points
	return X, y, m, learning_rate, theta_init, theta_given

def main():

	X,y,m,learning_rate,theta_init,theta_given = init()

	theta = theta_init
	#theta = regression(X,Y,m,learning_rate,theta_init)

	plot_results(X,y,theta,theta_given)

main()
