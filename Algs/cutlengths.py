#Jacob Siepker
#CSC 321 Algs
#Final Exam | Cut Lengths
#3/17/2021


def main():

    sizeClasses = [7, 6, 2, 1]

    cut(12, sizeClasses)


def cut(size, sizeClasses):
    sizes = []
    for element in sizeClasses:
        sizes.append(0)
    cutHelper(sizes, sizeClasses, size)
    printOutput(size, sizes, sizeClasses)


def cutHelper(sizes, sizeClasses,size):

    if (size == 0):
        pass

    else:
        for i in range(len(sizeClasses)):
            if (sizeClasses[i] <= size):
                sizes[i]+=1
                cutHelper(sizes, sizeClasses, size-sizeClasses[i])
                break


def printOutput(size, sizes, sizeClasses):

    print(f"Board length {size}\nPiece size\t\tCount")

    for i in range(len(sizeClasses)):
        print(f"{sizeClasses[i]}\t\t\t{sizes[i]}")
        

main()
