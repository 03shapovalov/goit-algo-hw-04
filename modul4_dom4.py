def parse_input(command):
    parts = command.split()
    keyword = parts[0].lower()
    args = parts[1:]

    return keyword, args

def add_contact(name, phone, contacts):
    contacts[name] = phone
    print("Contact added.")

def change_contact(name, new_phone, contacts):
    if name in contacts:
        contacts[name] = new_phone
        print("Contact updated.")
    else:
        print("Contact not found.")

def show_phone(name, contacts):
    if name in contacts:
        print(contacts[name])
    else:
        print("Contact not found.")

def show_all(contacts):
    for name, phone in contacts.items():
        print(f"{name}: {phone}")

def main():
    contacts = {}

    while True:
        command = input("Enter command: ")
        keyword, args = parse_input(command)
        if keyword == "hello":
            print("How can I help you?")
        elif keyword == "add":
            if len(args) == 2:
                add_contact(args[0], args[1], contacts)
            else:
                print("Invalid command.")
        elif keyword == "change":
            if len(args) == 2:
                change_contact(args[0], args[1], contacts)
            else:
                print("Invalid command.")
        elif keyword == "phone":
            if len(args) == 1:
                show_phone(args[0], contacts)
            else:
                print("Invalid command.")
        elif keyword == "all":
            if len(args) == 0:
                show_all(contacts)
            else:
                print("Invalid command.")
        elif keyword == "exit" or keyword == "close":
            print("Good bye!")
            break
        else:
            print("Invalid command.")
if __name__ == "__main__":
    main()
