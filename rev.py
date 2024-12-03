#Final Review Program
import csv
import os
from datetime import datetime

# Function to read info from .txt file
def read_employee_contact_info(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    contacts = []
    for line in lines:
        line = line.strip()
        if line:
            name, email = line.split(',')
            contacts.append([name.strip(), email.strip()])
    return contacts

# Function to list contact info
def list_contacts(contacts):
    print(f"{'Name':<20} {'Email':<30}")
    print("-" * 50)
    for idx, contact in enumerate(contacts):
        print(f"{idx+1:<3} {contact[0]:<20} {contact[1]:<30}")

# Function to write info to CSV file
def write_to_csv(contacts, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Email'])
        writer.writerows(contacts)
    print(f"Written by Your Name")

# Function to edit a contact, -1 to exit, with error handling
def edit_contact(contacts):
    list_contacts(contacts)
    try:
        choice = int(input("Enter the number of the contact to edit (or -1 to exit): "))
        if choice == -1:
            return
        if 1 <= choice <= len(contacts):
            name = input("Enter new name: ")
            email = input("Enter new email: ")
            contacts[choice-1] = [name.strip(), email.strip()]
        else:
            print("Invalid selection.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to delete a contact, with error handling
def delete_contact(contacts):
    list_contacts(contacts)
    try:
        choice = int(input("Enter the number of the contact to delete (or -1 to exit): "))
        if choice == -1:
            return
        if 1 <= choice <= len(contacts):
            del contacts[choice-1]
            print("Contact deleted.")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    print("Welcome to the Employee Contact Directory")
    start_time = datetime.now()
    print(f"Program started at: {start_time.strftime('%m/%d/%Y %I:%M:%S %p')}")


    contacts = read_employee_contact_info(r'C:\Users\nyred\OneDrive\Desktop\programming_final_rev\employee_contact_info.txt')

    while True:
        list_contacts(contacts)
        print("\nOptions:\n1. Edit contact\n2. Delete contact\n3. Write to CSV file\n4. Exit")
        try:
            choice = int(input("Select an option: "))
            if choice == 1:
                edit_contact(contacts)
            elif choice == 2:
                delete_contact(contacts)
            elif choice == 3:
                filename = input("Choose file name (e.g., contacts.csv): ")
                write_to_csv(contacts, filename)
            elif choice == 4:
                break
            else:
                print("Invalid option. Please choose again.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        except Exception as e:
            print(f"An error occurred: {e}")

    end_time = datetime.now()
    print(f"Program ended at: {end_time.strftime('%m/%d/%Y %I:%M:%S %p')}")

if __name__ == "__main__":
    main()

print("Completed by Laura Bartlett")

