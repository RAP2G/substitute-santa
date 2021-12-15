import os.path


def list_create():
    name = input("\nName your list: ")
    child_name = input("Name yourself: ")
    items = []
    items.append(input("What do you want for Christmas? ")+"\n")
    while True:
        answer = input("Do you want anything else?y/n ").lower()
        if answer == "yes" or answer == "y":
            items.append(input("What is it? ")+"\n")
        elif answer == "no" or answer == "n":
            break
    file_exists = os.path.exists(f"{name}.txt")
    if file_exists:
        print("File already exists. Choose another name.")
    else:
        with open(f"{name}.txt", "a", encoding="utf=8") as file_content:
            file_content.write(child_name+"\n")
            file_content.writelines(items)


def list_read():
    name = input("What is the name of your whishlist? ")
    file_exists = os.path.exists(f"{name}.txt")
    if file_exists:
        print("File already exists. Choose another name.")
    else:
        with open(f"{name}.txt", "r") as file:
            print(file.readline())
            print("WHISH LIST")
            for i in file:
                print(i.strip())


def naughty_list():
    print("Would you like to read the naughty list or add to it? r/a")
    while True:
        answer = input("Answer: ").lower()
        if answer == "r":
            with open("kolbarn.txt", "r") as file:
                print("NAUGHTY LIST\n")
                for i in file:
                    print(i.strip())
        elif answer == "a":
            with open("kolbarn.txt", "r") as file:
                print("NAUGHTY LIST")
                for i in file:
                    print(i.strip())
                while True:
                    answer = input(
                        "Add children to the naughty list. Type 'done' if you are done.  ")
                    if answer == "done":
                        answer = "q"
                        break
                    else:
                        with open("kolbarn.txt", "a", encoding="utf=8") as file_content:
                            file_content.write(answer+"\n")

        elif answer == "q":
            break
        else:
            print("Wrong Input\n")


def wish_list():
    print("Would you like to create a whish list? Or would you like to read one?")
    while True:
        print("Type: 'c' for create, 'r' for read or 'q' for quit")
        answer = input("Answer: ").lower()
        if answer == "c":
            list_create()

        elif answer == "r":
            list_read()
        elif answer == "q":
            break
        else:
            print("Wrong Input\n")


def main():
    print("Typing q will take you back to the main screen. And on the main screen it will end the program.")
    while True:
        answer = input("Naughty list or Whish list?N/W \n").upper()
        if answer == "N":
            naughty_list()
        elif answer == "W":
            wish_list()
        elif answer == "Q":
            break
        else:
            print("Wrong Input\n")


if __name__ == "__main__":
    main()
