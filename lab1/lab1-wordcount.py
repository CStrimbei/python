def wordCounter():
    string = input("Da-mi un string: ")

    if string.strip() == "":
        return 0
    cuvinte = string.split()

    return len(cuvinte)

print(wordCounter())