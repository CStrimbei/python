def process_item(x):
    x += 1
    while True:
        for i in range(2, x):
            if x % i == 0:
                x += 1
                break
        else:
            return x

# print(process_item(int(input("Enter a number: "))))