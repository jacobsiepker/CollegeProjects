#count inversions
debugPrints = False
inversionCount = 0
fileName = "inversionsinput.txt"

#Base for mergeSort() and merge() were taken from someone elses implementation
#Functionality for inversion counting added by me of course
#Main() and debugPrints also added by me

def main():
    global fileName
    if (debugPrints):
        print("RUNNING\n")
    #open file inversionsinput.txt  
    inversionsF = open(fileName, 'r')
    lineCount = 0;
    invAry = []

    #for each line, add line to array[i]
    for line in inversionsF.readlines():
        invAry.append(eval(line))
        lineCount+=1

    if (debugPrints):
        print("Array Before Sort:")
        for element in invAry:
            print (element, end = ' | ')
        print('\n')

    #call merge sort on the array
    mergeSort(invAry, 0, lineCount-1)

    if (debugPrints):
        print("\nArray After Sort:")
        for element in invAry:
            print (element, end = ' | ')
        print('\n')

    print("There are "+ str(inversionCount)+" inversions")


##########################################################################
#call merge sort on the array
#modify merge function to do n choose 2 or whatever and tally up inversion count

def mergeSort(arr,l,r): 
    if l < r: 
  
        # Same as (l+r)//2, but avoids overflow for 
        # large l and h 
        m = (l+(r-1))//2
  
        # Sort first and second halves 
        mergeSort(arr, l, m) 
        mergeSort(arr, m+1, r) 
        merge(arr, l, m, r) 
        
def merge(arr, l, m, r):
    global inversionCount
    global debugPrints
    
    n1 = m - l + 1
    n2 = r- m 
  
    # create temp arrays 
    L = [0] * (n1) 
    R = [0] * (n2) 
  
    # Copy data to temp arrays L[] and R[] 
    for i in range(0 , n1): 
        L[i] = arr[l + i] 
  
    for j in range(0 , n2): 
        R[j] = arr[m + 1 + j] 
  
    # Merge the temp arrays back into arr[l..r] 
    i = 0     # Initial index of first subarray 
    j = 0     # Initial index of second subarray 
    k = l     # Initial index of merged subarray 
  
    while i < n1 and j < n2 : 
        if L[i] <= R[j]: 
            arr[k] = L[i]
            inversionCount += j #This line was added by me
            if (debugPrints):
                print("Plus " + str(j) + " inversions")
            i += 1
        else: 
            arr[k] = R[j] 
            j += 1
        k += 1
  
    # Copy the remaining elements of L[], if there 
    # are any 
    while i < n1: 
        arr[k] = L[i]
        inversionCount += j #This line was added by me
        if (debugPrints):
            print("Plus " + str(j) + " inversions")
        i += 1
        k += 1
  
    # Copy the remaining elements of R[], if there 
    # are any 
    while j < n2: 
        arr[k] = R[j] 
        j += 1
        k += 1
  
# l is for left index and r is right index of the 
# sub-array of arr to be sorted 

    #return invAry
    

main()
