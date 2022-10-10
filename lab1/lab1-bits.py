def usefulBinary(n):
    return bin(n).replace("0b", "")

def countBits():
    n = int(input("Da-mi un numar: "))

    nbinary = int(usefulBinary(n))
    #print(nbinary)
    count = 0

    while (nbinary):
        if (nbinary % 10) == 1:
            count = count + 1
        nbinary = nbinary//10
    print(count)

countBits()