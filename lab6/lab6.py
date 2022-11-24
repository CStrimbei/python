# Ex 1:
import os
import re

def extract_words(text):
    words = []
    word = ""
    for char in text:
        if char.isalnum():
            word += char
        else:
            if word != "":
                words.append(word)
                word = ""
    if word != "":
        words.append(word)
    return words
print("Ex 1:")
print(extract_words("Hello, world! 123"))

# Ex 2:


def extract_words_regex(regex, text, x):
    import re
    words = re.findall(regex, text)
    return [word for word in words if len(word) == x]

print("Ex 2:")
print(extract_words_regex(r"\w+", "Hi, world! 123", 5))

# Ex 3:

def extract_words_regex_list(regex_list, text):
    import re
    words = []
    for regex in regex_list:
        words += re.findall(regex, text)
    return words

print("Ex 3:")
print(extract_words_regex_list([r"\w+", r"\d+"], "Hi, world! 123"))

# Ex 4:

def extract_elements(path, attrs):
    import xml.etree.ElementTree as ET
    tree = ET.parse(path)
    root = tree.getroot()
    elements = []
    for element in root.iter():
        if all([element.attrib.get(key) == value for key, value in attrs.items()]):
            elements.append(element)
    return elements

print("Ex 4:")
print(extract_elements("lab6.xml", {'seven': 'engine'}))

# Ex 5:

def extract_elements(path, attrs):
    import xml.etree.ElementTree as ET
    tree = ET.parse(path)
    root = tree.getroot()
    elements = []
    for element in root.iter():
        if any([element.attrib.get(key) == value for key, value in attrs.items()]):
            elements.append(element)
    return elements

print("Ex 5:")
print(extract_elements("lab6.xml", {'seven': 'engine', 'sky': 'happily'}))

# Ex 6:

def censor_words(text):
    words = extract_words(text)
    for word in words:
        if word[0].lower() in "aeiou" and word[-1].lower() in "aeiou":
            text = text.replace(word, "".join([char if i % 2 == 0 else "*" for i, char in enumerate(word)]))
    return text

print("Ex 6:")
print(censor_words("Hello, world! Aeiou, aeiou!"))

# Ex 7:

def is_valid_cnp(cnp):
    import re
    return bool(re.match(r"^[1-8]\d{2}(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])(0[1-9]|[1-4]\d|5[0-2])\d{4}$", cnp))

print("Ex 7:")
print(is_valid_cnp("5010407226719"))

# Ex 8:

def find_files(path, regex):
    for (root, directories, files) in os.walk(path):
        for file in files:
            ok = 0
            if re.match(regex, file):
                ok += 1

            try:
                f = open(os.path.join(root, file), 'r', encoding='utf-8', errors='ignore')
                for line in f:
                    tmp_line = line.strip()
                    if re.match(regex, tmp_line):
                        ok += 1
                        break
                f.close()
            except IOError:
                print("Unable to open file: " + file)

            if ok == 1:
                print(file)
            elif ok == 2:
                print(">>" + file)

print("Ex 8:")
find_files("../lab6", r"\w+")
