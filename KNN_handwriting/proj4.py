'''
Class: CPSC 427-01
Team Member 1: Nathan Magrogan
Team Member 2: none
Submitted by: Nathan Magrogan
GU username: nmagrogan
filename: proj4.py
python 2.7
Handwriting recognition using Knn
'''
from kNN import *
from os import listdir


'''
file_lst is the list of file names containing training or test data.  path is
the path from the code to where the data is stored.  train_matrix is an N X 1024
matrix of training/test data where each row is the contents of one of the
training files
'''
def make_matrix(path):
    file_lst = listdir(path)
    m = len(file_lst)
    train_matrix = zeros((m,1024))

    for i in range(m):
        train_matrix[i] = img2vector(file_lst[i],path)
        
    return train_matrix
    

'''
Each training, test file is a 32X32 matrix of 0's and 1's.  The goal is to
transform the matrix into a vector, where 32nd position of the vector begins
with the 0th item in the 1st row the matrix. This function and the following
one unpacks a 2-D array into a 1-D array.

A simpler example:
ex = matrix([[1,2],[3,4],[5,6]])
vect = zeros((1,6))
for i in range(3):
    for j in range(2):
        vect[0,2*i+j] = sample[i,j]
vect now contains: [1,2,3,4,5,6]
'''
def img2vector(file_name,path):
    
    file_name = path+file_name
    myFile = open(file_name,'r')
    
    fileContents = myFile.read()

    temp = fileContents.split()

    for i in range(len(temp)):
        temp[i] = list(temp[i])
        for j in range(len(temp[i])):
            temp[i][j] = int(temp[i][j])                       
                
    imVect = reshape(temp,(1,1024))
          
    myFile.close()
    return imVect
    

'''
file_lst is the list of file names containing training or test data.
Every file name begins with a digit, as in 1_160.txt.  This function and
the following one extracts the initial digit and stores it in a list
'''
def make_labels(path):
    baseList = listdir(path)
    endList = [baseList[i][0] for i in range(len(baseList))]
    for i in range(len(endList)):
       endList[i] = int(endList[i])
    return endList
        

'''
test all of the files in the test directory
'''
def test_classifier(test_path, train_matrix, train_labels, k):
    errors = 0
    file_lst = listdir(test_path)
    labels = make_labels(test_path)
    result = zeros(len(file_lst))
    testMatrix = make_matrix(test_path)
    
    for i in range(len(file_lst)):
        result[i] = classify(testMatrix[i],train_matrix,train_labels,k)
        if(result[i] != labels[i]):
            errors += 1
            print("Error on item " + str(i))
            print("  classifier says: " + str(result[i]) + " real answer: " + str(labels[i]))
            
    print "Total Errors: " + str(errors)
    print "Error Rate: " + str(float(errors)/float(len(file_lst)))
         
def main():
    k = 3
    train_path = 'trainingDigits/'
    test_path = 'testDigits/'
   
    train_labels = make_labels(train_path)
    train_matrix = make_matrix(train_path)
    
    test_classifier(test_path,train_matrix,train_labels,k)
    
    
main()
