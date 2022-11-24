# Ex 1:
# Write a function that extracts the words from a given text as a parameter. A word is defined as a sequence of alpha-numeric characters.
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
# Write a function that receives as a parameter a regex string, a text string and a whole number x, and returns those long-length x substrings that match the regular expression.


def extract_words_regex(regex, text, x):
    import re
    words = re.findall(regex, text)
    return [word for word in words if len(word) == x]

print("Ex 2:")
print(extract_words_regex(r"\w+", "Hi, world! 123", 5))

# Ex 3:
# Write a function that receives as a parameter a string of text characters and a list of regular expressions and returns a list of strings that match on at least one regular expression given as a parameter.

def extract_words_regex_list(regex_list, text):
    import re
    words = []
    for regex in regex_list:
        words += re.findall(regex, text)
    return words

print("Ex 3:")
print(extract_words_regex_list([r"\w+", r"\d+"], "Hi, world! 123"))

# Ex 4:
# Write a function that receives as a parameter the path to an xml document and an attrs dictionary and returns those elements that have as attributes all the keys in the dictionary and values ​​the corresponding values. For example, if attrs={"class": "url", "name": "url-form", "data-id": "item"} the items selected will be those tags whose attributes are class="url" si name="url-form" si data-id="item".

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
# Write another variant of the function from the previous exercise that returns those elements that have at least one attribute that corresponds to a key-value pair in the dictionary.

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
# Write a function that, for a text given as a parameter, censures words that begin and end with vowels. Censorship means replacing characters from odd positions with *.

def censor_words(text):
    words = extract_words(text)
    for word in words:
        if word[0].lower() in "aeiou" and word[-1].lower() in "aeiou":
            text = text.replace(word, "".join([char if i % 2 == 0 else "*" for i, char in enumerate(word)]))
    return text

print("Ex 6:")
print(censor_words("Hello, world! Aeiou, aeiou!"))

# Ex 7:
# Verify using a regular expression whether a string is a valid CNP.

def is_valid_cnp(cnp):
    import re
    return bool(re.match(r"^[1-8]\d{2}(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])(0[1-9]|[1-4]\d|5[0-2])\d{4}$", cnp))

print("Ex 7:")
print(is_valid_cnp("5010407226719"))

# Ex 8:
# Write a function that recursively scrolls a directory and displays those files whose name matches a regular expression given as a parameter or contains a string that matches the same expression. Files that satisfy both conditions will be prefixed with ">>"

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
