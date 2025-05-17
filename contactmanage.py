contacts=[]

def add_contacts(name,phone_num,contacts):
    for contact in contacts:
        if contact["name"]==name or contact["phone"]==phone_num:
            print("contacts is already saved")
            return
    contacts.append({"name":name,"phone":phone_num})
    print(f"contacts {name} added")

def view_contacts(contacts):
    if not contacts:
        print("no contacts available!")

    else:
        for i,contact in enumerate(contacts,1):
            print(f"{i}.{contact['name']}-{contact['phone']}")


def search_contact(name,contacts):
    if not contacts:
        print("no contacts available!")
    else:
        for contact in contacts:
            if contact['name'].lower()==name.lower():
                print(f"found:{contact['name']}-{contact['phone']}")


def delete_contact(name,contacts):
    if not contacts:
        print("no contacts available!")
    
    elif contact['name'].lower()!=name.lower():
        print("contact not found")

    else:
        for contact in contacts:
             if contact['name'].lower()==name.lower():
                 contacts.remove(contact)
                 print(f"{contact['name']}")
            
def update_contact(name,phone_num,contacts):
    for contact in contacts:
        if contact['name'].lower()==name.lower():
            new_name=input("enter new name to update!!:-")
            new_phone=input("enter new phone number to update!!:-")

            contact['name']=new_name
            contact['phone']=new_phone

            print(f"update contact to {contact['name']-contact[phone_num]}")
        

while True:
    print("\n--- Contact Book Menu ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5.update contact info")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter contact name: ")
        phone = input("Enter phone number: ")
        add_contacts(name, phone, contacts)

    elif choice == "2":
        view_contacts(contacts)

    elif choice == "3":
        name = input("Enter name to search: ")
        search_contact(name, contacts)

    elif choice == "4":
        name = input("Enter name to delete: ")
        delete_contact(name, contacts)

    elif choice == "5":
        name=input("enter name to update the contact info:-")
        update_contact(name,phone,contacts)

    elif choice == "6":
        print("thanks ,goodbye!!")
        
    else:
        print("Invalid choice, please try again.")