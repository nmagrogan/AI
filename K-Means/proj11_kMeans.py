'''
Class: CPSC 427
Team Member 1: Nathan Magrogan
Team Member 2: None
Submitted By Nathan Magrogan
GU Username: nmagrogan
File Name: proj11_kMeans.py
Preforms the K means algorithm on a set of data.
Outputs a plot of final k means fit
Usage :  python proj11_kMeans.py
'''
#Based on Peter Harrington, Machine Learning in Action

import numpy as np
import matplotlib.pyplot as plt

'''
Data comes in like this:
0.xxx ...  0.yyyy
where the values are floating point numbers representing points in a space
my example is m x 2, but the code would work for n features
Read these into an m x 2 numpy matrix, where m is the number of points
'''
def loadData(file_name):
    with open(file_name) as fin:
        rows = (line.strip().split('\t') for line in fin)
        dataMat = [map(float,row) for row in rows]
    return np.mat(dataMat)

'''
Construct a k x n matrix of randomly generated points as the
initial centroids. The points have to be in the range of the points
in the data set
'''
def randCent(dataMat,k):
    numCol = np.shape(dataMat)[1]  #notice the number of cols is not fixed.
    centroids = np.mat(np.zeros((k,numCol))) #kxnumCol matrix of zeros
    for col in range(numCol):
        minCol = np.min(dataMat[:,col]) #minimum from each column
        maxCol = np.max(dataMat[:,col]) #maximum from each column
        rangeCol = float(maxCol - minCol)
        centroids[:,col] = minCol + rangeCol * np.random.rand(k,1)
    return centroids

'''
Compute the Euclidean distance between two points
Each point is vector, composed of n values, idicating a point in n space
'''
def distEucl(vecA,vecB):
    return np.sqrt(np.sum(np.power(vecA - vecB,2)))



def kMeans(dataMat, k, distMeas=distEucl, createCent=randCent):
    m = np.shape(dataMat)[0]  #how many items in data set
    iterations = 0
    #create an mX2 natrix filled with zeros
    #each row stores centroi information for a point
    #col 0 stores the centroid index to which the point belongs
    #col 1 stores the distance from the point to the centroid
    clusterAssment = np.mat(np.zeros((m,2)))
    distance = []

    #create k randomly placed centroids
    centroids = createCent(dataMat,k)

    diff = centroids > 10


    #your code goes here (I required about 15 lines)
    while not diff.all():
        iterations = iterations + 1
        centroids_old = centroids.copy()

        for i in range(len(dataMat)):
            distance = []
            for j in range(len(centroids)):
                distance.append(distEucl(dataMat[i],centroids[j]))

            clusterAssment[i,0] = distance.index(min(distance))

        for i in range(len(centroids)):
            cluster = [dataMat[j] for j in range(len(clusterAssment)) if int(clusterAssment[j,0])== i]

            if len(cluster) != 0:
                mean_distance = sum(cluster) / float(len(cluster))
                centroids[i] = mean_distance

        diff = centroids_old - centroids < .000001


    return centroids, iterations #is the number of iterations required

def plot_results(dataMat, centroids, iterations):
    #your code goes here.  The trick is to transfrom the incoming matrices
    #to lists
    #On the same scatter plot, plot the points and the centroids
    #The centroid points should be a different shape and color than the data
    #points

    x = [dataMat[i,0] for i in range(len(dataMat))]
    y = [dataMat[i,1] for i in range(len(dataMat))]

    xc = [centroids[i,0] for i in range(len(centroids))]
    yc = [centroids[i,1] for i in range(len(centroids))]

    plt.scatter(x,y,color='g')
    plt.scatter(xc,yc,color='r',marker='x')
    plt.title("K-means data\nNum iterations :" + " " + str(iterations))
    plt.show()




def main():
    k = 4
    dataMat = loadData("testSet.txt")

    centroids, iterations = kMeans(dataMat, k, distEucl, randCent)

    plot_results(dataMat, centroids,iterations)


main()
