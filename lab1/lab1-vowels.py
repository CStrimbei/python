string = str(input("Da-mi o propozitie: "))

def numaramivocalele():
    nr = 0
    for caracter in string:
        if caracter in "aeiouAEIOU":
            nr = nr + 1
    return nr;

print(numaramivocalele())