def cameltosnake():
    string = input("Da-mi un string: ")
    rez = [string[0].lower()]
    for char in string[1:]:
        if char in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
            rez.append('_')
            rez.append(char.lower())
        else:
            rez.append(char)
    print(''.join(rez))

cameltosnake()
