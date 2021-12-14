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
        print("File already exists")
    else:
        with open(f"{name}.txt", "a", encoding="utf=8") as file_content:
            file_content.write(child_name+"\n")
            file_content.writelines(items)


def list_read():
    name = input("What is the name of your whishlist? ")
    with open(f"{name}.txt", "r") as file:
        print(file.readline())


def main():
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


if __name__ == "__main__":
    main()
