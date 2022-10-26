# Ex 1: Write a function that receives as parameters two lists a and b and returns a list of sets containing: (a intersected with b, a reunited with b, a - b, b - a)

def ex1(a: list, b: list):
    return [set(a) & set(b), set(a) | set(b), set(a) - set(b), set(b) - set(a)]

a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7, 8]
print("Ex1: ")
print(ex1(a, b))
print()

# Ex 2: Write a function that receives a string as a parameter and returns a dictionary in which the keys are the characters in the character string and the values are the number of occurrences of that character in the given text.

def ex2(text: str):
    cnt = dict()
    for char in string:
        if cnt.get(char) is None:
            cnt[char] = 1
        else:
            cnt[char] += 1
    return cnt
string = "Ana has apples"
print("Ex2: ")
print(ex2(string))
print()

# Ex 3: Compare two dictionaries without using the operator "==" returning True or False. (Attention, dictionaries must be recursively covered because they can contain other containers, such as dictionaries, lists, sets, etc.)

def ex3_rec(dict1: dict, dict2: dict):
    if dict1.keys() != dict2.keys():
        return False
    for key in dict1.keys():
        if type(dict1[key]) is dict:
            if not ex3_rec(dict1[key], dict2[key]):
                return False
        elif dict1[key] != dict2[key]:
            return False
    return True

dict1 = {"a": 1, "b": 2, "c": {"d": 3, "e": 4}}
dict2 = {"a": 1, "b": 2, "c": {"d": 3, "e": 4}}
dict3 = {"a": 1, "b": 2, "c": {"d": 3, "e": 5}}
print("Ex3: ")
print(ex3_rec(dict1, dict2))
print(ex3_rec(dict1, dict3))
print()

# Ex 4: The build_xml_element function receives the following parameters: tag, content, and key-value elements given as name-parameters. Build and return a string that represents the corresponding XML element. Example: build_xml_element ("a", "Hello there", href =" http://python.org ", _class =" my-link ", id= " someid ") returns  the string = "<a href=\"http://python.org \ "_class = \" my-link \ "id = \" someid \ "> Hello there </a>"

def build_xml_element(tag: str, content: str, **kwargs):
    string = "<" + tag
    for key in kwargs:
        string += " " + key + "=\"" + kwargs[key] + "\""
    string += ">" + content + "</" + tag + ">"
    return string

print("Ex4: ")
print(build_xml_element("a", "Hello there", href="http://python.org", _class="my-link", id="someid"))
print()

# Ex 5: The validate_dict function that receives as a parameter a set of tuples ( that represents validation rules for a dictionary that has strings as keys and values) and a dictionary. A rule is defined as follows: (key, "prefix", "middle", "suffix"). A value is considered valid if it starts with "prefix", "middle" is inside the value (not at the beginning or end) and ends with "suffix". The function will return True if the given dictionary matches all the rules, False otherwise.

def ex5_validate_dict(rules: set, dict: dict):
    for rule in rules:
        if not (dict[rule[0]].startswith(rule[1]) and dict[rule[0]].endswith(rule[3]) and rule[2] in dict[rule[0]][len(rule[1]):-len(rule[3])]):
            return False
    return True

rules = {("key1", "", "acasa", ""), ("key2", "", "valid", "")}
example = {"key1": "hai acasa ca-i mai cald", "key2" : "nu-i valid"}

print("Ex5: ")
print(ex5_validate_dict(rules, example))
print()


# Ex 6: Write a function that receives as a parameter a list and returns a tuple (a, b), representing the number of unique elements in the list, and b representing the number of duplicate elements in the list (use sets to achieve this objective).

def ex6(lst: list):
    return (len(lst), len(lst) - len(set(lst)))

lst = ['ioana', 'maria', 'cristina', 'maria', 'maria', 'maria', 'cristina']
print("Ex6: ")
print(ex6(lst))
print()

# Ex 7: Write a function that receives a variable number of sets and returns a dictionary with the following operations from all sets two by two: reunion, intersection, a-b, b-a. The key will have the following form: "a op b", where a and b are two sets, and op is the applied operator: |, &, -.

def ex7(*args: set):
    cnt = dict()
    for i in range(len(args)):
        for j in range(i + 1, len(args)):
            cnt[str(args[i]) + " | " + str(args[j])] = args[i] | args[j]
            cnt[str(args[i]) + " & " + str(args[j])] = args[i] & args[j]
            cnt[str(args[i]) + " - " + str(args[j])] = args[i] - args[j]
            cnt[str(args[i]) + " - " + str(args[j])] = args[j] - args[i]
    return cnt

set1 = {1, 2}
set2 = {2, 3}

print("Ex7: ")
print(ex7(set1, set2))
print()

# Ex 8: Write a function that receives a single dict parameter named mapping. This dictionary always contains a string key "start". Starting with the value of this key you must obtain a list of objects by iterating over mapping in the following way: the value of the current key is the key for the next value, until you find a loop (a key that was visited before). The function must return the list of objects obtained as previously described.

def ex8(mapping: dict):
    lst = []
    key = mapping["start"]
    while key not in lst:
        lst.append(key)
        key = mapping[key]
    return lst

mapping = {'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}

print("Ex8: ")
print(ex8(mapping))
print()

# Ex 9: Write a function that receives a variable number of positional arguments and a variable number of keyword arguments adn will return the number of positional arguments whose values can be found among keyword arguments values.

def ex9(*args, **kwargs):
    cnt = 0
    for arg in args:
        if arg in kwargs.values():
            cnt += 1
    return cnt

print("Ex9: ")
print(ex9(1, 2, 3, 4, x=1, y=2, z=3, w=5))
print()
