# Dominic Meikle
# 2/27/35
# P2HW2
# This program calculates the average and sum of the users grades.

#gets the grades from user
m1 = float(input("Enter your rade for Module 1: "))
m2 = float(input("Enter your rade for Module 2: "))
m3 = float(input("Enter your rade for Module 3: "))
m4 = float(input("Enter your rade for Module 4: "))
m5 = float(input("Enter your rade for Module 5: "))
m6 = float(input("Enter your rade for Module 6: "))

#puts the grades in a dictionary
grades = {
    "Module 1":m1,
    "Module 2":m2,
    "Mudule 3":m3,
    "Module 4":m4,
    "Module 5":m5,
    "Module 6":m6
}


#calculates the average and sum, as well as determine the lowest and highest grades
low = min(grades.values())
high = max(grades.values())
gsum = m1 + m2 + m3 + m4 + m5 + m6
avg = gsum / 6

#displays the results
print()
print("----------Results----------")
print(f"{"Lowest Grade:":<20} {low:.1f}")
print(f"{"Highest Grade:":<20} {high:.1f}")
print(f"{"Sum of Grades:":<20} {gsum:.1f}")
print(f"{"Average:":<20} {avg:.2f}")
print("---------------------------")