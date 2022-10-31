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
