import utils as u

def main():
    print("Enter a number, or input 'q' to quit: ")
    tastatura = input()
    if(tastatura == 'q'):
        print("Goodbye!")
        return
    else:
        if(tastatura.isdigit()):
            print(u.process_item(int(tastatura)))
            main()
        else:
            print("Invalid input")
            main()
main()