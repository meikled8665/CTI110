# Dominic Meikle
# 3/18/25
# P3HW2
# This program calculates the pay and overtime pay using input from the user.

name = input("Enter employee's name: ")
hours = float(input("Enter number of hours worked: "))
rate = float(input("Enter employee's pay rate: "))
totalhours = hours

if hours > 40:
    overtimehours = hours - 40
    hours = hours - overtimehours
    overtimepay = (1.5 * rate) * overtimehours
else: 
    overtimepay = 0
    overtimehours = 0

regpay = hours * rate
totalpay = regpay + overtimepay

print("-"*115)

print(f"{"Employee name:":<15} {name:<20}")
print()

print(f"{"Hours Worked":<20}", end = "")
print(f"{"Pay Rate":<15}", end = "")
print(f"{"OverTime":<15}", end = "")
print(f"{"OverTime Pay":<20}", end = "")
print(f"{"RegHour Pay":<20}", end = "")
print(f"{"Gross Pay":<20}")

print("-"*115)

print(f"{totalhours:<20}", end = "")
print(f"{rate:<15}", end = "")
print(f"{overtimehours:<15}", end = "")
print(f"${overtimepay:<19}", end = "")
print(f"${regpay:<19}", end = "")
print(f"${totalpay:<19}")