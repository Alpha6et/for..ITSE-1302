#Lesson 5 Assignment
#Grade Calculator

#create grades list
grades=[]

#function to get user input and add input to grades list
#included "-1 to stop" for when the user is done entering grades
def get_grades(): 
    while True:
        user_grade = int(input("Enter grade now, enter -1 to stop:    "))
        if user_grade != -1:
            grades.append(user_grade)
        else:
            break
    print("You grades are:")    
    print(grades)

#function to drop the lowest grade 
def drop_low():
    print()
    print("Removing lowest grade.")
    print()
    if grades:
        lowest= min(grades)
        lowest_index= grades.index(lowest)
        grades.pop(lowest_index)
    print("Your grades are:")
    print (grades)

#function to drop one random grade
def drop_rand():
    import random
    print()
    print("Removing random grade.")
    print()

    random_grade = random.choice(grades)
    grades.remove(random_grade)

    print("Your grades are:")
    print(grades)

#funtion to allow user to edit grade values 
#I added "-1 to finish" for when the user is done editing
#or if they want to skip editing. Used "if to_edit == -2" becuase 
#it will not work with -1 because counting is starting at 0 
def edit():
    print()
    print("Edit a grade:")
    print()
    for index, item in enumerate(grades, start=1):
        print(f"{index} . {item}")
        print()
    while True:
        to_edit = int(input("Choose which grade to edit or -1 to finish: ")) - 1
        if to_edit == -2:
            break
        if 0 <= to_edit < len(grades):
            edited = int(input("Enter new grade: "))
            grades[to_edit] = edited
        else:
            print("Error: please enter a value that corresponds to a grade.")
            print()
    print()
    print("Your grades are: ")
    print(grades)

#function to sort then reverse the list
def sort_rev():
    print()
    print("Sorting and reversing grades...")
    print()
    grades.sort()
    grades.reverse()
    print(grades)

#function to calculate and print list total, then calculate and print list average
def tot_avg():
    print()
    print("Calculating total and average...")
    print()
    total = sum(grades)
    print("Total: ")
    print(total)
    avg = total / len(grades)
    print()
    print("Average: ")
    print(int(avg))

# Defined main() and ran all my functions within main,
# included "hello" and "goodbye" print statements
def main():
    print()
    print("Welcome to The Grade Calculator")
    print()
    
    get_grades()
    drop_low()
    drop_rand()
    edit()
    sort_rev()
    tot_avg()
    print()
    print("Thank you for using The Grade Calculator!")
    print()
main()
    
print("Completed by Laura Bartlett")