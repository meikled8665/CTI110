# Dominic Meikle
# 2/13/25
# P1HW2
# This program does some basic math on numbers that are enterted.

##ask user for budget
##ask user for travel destination
##ask user for how much they will spend on gas
##ask user for how much they will spend on accommodation
##ask user for how much they will spend on food
##add expenses
##subtract expenses from budget
##dispay results

print("This program calculates and displays travel expenses\n")

budg = int(input("Enter Budget: "))
dest = str(input("\nEnter your travel destination: "))
gas = int(input("\nHow much do you think you sill spend on gas? "))
acc = int(input("\nApproximately, how much will you need for accomodation/hotel? "))
food = int(input("\nLast, how much do you need for food? "))

bal = int(budg - (gas + acc + food))

print()
print(str("-"*12), "Travel Expenses", str("-"*12))

print("Locaton:", dest)
print("Initial Budget:", budg, "\n")

print("Fuel:", gas)
print("Accomodation:", acc)
print("Food:", food, "\n")

print("Remaining Balance:", bal)
