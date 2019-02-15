'''
Nathan Magrogan
Project 2
1/25/19
'''

import re

'''
pre: none
post: input and output files are opened and references returned
'''
def my_open():
    while(True):
        file_in = raw_input('Enter an input file name\n')
        try:
            fin = open(file_in, 'r')
            break
        except:
            print("Invalid file name, Try again")
    return fin       




def main():
    fin = my_open();
    book = fin.read()
    book = book.lower()

    listWords = book.split()

    
    good_chars = [chr(value) for value in range(ord("a"),ord('z') + 1,1)]
    good_chars.append(' ')
    good_chars.append("'")

    totalWords = len(listWords)


    for i in range(0,len(listWords),1):
        for j in range(0,len(listWords[i]),1):
            if (listWords[i][j] not in good_chars or listWords[i][-1] == "'" or listWords[i][0] == "'"):
                listWords[i] = "'"
                totalWords = totalWords -1
                break



    good_chars.remove("'")
    good_chars.remove(" ")
    
    count_dict = {}

    for i in range(len(listWords)):
        if listWords[i][0] in count_dict:
            count_dict[listWords[i][0]] = count_dict[listWords[i][0]] + 1
        elif listWords[i][0] in good_chars:
            count_dict[listWords[i][0]] = 1
            

    listWords = list(count_dict.keys())
    listWords.sort()
    print("CHARACTER  FREQUENCY\n")
    for word in listWords:
        print(word + '\t\t' + str(count_dict[word]) + '\n')
    print("Total Words : " + str(totalWords))

    
    

main()
