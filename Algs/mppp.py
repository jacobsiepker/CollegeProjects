#Jacob Siepker
#CSC 321
#3/2/2020

#Solves maximum profit path problem using backtracing

def main():
    fileName = "ptable.txt"
    fileInput = open(fileName, 'r')
    fileInput.readline() #pass the first line. we dont need to know the size since my program is perfect
    
    ##set up 2d array.  for line in file.  For char in line (seperate by space)
    inAry = []
    index = 0
    for i in fileInput.readlines():
        inAry.append([])
        tempCharAry = i.split(" ") #split by space
        for j in tempCharAry:
            inAry[index].append(eval(j))
        index+=1


    maxProfit(inAry)


def printOutput(p, q, d, m):
    print("The maximum earnable profit is ${}\nThe maximum profit path is:".format(m))
    printPath(q, d)


def printPath(q, d):
    maxLoc = 0
    maxVal = 0
    for j in range(len(q[-1])):
        if (q[-1][j] > maxVal):
            maxLoc = j
            maxVal = q[-1][j]

    printPathHelper(d, -1, maxLoc)


def printPathHelper(d, i, j):
    if (i==-1):
        i = len(d)-1
    if (d[i][j] != -1):
        printPathHelper(d, i-1, d[i][j])

    print("({},{})".format(i+1,j+1))

def maxProfit(inAry):
    maximum = 0
    tempAry = []
    dAry = []

    
    for i in range(0, len(inAry)):
        tempAry.append([])
        dAry.append([])
        for j in range(0, len(inAry[i])):
            dAry[i].append(-1)
            tempAry[i].append(-1)
            
        
    for element in range(0, len(tempAry[-1]) ):
        maxProfitProphet(inAry, tempAry, len(inAry)-1, element, dAry)
        if (tempAry[-1][element] > maximum):
            maximum = tempAry[-1][element]

    printOutput(inAry, tempAry, dAry, maximum)    
    return maximum

def maxProfitProphet(inAry, tempAry, i, j, dAry):

    if (i==-1 or j>=len(tempAry[i]) or j==-1): ##bound the recursion, base cases
        return (0)
    if (tempAry[i][j] != -1):
        return (tempAry[i][j])

    else:
        maxLoc = j-1
        maxVal = maxProfitProphet(inAry, tempAry, i-1, j-1, dAry)

        if (  maxProfitProphet(inAry, tempAry, i-1, j, dAry) > maxVal ):
            maxLoc = j
            maxVal = maxProfitProphet(inAry, tempAry, i-1, j, dAry)

        if (maxProfitProphet(inAry, tempAry, i-1, j+1, dAry) > maxVal):
            maxLoc = j+1
            maxVal = maxProfitProphet(inAry, tempAry, i-1, j+1, dAry)

        if (i!=0):
            dAry[i][j] = maxLoc
        
        tempAry[i][j] = maxVal+ inAry[i][j]
        return(tempAry[i][j])

main()
