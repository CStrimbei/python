def mostCommon():
    string = input("Da-mi un string: ")
    max = 1

    for c in string:
        if c != ' ':
            min = string.count(c)
            if min>max:
                max = min
                rez = c
    print(rez)

mostCommon()