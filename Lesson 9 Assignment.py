
#Lesson 9 Assignment
#import locale and set to US
import locale as lc
lc.setlocale(lc.LC_ALL, "en_US")
#Function to collect user input for income and return income to main:
def get_income():
    #loop until the user enters valid amount, in this case either 0 or a positive number, income designated float and exception handling for float error:
    while True:
        income=(input("Please enter your income :  "))
        try:
            your_income = float(income)
            if your_income > 0:
                print(f"\nYou have entered: {income}\n")
                return your_income
            else:
                print("\nPlease enter a valid number!\n")
        except ValueError:
            print("\nInvalid input, please enter a valid dollar amount.\n ")
#Function to create empty list for expenses, collect user input of expenses and append to list, then return list to main. 
# 0 to finish option and error for negative expenses, expense designated float and error handling.
def get_exp():
    exp_list = []
    while True:
        try:
            expense = float(input("\nPlease enter an expense and press enter, or press 0 when finished:  " ))
            if expense == 0:
                break
            if expense < 0:
                print("\nExpenses cannot be negative!\n")
                continue
            exp_list.append(expense)
        except ValueError:
            print("\nPlease enter a valid number!\n")
    return (exp_list)
#Function to return the sum of expenses list to the main function
def calc_exp(exp_list):
    return (sum(exp_list))
#Main function, print statement with purpose of the program, functions and their returned variables defined
#I used the f string ${VARIABLE:.2f} in print functions to format the final output.
def main():
    print("\n*********(: Budget Buddy :)*********\n*****Your Personal Budget Tracker!*****\n---------------------------------------")
    income = get_income()
    expenses = get_exp()
    total_exp = calc_exp(expenses)
    budget = income - total_exp
    #formatting the expenses list, indexing and using previously imported locale module
    #to format currency:
    formatted = [f"Expense {i+1}:  {lc.currency(expense, grouping=True)}" for i, expense in enumerate(expenses)]
    print("\nHere are your budget reults:\n---------------------------------------\n")
    print(f"Your total income is : ${income:.2f}")
    print(f"Your total expenses are : ${total_exp:.2f}")
    print(f"Remianing budget : ${budget:.2f}")
    #Print list of formatted expenses:
    print("\nList of Expenses:\n---------------------------------------\n")
    for formatted_exp in formatted:
        print(formatted_exp)
if __name__ == '__main__':
    main()
print("Completed by Laura Bartlett")
