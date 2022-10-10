def numbers():
    string = input("Da-mi un string: ")

    print("Debug: " + string)

    numerele = ""

    for caracter in string:
        if caracter.isdigit():
            numerele = numerele + caracter
    print("Ce am extras din stringul tau: " + numerele)

numbers()