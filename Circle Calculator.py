import math
pi = math.pi
Diameter = float(input("Enter diameter "))
Radius = Diameter/2 or float(input("Enter Radius "))
Diameter = Radius * 2
Circumference = 2*pi*Radius or float(input("Enter Circumfernce "))
Area = pi*(Radius**2)

print("Calculation complete")
print(f"Diameter is {Diameter}")
print(f"Radius is {Radius}")
print(f"Circumference is {Circumference}")
print(f"Area is {Area}")

Semi_Circle = input("Do you need semi circle calculations ")
if Semi_Circle == "Yes" or "yes":
    Diameter_Semi = float(input("Enter Diameter"))
    Radius_Semi = Diameter_Semi /2 or float(input("Enter Radius"))
    Diameter_Semi = Radius_Semi * 2
    Circumference_Semi = (2 * pi * Radius)/2
    Area_Semi = pi*(Radius**2)/2

    print("Calculation complete")
    print(f"Diameter is {Diameter_Semi}")
    print(f"Radius is {Radius_Semi}")
    print(f"Circumference is {Circumference_Semi}")
    print(f"Area is {Area_Semi}")