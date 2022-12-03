import os
import sys
import hashlib
import filecmp as fc
# print("Fac hashul")
def get_hash(path):
    hashobj = hashlib
    with open(path, "rb") as file:
        return hashobj.md5(file.read()).hexdigest()

def get_files(path):
    files = []
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isfile(file_path):
            files.append(file_path)
    return files

def get_duplicate_files(files):
    hash_dict = {}
    for file in files:
        hash = get_hash(file)
        if hash in hash_dict:
            hash_dict[hash].append(file)
        else:
            hash_dict[hash] = [file]
    duplicates = []
    for hash in hash_dict:
        if len(hash_dict[hash]) > 1:
            duplicates.append(hash_dict[hash])
    return duplicates

def compare_duplicate_files(duplicates):
    for file in duplicates:
        if fc.cmp(file[0], file[1]) == False:
            duplicates.remove(file)
    return duplicates

# print("Remove duplicates")
def remove_duplicates(duplicates):
    for i, duplicate in enumerate(duplicates, start=1):
        print("The following files are identical:")
        # print(duplicate)
        for i in range(len(duplicate)):
            print(i+1, duplicate[i])
        print("Please select the file you want to keep [1..{}] ?".format(len(duplicate)))
        choice = int(input()) - 1
        for j in range(len(duplicate)):
            if j != choice:
                os.remove(duplicate[j])


# print("Main")
def main():
    if len(sys.argv) != 2:
        print("Usage: remove_duplicate.py <folder>")
        return
    elif not os.path.isdir(sys.argv[1]):
        print("The given path is not a directory")
        return
    files = get_files(sys.argv[1])
    duplicates = compare_duplicate_files(get_duplicate_files(files))
    remove_duplicates(duplicates)
    exit()


if __name__ == "__main__":
    main()