# Dominic Meikle
# 3/18/25
# P3HW2
# This program calculates the pay and overtime pay using input from the user.

name = input("Enter employee's name or \"Done\" to terminate: ")
employeecount = 0
totalovertimepay = 0
totalnormalpay = 0
totalgrosspay = 0

while name.lower() != "done":
    employeecount += 1
    hours = float(input("How long did "+name+" work: "))
    rate = float(input("What is " +name+ "'s pay rate: "))
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

    totalovertimepay += overtimepay
    totalnormalpay += regpay
    totalgrosspay += (totalnormalpay + totalovertimepay)

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
    print(f"${overtimepay:<19.2f}", end = "")
    print(f"${regpay:<19.2f}", end = "")
    print(f"${totalpay:<19.2f}")

    print()
    name = input("Enter employee's name or \"Done\" to terminate: ")

print("\nTotal number of employees entered:", employeecount)
print("Total amount paid for overtime: $", format(totalovertimepay, ".2f"), sep = "")
print("Total amount paid for regular hours: $", format(totalnormalpay, ".2f"), sep = "")
print("Total amount paid in gross: $", format(totalgrosspay, ".2f"), sep = "")