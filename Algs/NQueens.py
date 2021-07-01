
#I diverted quite a bit from the pseudocode
#Mainly the isLegal function only checks columns and diaganols where a conflict could occur
#
firstValid = 1 #change this val to 0 to see all possible correct placements

def main(firstValid):
    print("How many queens should be placed?")
    Uinput = input("Enter a positive integer: ")
    UinputInt = eval(str(Uinput))

    Q = []

    for i in range(0, UinputInt):
        Q.append([])
        for j in range(0, UinputInt):
            Q[i].append(0)
            
    print(PlaceQueens(Q, 0, firstValid))
    #printArray(Q)

def printArray(Q):
    for i in range(0, len(Q)):
        print('')
        for j in range(0, len(Q)):
            print(Q[i][j], end = ' ')
    print("\n\n")

def PlaceQueens(Q, r, firstValid = 1):

    
    #print("Placing Queens")
    
    if (r == len(Q)):
        printArray(Q)
        return True
        

    else:
        for element in Q[r]:
            element =0

        valid = False
        
        for i in range(0, len(Q)):
            if (isLegal(Q, i, r)):
                for x in range(0,len(Q)):
                    Q[r][x] =0
                Q[r][i] = 1
                valid = PlaceQueens(Q, r+1)
                if(valid==True and firstValid == 1):
                    return valid
        return valid
                


def isLegal(Q, i, j):


    for x in range(0,j):
        if (Q[x][i] == 1):
            return False
    x=j-1
    y=i+1
    while(x>=0 and y<len(Q)):
        if (Q[x][y]==1):
            return False
        x-=1
        y+=1

    x=j-1
    y=i-1
    while(x>=0 and y>=0):
        if (Q[x][y]==1):
            return False
        x-=1
        y-=1
        
    return True
    


main(firstValid)
