# Dominic Meikle
# 4/10/25
# P5Lab
# Calculate change

import random
def main():
    amount_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe ${amount_owed:.2f}")
    amount_paid = float(input("How much cash will you put into the self-checkout? "))
    change_owed = amount_paid - amount_owed
    print(f"Change is ${change_owed:.2f}")
    print()
    change_owed = round(change_owed * 100)
    disperse_change(change_owed)

def disperse_change(money):
    if money == 0:
        print("No Change Due")

    dollars = money // 100
    money = money - (dollars * 100)
    quarters = money // 25
    money = money - (quarters * 25)
    dimes = money // 10
    money = money - (dimes * 10)
    nickels = money // 5
    money = money - (nickels * 5)
    pennies = money
    money = money - pennies

    if dollars > 0:
        print(dollars, end = " ")
        if dollars == 1:
            print("Dollar")
        else:
            print("Dollars")
    if quarters > 0:
        print(quarters, end = " ")
        if quarters == 1:
            print("Quarter")
        else:
            print("Quarters")
    if dimes > 0:
        print(dimes, end = " ")
        if dimes == 1:
            print("Dime")
        else:
            print("Dimes")
    if nickels > 0:
        print(nickels, end = " ")
        if nickels == 1:
            print("Nickel")
        else:
            print("Nickels")
    if pennies > 0:
        print(pennies, end = " ")
        if pennies == 1:
            print("Penny")
        else:
            print("Pennies")

main()