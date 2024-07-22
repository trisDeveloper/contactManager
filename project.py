import os

def load(file_path):
    contacts = {}
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            for line in file:
                name, phone = line.strip().split(',')
                contacts[name] = phone
    return contacts

def save(contacts, file_path):
    with open(file_path, 'w') as file:
        for name, phone in contacts.items():
            file.write(f"{name},{phone}\n")

def add(contacts, Input=None, Output=None):
    if Input is None:
        Input = os.sys.stdin
    if Output is None:
        Output = os.sys.stdout
    
    name =  input("Enter contact name: ") or Input.readline().strip() 
    phone = input("Enter contact phone number: ") or Input.readline().strip() 
    contacts[name] = phone
    print(f"Contact {name} added.", file=Output)

def view(contacts, Output=None):
    if Output is None:
        Output = os.sys.stdout
    
    if contacts:
        print("\nContact List:", file=Output)
        for name, phone in contacts.items():
            print(f"Name: {name}, Phone: {phone}", file=Output)
    else:
        print("\nNo contacts found.", file=Output)

def delete(contacts, Input=None, Output=None):
    if Input is None:
        Input = os.sys.stdin
    if Output is None:
        Output = os.sys.stdout
    
    name = input("Enter the name of the contact to delete: ") or Input.readline().strip()
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted.", file=Output)
    else:
        print(f"Contact {name} not found.", file=Output)

def main():
    file_path = 'contacts.txt'
    contacts = load(file_path)
    while True:
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Delete Contact")
        print("4. Exit")
        choice = input("what do you want? ")
        if choice == '1':
            add(contacts)
        elif choice == '2':
            view(contacts)
        elif choice == '3':
            delete(contacts)
        elif choice == '4':
            save(contacts, file_path)
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == '__main__':
    main()
