#gcd

lst = []

x=0

n = int(input("Enter number of elements : "))

for i in range(0, n):
    ele = int(input())
    lst.append(ele)
#print(type(lst[1]))

def find_gcd(arr):
    if len(arr) <= 1:
        return arr
    else:
        for i in range(len(arr)-1):
            a = arr[i]
            b = arr[i+1]
            while b:
                a, b = b, a%b
            arr[i+1] = a
        return a
def main(array):
    print(find_gcd(array))

main(lst)