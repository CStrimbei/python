def fibonacci(n):
    fib = [1, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
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

#print(fibonacci(10))

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(prime_numbers(numbers))


def list_operations(a, b):
    return list(set(a) & set(b)), list(set(a) | set(b)), list(set(a) - set(b)), list(set(b) - set(a))

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# b = [4, 11, 12, 13]
# print(list_operations(a, b))

def song(musical_notes, moves, start_pos):
    song = []
    current_pos = start_pos
    for move in moves:
        song.append(musical_notes[current_pos])
        current_pos = (current_pos + move) % len(musical_notes)
    song.append(musical_notes[current_pos])
    return song

# notes = ["do", "re", "mi", "fa", "sol"]
# moves = [1, -3, 4, 2]
# start = 2
#
# print(song(notes, moves, start))


def matrix_operations(matrix):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            if i > j:
                matrix[i][j] = 0
    return matrix

# def print_matrix(matrix):
#     i = 0
#     while i!=len(matrix):
#         print(matrix[i])
#         i+=1

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print_matrix(matrix_operations(matrix))
# print(matrix_operations(matrix))

def find_x_times(*lists, x):
    items = []
    for list in lists:
        for item in list:
            if list.count(item) == x:
                items.append(item)
    return items

print(find_x_times([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], x=3))