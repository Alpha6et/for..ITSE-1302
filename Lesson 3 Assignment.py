##Lesson 3 Assignment##
amount=int(input("Enter the investment amount (greater than 0 but less than 50,000)"))
while amount <= 0 or amount > 50000:
    print("Invalid input, please try again.")
    amount=int(input("Enter the investment amount (greater than 0 but less than 50,000)"))
rate=int(input("Enter the interest rate (greater than 0 but less than 15)"))
while rate <= 0 or rate > 15:
    print("Invalid input, please try again.")
    rate=int(input("Enter the interest rate (greater than 0 but less than 15)"))
duration=int(input("Enter the duration of the investment in years (greater than 0)."))
while duration <= 0:
    print("Invalid input, please try again.")
    duration=int(input("Enter the duration of the investment in years (greater than 0)"))
months=12 
for period in range (duration + 1):
        total = "%.2f" % (amount * (pow((1 + rate / 100 / months), months * period)))
        print(f'Year', period + 1, total)
print("Completed by Laura Bartlett")




