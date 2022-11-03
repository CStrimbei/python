# Ex1
import os

def get_extensions(dir):
    extensions = []
    for file in os.listdir(dir):
        if os.path.isfile(file):
            extension = file.split('.')[-1]
            if extension not in extensions:
                extensions.append(extension)
    return sorted(extensions)
print("Ex1")
print(get_extensions('../lab4'))

# Ex2

def get_files(dir, file):
    with open(file, 'w') as f:
        for file in os.listdir(dir):
            if os.path.isfile(file):
                if file[0] == 'A':
                    f.write(os.path.abspath(file) + '\n')

print("Ex2")
print("Am scris in fisierul 'files.txt'")
get_files('../lab4', 'files.txt')

# Ex3

def get_last_20_chars_rec(my_path):
    if os.path.isfile(my_path):
        with open(my_path, 'r') as f:
            content = f.read()
            if len(content) > 20:
                return content[-20:]
            else:
                return content
    else:
        return 'Not a file'

print("Ex3")
print(get_last_20_chars_rec('../lab4/Alune.txt'))

# Ex 4


def get_extensions(dir):
    extensions = []
    for file in os.listdir(dir):
        if os.path.isfile(file):
            extension = file.split('.')[-1]
            if extension not in extensions:
                extensions.append(extension)
    return sorted(extensions)

print("Ex4")
print(get_extensions(input()))

# Ex 5
