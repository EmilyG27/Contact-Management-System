import os
import re

def read_contacts(filename):
    try:
        with open(filename, 'r') as file:
            contacts = []
            for line in file:
                name, number, email, address = line.strip().split(',')
                contacts.append({'name': name, 'number': number, 'email': email, 'address': address})
            return contacts
    except FileNotFoundError:
        return []
    
def write_contacts(filename, contacts):
    with open(filename, 'w') as file:
        for contact in contacts:
            file.write(f"{contact['name']},{contact['number']},{contact['email']},{contact['address']}\n")

def add_contact(contacts, filename):
    name = input("Enter name: ")
    number = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    new_contact = {'name': name, 'phone number': number, 'email': email, 'address': address}
    contacts.append(new_contact)
    with open(filename, 'a') as file:
        file.write(f"Name: {name}, Phone Number: {number}, Email: {email}, Address: {address}\n")
    print(f"{name} added to contacts")

def edit_contact(contacts):
    contacts = read_contacts('contacts.txt')
    contact_to_edit = input("Enter the name of the contact you want to edit: ")
    if contact_to_edit in contacts:           
        name = input("Enter name: ")
        number = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        new_info = {'Name': name, 'Phone Number': number, 'Email': email, 'Address': address}
        contacts[new_info]
        print(f"{name} has been updated")

def delete_contact(contacts, filename):
    contact_to_delete = input("Enter name of contact to delete: ")
    if contact_to_delete in contacts:
        del contact_to_delete
    else:
        print("Contact not found")

def search_contact(contacts):
    name = input("Enter the name of the contact to search for: ")
    found_contact = [contacts['name'] for contact in contacts if name in contact['name']]
    print(found_contact)

def display_contacts(contacts):
    for contact in contacts:
        print(contact['name', 'number', 'email', 'address'])

def export_to_textfile():
    path = input("Enter the path to the file you would like to export: ")
    os.makedirs(path, exist_ok=True)    


def main():
    contacts = read_contacts('contacts.txt')
    print("Welcome to the Contact Management System!") 

    while True:
        print("Menu:\n1. Add a new contact\n2. Edit an existing contact\n3. Delete a contact\n4. Search for a contact\n5. Display all contacts\n6. Export contacts to a text file\n7. Quit")
        choice = input("Please enter a number from the list above: ")
        if choice == "1":
            add_contact(contacts, 'contacts.txt')
        elif choice == "2":
            edit_contact(contacts)
        elif choice == "3":
            delete_contact(contacts, 'contacts.txt')
        elif choice == "4":
            search_contact(contacts, 'contacts.txt')
        elif choice == "5":
            display_contacts(contacts, 'contacts.txt')
        elif choice == "6":
            export_to_textfile(contacts, 'contacts.txt')
        elif choice == "7":
            break
        else:
            print("Invalid input. Please enter a number from the menu. ")

if __name__ == "__main__":
    main()
        