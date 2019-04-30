'''
Class: CPSC 427
Team Member 1: Nathan Magrogan
Team Member 2: None
Submitted By Nathan Magrogan
GU Username: nmagrogan
File Name: log_regression.py
Preforms logarighmic regression using a vectorized approach.
Outputs a plot of regression line and input data
Usage :  python logReg.py

'''

import numpy as np
import csv
import matplotlib.pyplot as plt
import scipy.optimize as opt


def decision_boundary(X,theta):

	x = [X[:,1].item(i) for i in range(len(X))]
	xVals = np.array([min(x),max(x)])
	yVals = -1/theta[2]*(theta[1]*xVals + theta[0])
	yVals = [yVals[0,0],yVals[0,1]]
	return xVals, yVals


def plot_results(X,y,theta_given):

	points0 = [[X[i,1],X[i,2]] for i in range(len(X)) if y[i] == 0]
	points1 = [[X[i,1],X[i,2]] for i in range(len(X)) if y[i] == 1]


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

def sigmoid(x):
	return 1/(1+np.exp(-x))

def compJ(theta,X,y):
	theta = np.matrix(theta)
	X = np.matrix(X)
	y = np.matrix(y)
	m = np.shape(X)[0]
	hx = sigmoid((X*theta.transpose()))
	left = np.multiply(-y,np.log(hx))
	right = np.multiply((1-y),np.log(1-hx))
	return np.sum(left-right)/m

def compGrad(theta,X,y):
	m = np.shape(X)[0]
	theta = np.matrix(theta)
	X = np.matrix(X)
	y = np.matrix(y)
	hx = sigmoid(X*theta.transpose())
	error = hx-y
	gradient = (X.transpose()*error)/m
	return gradient

def opt_params(theta,X,y):
	answer = opt.fmin_tnc(func=compJ,x0=theta,fprime=compGrad,args=(X,y))
	return answer[0]

def init():
	#read file into list of x,y coordinates, one set of coords per line
	reader = list(csv.reader(open("data1.txt", "rb"), delimiter=','))
	data = np.mat(reader).astype('float')

	theta_given = list(csv.reader(open("theta.txt", "rb"),delimiter=' '))
	theta_given = np.mat(theta_given).astype('float')

	X = data[:,:2]
	y = data[:,2]

	X = np.insert(X,0,1,1)


	#set the initial parameters
	learning_rate = 0.0001 #step size
	theta_init = np.zeros(np.shape(X)[1]) # initial theta guess
	theta_init = np.matrix(theta_init)

	return X, y, learning_rate, theta_init, theta_given

def main():

	X,y,learning_rate,theta_init,theta_given = init()
	#plot for part 1 of assignmen
	#plot_results(X,y,theta_given)


	theta = opt_params(theta_init,X,y)
	theta = np.matrix(theta)
	theta = theta.transpose()
	#plots results for part 3 of assignment
	plot_results(X,y,theta)


main()
