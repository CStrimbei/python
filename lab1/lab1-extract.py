def numbers():
    string = input("Da-mi un string: ")

    gasit = False

    numerele = ''

    i = 0

    while(gasit!=True):
        
        if(string[i].isdigit()):
            numerele+=string[i]
            if(string[i+1].isdigit()==False):
                gasit = True
        i = i+1
    print(numerele)

numbers()