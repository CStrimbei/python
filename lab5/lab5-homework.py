# Ex 2:

def sum_of_kwargs(*args, **kwargs):
    sum = 0
    for key, value in kwargs.items():
        sum += value
    return sum

sum_of_kwargs_lambda = lambda *args, **kwargs: sum(kwargs.values())

print("Ex 2: ")

print("Normal function: ")
print(sum_of_kwargs(a=1, b=2, c=3))

print("Lambda function: ")
print(sum_of_kwargs_lambda(a=1, b=2, c=3))

# Ex 3: 
# Method 1: Using functions

def get_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in string if char in vowels]

print("Ex 3: ")

print("Function method: ")
print(get_vowels("Programming in Python is fun"))


get_vowels_lambda = lambda string: [char for char in string if char in ['a', 'e', 'i', 'o', 'u']]
print("Anonymous function method: ")
print(get_vowels_lambda("Programming in Python is fun"))

def get_vowels_filter(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return list(filter(lambda char: char in vowels, string))

print("Filter method: ")
print(get_vowels_filter("Programming in Python is fun"))

# Ex 4:

def my_function(*args, **kwargs):
    result = []
    result_args = [arg for arg in args if type(arg) == dict and len(arg) >= 2 and any([True for key in arg if type(key) == str and len(key) >= 3])]
    result_kwargs = {key: value for key, value in kwargs.items() if type(value) == dict and len(value) >= 2 and any([True for key in value if type(key) == str and len(key) >= 3])}
    result.extend(result_args)
    result.append(result_kwargs)
    return result
print("Ex 4: ")
print(my_function({1: 2, 3: 4, 5: 6}, {'a': 5, 'b': 7, 'c': 'e'}, {2: 3}, [1, 2, 3], {'abc': 4, 'def': 5}, 3764, dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'}, test={1: 1, 'test': True}))

# Ex 5:


def get_numbers(list):
    return [element for element in list if type(element) == int or type(element) == float]

print("Ex 5: ")
print(get_numbers([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0]))

# Ex 6:

def get_pairs(parlist):
    even = [element for element in parlist if element % 2 == 0]
    odd = [element for element in parlist if element % 2 != 0]
    return list(zip(even, odd))

print("Ex 6: ")
print(get_pairs([1, 3, 5, 2, 8, 7, 4, 10, 9, 2]))
