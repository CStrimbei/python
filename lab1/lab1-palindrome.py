def palindrom():
    n = int(input("Da-mi un numar: "))

    aux = n

    invers = 0

    while n > 0:
        cif = n % 10
        invers = invers * 10 + cif
        n = int(n / 10)

    if aux == invers:
        print("Numarul e palindrom!")
    else:
        print("Numarul nu e palindrom!")


palindrom()
