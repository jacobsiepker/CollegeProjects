#take file called numbers.txt to start
fileName = "numbers.txt"
def main():
    global fileName

    fileInput = open(fileName, 'r')
    numAry = []

    for line in fileInput.readlines():
        numAry.append(eval(line))

    maxInt = findMax(numAry, 0, len(numAry)-1)

    print("The Max Value Is " + str(maxInt))
    
def findMax(numAry, start, end):
    if (end-start == 0):
        return numAry[start]

    else:
        midpoint = ((end-start)//2)+start
        l = findMax(numAry, start, midpoint) #recursive call to left half
        r = findMax(numAry, midpoint+1, end) #recursive call to right half
        if (l > r):
            return l
        else:
            return r
    
main()
