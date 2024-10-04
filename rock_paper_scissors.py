# Lesson 4 Assignment

from random import randrange

def your_weapon():
    print()
    your_choice=int(input("Choose (1) for ROCK, (2) for PAPER or (3) for SCISSORS: "))
    print()
    return your_choice

def my_weapon():
    
    random_number = randrange(1,4)
    my_choice=random_number
    print(f"My choice is {random_number}")
    return my_choice

def winner(your_choice, my_choice):
    
    if (your_choice == 1) and (my_choice == 2):
        print()
        print("You lose! Paper covers rock!")
        print()
        
    elif (your_choice == 1) and (my_choice == 3):
        print()
        print("You win! Rock crushes scissors!")
        print()
        
    elif (your_choice== 2) and (my_choice == 1):
        print()
        print("You win! Paper covers rock!")
        print()
        
    elif (your_choice == 2) and (my_choice == 3):
        print()
        print("You lose! Scissors cut paper!")
        print()
        
    elif (your_choice == 3) and (my_choice == 1):
        print()
        print("You lose! Rock crushes scissors!")
        print()
        
    elif (your_choice == 3) and (my_choice == 2):
            print()
            print("You win! Scissors cut paper!")
            print()
            
    elif your_choice == my_choice:
        print()
        print("It's a tie!")
        print()        
    
    
def main():
    print()
    print("Let's play Rock, Paper Scissors!")
    print()
    continue_option = "y"
    while continue_option.lower() == "y":
        your_choice=your_weapon()
        my_choice=my_weapon()
        winner(your_choice, my_choice)
        continue_option = input(" Play again? y/n: ")
        print()
    print()
    print("Bye!")
    print()

if __name__ == "__main__":
    main()

print("Completed by Laura Bartlett")
