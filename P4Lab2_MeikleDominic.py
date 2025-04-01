running = 'y'

while(running.lower() == 'y'):
    num = int(input("Enter an integer: "))
    num2 = 1
    if num <0:
        print("This program does not handle negative numbers.")
    else:
        for i in range(12):
            solve = num * num2
            print(f"{num} * {num2} = {solve}")
            num2 += 1
            running = 'n'

    running = input("Do you want to run the program again? ")
    if running.lower() == "yes":
        running = 'y'
    elif running.lower() == "no":
        running = 'n'
        print("Exiting...")