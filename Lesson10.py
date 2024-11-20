##Lesson 10 Assignment
#function to index and find the sub-string
def find(string, sub_string):
    index = string.find(sub_string)
    if index != -1:
        print(f"'{sub_string}' was found at index {index}")
    else: 
        print(f"'{sub_string}' not found!")
    return index
#function to ask user if they want to replace the substring, requires the user
#to enter y or n, otherwise gives invalid entry message
def replace_choice():
    while True:
        choice = input("Do you want to replace the sub-string with a new string? y/n : ")
        if choice in ['y','n']:
            return choice == 'y'
        else:
            print("Invalid entry, please enter y for yes or n for no!")
#function to replace the sub-string
def replace(string, sub_string):
    new = input("Please enter the new string: ")
    new_string = string.replace(sub_string, new)
    print(f"New String: {new_string}")
    return new_string
def main():
    print("String Replacement Tool")
    print("-" * 20)
    #variables to store the string and sub-string the user enters
    string = input("Enter the string you want to search through: ")
    sub_string = input("Enter the string you want to search for: ")
    print("-" * 20)
    #calling on the find() replace_choice() and replace() functions:
    index = find(string, sub_string)
    if index != -1:
        if replace_choice():
            replace(string,sub_string)
        else:
            print("No replacement was made.")
    else:
        print("Sub-string not found so no replacement was made.")
    print("-" * 20)
    print("Thank you for using the String Replacement Tool!")
if __name__ == "__main__":
    main()
print("-" * 20)
print("Completed by Laura Bartlett")
    