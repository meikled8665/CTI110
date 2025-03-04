# Dominic Meikle
# 2/27/35
# P2HW2
# This program calculates the average and sum of the users grades.

#gets the grades from user
mod1 = float(input("Enter grade for Module 1: "))
mod2 = float(input("Enter grade for Module 2: "))
mod3 = float(input("Enter grade for Module 3: "))
mod4 = float(input("Enter grade for Module 4: "))
mod5 = float(input("Enter grade for Module 5: "))
mod6 = float(input("Enter grade for Module 6: "))

#puts the grades in a dictionary
gradelist = [] #creates empty list
gradelist = [mod1, mod2, mod3, mod4, mod5, mod6]

#calculates the average and sum, as well as determine the lowest and highest grades
glen = len(gradelist)
low = min(gradelist)
high = max(gradelist)

gsum = sum(gradelist)
avg = sum / glen

#displays the results
print()
print("----------Results----------")
print(f"{"Lowest Grade:":<20} {low:.1f}")
print(f"{"Highest Grade:":<20} {high:.1f}")
print(f"{"Sum of Grades:":<20} {gsum:.1f}")
print(f"{"Average:":<20} {avg:.2f}")
print("---------------------------")