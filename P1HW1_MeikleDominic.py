# Dominic Meikle
# 2/13/25
# P1HW1
# This proram does math using inputs form the user.

print(str("-"*5), str("Calculating Exponents"), str("-"*5))
print("\n")

base = int(input("Enter an integer as the base value: "))
expo = int(input("Enter an integer as the exponent: "))
print("\n")

solve1 = int(base**expo)
print(base, "raised to the power of", expo, "is", solve1)
print("\n")

print(str("-"*5), str("Addition and Subtraction"), str("-"*5))
print("\n")

start = int(input("Enter a starting integer: "))
add = int(input("Enter an integer to add: "))
sub = int(input("Enter an integer to subtract: "))
print("\n")

solve2 = int((start + add) - sub)
print(start, "+", add, "-", sub, "is equal to", solve2)
