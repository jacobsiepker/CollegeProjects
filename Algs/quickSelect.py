#Jacob Siepker
#CSC 321 Algs
#Final Exam
#Quick Select
#3/17/2021


def main():

    ##File#I/O#&#Array#INIT######
    filename = "finalexamselect.txt"
    fileInput = open(filename, 'r')
    text = fileInput.readline()
    ary = text.split(" ")
    for i in range(len(ary)):
        ary[i] = int(ary[i])

    k1 = 4
    
    k2 = len(ary)//2
    k3 = len(ary)-1

    #for k1 in range(0, 63):
    print(f"The {k1}th largest element is {QuickSelect(ary, k1)}")
    print(f"The {k2}nd largest element is {QuickSelect(ary, k2)}")
    print(f"The {k3}rd largest element is {QuickSelect(ary, k3)}")


def QuickSelect(ary, k, m = 0, n=-1):
    #print(f"QuickSelect({m},{n})")
    if (n==-1): #set n if none provided
        n = len(ary)-1
    
    if (m>=n):  #base case
        return (ary[k])

    piv = ary[n]
    pivIndex = partition(ary, m, n)

    if (k < pivIndex):
        #print("Right")
        return QuickSelect(ary, k, m, pivIndex-1)
    
    else:
        #print("Left")
        return QuickSelect(ary, k, pivIndex+1, n)




def partition(ary, m, n):
    #####DEBUG#PRINTS###################
##    print(f"Partition({m},{n})")
##    print("Before: ",end='')    
##    for i in range(m,n+1):
##        print (f"{ary[i]} ",end='')
##    print('')

    ####################################

    #ChoosePivot
    p = ary[n]
    
    lmda = m-1

    #print(f"Pivot: {p}")
    for i in range(m,n):
        if ary[i] < p:
            lmda+=1
            ary[lmda], ary[i] = ary[i], ary[lmda] #I forget python can do this, pretty cool
    ary[lmda+1], ary[n] = ary[n], ary[lmda+1]


    #######DEBUG#PRINTS############
##    print("After: ",end='')    
##    for i in range(m,n+1):
##        print (f"{ary[i]} ",end='')
##    print('\n')
    ###############################

    return lmda +1


main()
