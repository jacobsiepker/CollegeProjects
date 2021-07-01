#Jacob Siepker
#CSC 321
#2/26/2020

import argparse

def main():

##########parse cmd line##############
    parser = argparse.ArgumentParser()

    parser.add_argument("word1")
    parser.add_argument("word2")
    args = parser.parse_args()

    word1 = args.word1
    word2 = args.word2

#########end parse cmd line###########

    
    editDistance = findEditDistance(word1,word2) #get val
    print("\nThe edit distance between {0} and {1} is {2} edits".format(word1, word2, editDistance)) #final output

def findEditDistance(word1, word2):  #user should only concern themselves with the words put into this function

    arry = []
    for i in range(0, len(word1)+1):
        arry.append([])
        for j in range(0, len(word2)+1):
            arry[i].append(-1)
    #setup array
    
    return findEditDistanceHelper(word1, word2, len(word1), len(word2), arry)

    
def findEditDistanceHelper(word1, word2, i, j, arry):
    if (arry[i][j] != -1): ##if already filled, return val
        return arry[i][j]

    if (i == 0): ##if upper base case, set accordingly
        arry[i][j] = j
        return (j)
    elif (j == 0):  #if left base case, set accordingly
        arry[i][j] = i
        return(i)

    else:
        lowest = min(  findEditDistanceHelper(word1, word2, i-1, j, arry), findEditDistanceHelper(word1, word2, i-1, j-1, arry), findEditDistanceHelper(word1, word2, i, j-1, arry)) #lotta recursion
                     
        if (word1[i-1] == word2[j-1]): ##no change needed
            arry[i][j] = lowest
            return lowest
        else: ##change needed, add one to lowest
            arry[i][j] = lowest+1
            return lowest +1

main()
