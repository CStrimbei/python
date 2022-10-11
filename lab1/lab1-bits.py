def countBits():
    n = int(input("Da-mi un numar: "))

    nbinary = bin(n)
    nbinary = int(nbinary[2:])
    #print(nbinary)
    count = 0

    while (nbinary):
        if (nbinary % 10) == 1:
            count = count + 1
        nbinary = nbinary//10
    print(count)

countBits()