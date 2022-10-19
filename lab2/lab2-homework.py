def fibonacci(n):
    fib = [1, 1]
    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib


def prime_numbers(numbers):
    primes = []
    for number in numbers:
        if number > 1:
            for i in range(2, number):
                if (number % i) == 0:
                    break
            else:
                primes.append(number)
    return primes

print("EX 1:")
print(fibonacci(10))
print()
print("EX 2:")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(prime_numbers(numbers))
print()

def list_operations(a, b):
    return list(set(a) & set(b)), list(set(a) | set(b)), list(set(a) - set(b)), list(set(b) - set(a))

print("EX 3:")
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [4, 11, 12, 13]
print(list_operations(a, b))
print()

def song(musical_notes, moves, start_pos):
    song = []
    current_pos = start_pos
    for move in moves:
        song.append(musical_notes[current_pos])
        current_pos = (current_pos + move) % len(musical_notes)
    song.append(musical_notes[current_pos])
    return song

print("EX 4:")
notes = ["do", "re", "mi", "fa", "sol"]
moves = [1, -3, 4, 2]
start = 2

print(song(notes, moves, start))
print()

def matrix_operations(matrix):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            if i > j:
                matrix[i][j] = 0
    return matrix
print("EX 5:")
print(matrix_operations([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print()
def find_x_times(*lists, x):
    fin = []
    items = []
    for list in lists:
        fin += list

    for number in fin:
        if fin.count(number) == x and items.count(number) == 0:
            items.append(number)

    items.sort()
    return items

print("EX 6:")
print(find_x_times([1, 2, 3], [2, 3, 4], [4, 5, 6], [4, 1, "test"], x=2))
print()
def palindrome_check(number):
    number = str(number)
    if number == number[::-1]:
        return True
    else:
        return False


def palindrome_numbers(numbers):
    palindromes = []
    for number in numbers:
        if palindrome_check(number):
            palindromes.append(number)
    return len(palindromes), max(palindromes)

print("EX 7:")
print(palindrome_numbers([1 , 2, 101, 3, 4004, 23451, 898989, 234432, 10001, 454]))
print()
def ascii_code(x=1, *strings, flag):
    result = []
    for string in strings:
        if flag:
            result.append([char for char in string if ord(char) % x == 0])
        else:
            result.append([char for char in string if ord(char) % x != 0])
    return result


x = 2
strings = ["test", "hello", "lab002"]
flag = False
print("EX 8:")
print(ascii_code(x, *strings, flag=flag))
print()
def spectators(matrix):
    result = []
    for i in range(0, len(matrix[0])):
        max = matrix[0][i]
        for j in range(1, len(matrix)):
            if matrix[j][i] > max:
                max = matrix[j][i]
            else:
                result.append((j, i))
    return result

matrix = [[1, 2, 3, 2, 1, 1], [2, 4, 4, 3, 7, 2], [5, 5, 2, 5, 6, 4], [6, 6, 7, 6, 7, 5]]
print("EX 9:")
print(spectators(matrix))
print()
def tuple_list(*lists):
    result = []
    for i in range(0, max([len(x) for x in lists])):
        result.append(tuple([x[i] if len(x) > i else None for x in lists]))
    return result

print("EX 10:")
print(tuple_list([1,2,3], [5,6,7], ["a", "b", "c"]))
print()
print("Example 2")
print(tuple_list([1,2,3], [5,6,7], ["a", "b", "c"], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print()
def order_tuples(tuples):
    return sorted(tuples, key=lambda x: x[1][2])

tuples = ('abc', 'bcd'), ('abc', 'zza')
print("EX 11:")
print(order_tuples(tuples))
print()
def group_by_rhyme(words):
    result = []
    for word in words:
        for i in range(0, len(result)):
            if word[-2:] == result[i][0][-2:]:
                result[i].append(word)
                break
        else:
            result.append([word])
    return result

words = ['ana', 'banana', 'carte', 'arme', 'parte']

print("EX 12:")
print(group_by_rhyme(words))