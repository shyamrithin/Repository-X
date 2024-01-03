weight = int(input("Enter your weight:" ))
unit = input("Specify units, is it (K)g or (L)bs?: ")
if unit.upper()== "K":
    converted = weight / 0.45
    print("Your weight in Lbs is: " + str(converted))
else:
    converted = weight * 0.45
    print("Your weight in Kilograms is: " + str(converted))





