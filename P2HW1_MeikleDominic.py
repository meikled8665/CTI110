# Dominic Meikle
# 2/25/25
# P2HW1
# This program calculates and displays travel expenses

print("This program calculates and displays travel expenses\n")

# Request information

budget = float(input("Enter Budget: "))
print()

location = input("Enter your travel destination: ")

print()
fuel = float(input("How much do you think you will spend on gas? "))

print()

hotel = float(input("Approximately, how much will you need for accomodation/hotel? "))
print()

food = float(input("Last, how much do you need for food? "))

# add expenses

expenses = fuel + hotel+ food
remainAmount = budget - expenses

# display results

print("\n------------Travel Expenses------------")
print(f"{"Location:":<20} {location}")
print(f"{"Initial Budget:":<20} ${budget}")
print(f"{"Fuel Cost:":<20} ${fuel}")
print(f"{"Accomodation:":<20} ${hotel}")
print(f"{"Food Cost:":<20} ${food}")
print(f"{"Total Cost:":<20} ${expenses}")
print("---------------------------------------\n")

print(f"{"Amount Remainig:":<20} ${remainAmount}")