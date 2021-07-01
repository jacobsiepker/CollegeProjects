#Jacob Siepker
#CSC 321 Algs
#Final
#LIS program

import sys

def main():

    ary = [0, 60, 10, 70, 20, 80, 30, 90, 50, 100, 60, 110, 70, 120, 80, 90]

    sequence = lis(ary)

    print(f"The longest increasing subsequence has {sequence} elements")

    
def lis(ary):
    n = len(ary)
    ary[0] = -sys.maxsize

####INIT#LISbigger##########
    LISbigger = []
    for i in range(n):
        LISbigger.append([])
        for j in range(n+1):
            LISbigger[i].append(-1)
####END#INIT#LISbigger######

    for i in range(n): #Set Base Case
        LISbigger[i][n] = 0

    for j in range(n-1, 0, -1): #Fill table/ no recursion
        for i in range(j):
            keep = LISbigger[j][j+1] + 1
            skip = LISbigger[i][j+1]
            if ary[i]>ary[j]:
                LISbigger[i][j] = skip
            else:
                LISbigger[i][j] = max(keep, skip)

    return LISbigger[0][1]
    
main()

