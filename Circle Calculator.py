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
