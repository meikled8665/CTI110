# Dominic Meikle
# 2/27/25
# P2Lab2
# This displays he miles per gallon on the car you slect as well as calculate the amount of gas needed to drive a distance given by the user.

#create dictionary
cars = {
    "Camaro":18.21,
    "Prius":52.36,
    "Model S":110,
    "Silverado":26
}

#display results
keys = cars.keys()
print(keys)
print()

#get mpg of selected car
car_input = input("Enter a vehicle to see it's MPG: ")
print()
mpg_output = cars[car_input]

#display the mpg
print(f"The {car_input} gets {mpg_output} mpg.\n")

#calculates the amount of gas needed to drive a certain distance
distanse = float(input(f"How many miles will you drive the {car_input}? "))
gallons_needed = distanse/mpg_output

#display the anmount of gas needed
print(f"{gallons_needed:.2f} gallon(s) of gas are needed to drive the {car_input} {distanse:.2f} miles")